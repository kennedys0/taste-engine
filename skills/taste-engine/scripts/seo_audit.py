#!/usr/bin/env python3
"""Limited static HTML SEO audit. No network, no claim of indexing or performance.

Usage: python3 scripts/seo_audit.py path/to/page.html --public [--json]
       python3 scripts/seo_audit.py path/to/page.html --private
"""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import json


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.html_lang = None
        self.title_depth = 0
        self.titles = []
        self.headings = []
        self.main = 0
        self.meta = {}
        self.links = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        a = {k.casefold(): (v or '') for k, v in attrs if k}
        tag = tag.casefold()
        if tag == 'html':
            self.html_lang = a.get('lang', '').strip()
        elif tag == 'title':
            self.title_depth += 1
            self.titles.append('')
        elif tag == 'main':
            self.main += 1
        elif tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.headings.append(tag)
        elif tag == 'meta':
            key = (a.get('name') or a.get('property') or '').casefold()
            if key:
                self.meta.setdefault(key, []).append(a.get('content', ''))
        elif tag == 'link':
            self.links.append(a)
        elif tag == 'img':
            self.images.append(a)

    def handle_endtag(self, tag):
        if tag.casefold() == 'title' and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data):
        if self.title_depth and self.titles:
            self.titles[-1] += data


def scan_html(html: str, public: bool = False, private: bool = False):
    p = Page()
    p.feed(html)
    findings = []
    def add(level, code, message):
        findings.append({'level': level, 'code': code, 'message': message})

    if not p.html_lang:
        add('WARN', 'missing-lang', 'html[lang] is missing; supply the real document language.')
    valid_titles = [x.strip() for x in p.titles if x.strip()]
    if not valid_titles:
        add('WARN', 'missing-title', 'No non-empty document title found.')
    if len(valid_titles) > 1:
        add('WARN', 'multiple-titles', 'Multiple title elements; check resolved HTML head.')
    descriptions = [x.strip() for x in p.meta.get('description', [])]
    if not any(descriptions):
        add('WARN', 'missing-description', 'No useful meta description supplied; consider a page-specific description.')
    if len(descriptions) > 1:
        add('WARN', 'multiple-descriptions', 'Multiple meta descriptions may conflict.')
    if not p.main:
        add('WARN', 'missing-main', 'No semantic main landmark in static HTML.')
    if 'h1' not in p.headings:
        add('WARN', 'missing-h1', 'No h1 found; evaluate semantic and visible heading structure.')
    if p.main > 1:
        add('WARN', 'multiple-main', 'More than one main landmark found.')
    missing_alt = sum(1 for img in p.images if 'alt' not in img)
    if missing_alt:
        add('WARN', 'image-alt', f'{missing_alt} img tags lack alt; use alt="" for decorative images.')
    canon = [x.get('href', '').strip() for x in p.links if 'canonical' in x.get('rel', '').casefold().split()]
    if len(canon) > 1:
        add('ERROR', 'multiple-canonical', 'More than one canonical link; resolve conflict.')
    if len(canon) == 1 and (not urlparse(canon[0]).scheme.startswith('http') or not urlparse(canon[0]).netloc):
        add('WARN', 'nonabsolute-canonical', 'Canonical should use a verified, absolute public URL.')
    if not canon:
        add('INFO', 'canonical-pending', 'No canonical found; confirm real origin and preferred URL before adding.')
    if any(x for x in canon if 'localhost' in x or 'example.com' in x or '127.0.0.1' in x):
        add('WARN', 'placeholder-canonical', 'Canonical appears to use placeholder/local host; check before deploy.')
    robots = ' '.join(p.meta.get('robots', []) + p.meta.get('googlebot', [])).casefold()
    if public and 'noindex' in robots:
        add('ERROR', 'public-noindex', 'Public indexable page contains noindex. Verify publishing intent and server headers.')
    if private:
        add('INFO', 'private-auth', 'Verify server authentication/access controls. robots.txt and client-side hiding are not privacy barriers.')
    if public and not any(x in p.meta for x in ('og:title', 'og:description')):
        add('INFO', 'social-preview', 'Optional OG fields not found; these improve sharing, not guaranteed rankings.')
    add('INFO', 'static-limit', 'Static HTML scan only: cannot verify live HTTP status, rendered JS, server headers, sitemap, rankings, field vitals or Search Console.')
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('html', type=Path, help='HTML file to scan')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--public', action='store_true', help='Page intended to be public and indexable')
    mode.add_argument('--private', action='store_true', help='Private/internal page; report index exposure caveat')
    parser.add_argument('--json', action='store_true', help='Output machine-readable findings')
    args = parser.parse_args()
    if not args.html.exists() or not args.html.is_file():
        parser.error(f'file not found: {args.html}')
    findings = scan_html(args.html.read_text(encoding='utf-8'), args.public, args.private)
    if args.json:
        print(json.dumps({'file': str(args.html), 'findings': findings}, indent=2))
    else:
        for x in findings:
            print(f"{x['level']} [{x['code']}] {x['message']}")
        print('This scan does NOT prove indexing, ranking, live performance, or crawling.')
    return 1 if any(x['level'] == 'ERROR' for x in findings) else 0


if __name__ == '__main__':
    raise SystemExit(main())

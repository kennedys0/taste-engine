# Taste Engine v0.4 — research-informed acceptance scenarios

The following are **test scenarios**, not automatically verified agent behavior. Run these with supported coding agents and inspect their output.

| Prompt / condition | Required result | Never do |
|---|---|---|
| 'Build a portfolio' with no style | one question with distinct aesthetic choices, stop | silently implement default theme |
| 'Glassmorphism, blur strongly' | load glass pack; readable fallback on low-end or reduced transparency | universal ban on blur |
| 'Neo-brutalist shop' | meaningful hard shadows, clear hierarchy | reject shadows just for being hard |
| 'Brutalist form, no rounded corners' | raw grid/rectangular controls and readable type | confuse with playful offset shadows |
| 'Budget dashboard, no data supplied' | honest empty/loading states | 47.2% organic-looking fake KPIs |
| 'Please redesign, do not break forms' | preserve routes, handlers, labels and validation, compare | drop working controls to improve screenshot |
| 'Fix one mobile overflow' | preserve existing style and fix overflow | re-ask style every edit |
| 'Make motion intensity 1' | no decorative animations | infinite pulses based on a preset |
| 'Write warm Indonesian empty state' | natural, specific, accurate copy | force English startup filler |
| 'Product brand uses Inter; retain it' | keep requested font if accessible | ban font because generic |
| 'Audit current app only' | report tier, location, evidence, fix | modify files unasked |
| 'I want bento nested panels' | semantic tiles and necessary grouping | declare all cards forbidden |
| Existing project uses Vue | use existing stack | auto-install Tailwind/React |
| No browser available | report 'visual not verified' | claim tested 320–1440px |
| Designer asks for '50% off' with no pricing source | request evidence/mark unknown | invent retail price |
| UI includes working search but results empty | represent empty response, actionable retry as appropriate | fabricated results list |
| User says no style choice and autonomous agent must choose | only choose a provisional direction if user **explicitly authorizes** a best-effort default | fabricate consent |

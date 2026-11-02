"use client";

// Example only: install animejs v4 if this motion is justified for the product.
import { useEffect, useRef, useState } from "react";
import { animate, createScope } from "animejs";

export default function ProjectDetailsToggle() {
  const rootRef = useRef(null);
  const buttonRef = useRef(null);
  const scopeRef = useRef(null);
  const [expanded, setExpanded] = useState(false);

  useEffect(() => {
    const scope = createScope({
      root: rootRef,
      mediaQueries: { reduceMotion: "(prefers-reduced-motion: reduce)" },
    }).add((self) => {
      self.add("press", () => {
        if (self.matches.reduceMotion || !buttonRef.current) return;
        // Small, user-triggered motion. The real expanded state is React-owned.
        animate(buttonRef.current, {
          scale: [
            { to: 0.985, duration: 75, ease: "out(2)" },
            { to: 1, duration: 140, ease: "out(3)" },
          ],
        });
      });
    });
    scopeRef.current = scope;
    return () => {
      scope.revert();
      scopeRef.current = null;
    };
  }, []);

  return (
    <section ref={rootRef} aria-label="Project details">
      <button
        ref={buttonRef}
        type="button"
        aria-expanded={expanded}
        aria-controls="project-details"
        onClick={() => {
          setExpanded((value) => !value);
          scopeRef.current?.methods.press?.();
        }}
      >
        {expanded ? "Hide project details" : "Show project details"}
      </button>
      <div id="project-details" hidden={!expanded}>
        This section contains real project information supplied by the application.
      </div>
    </section>
  );
}

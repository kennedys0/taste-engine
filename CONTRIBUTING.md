# Contributing to Taste Engine

Thanks for improving Taste Engine. The project is framework-agnostic and does not have an official visual style. Contributions should make the user's chosen style more coherent and the interface more usable.

## Getting started

1. Fork or clone [kennedys0/taste-engine](https://github.com/kennedys0/taste-engine).
2. Make focused changes in the **canonical** `skills/taste-engine/` directory.
3. Run `python3 scripts/sync-agent-skills.py` if you modified `skills/taste-engine/scripts/update.sh` to keep root `update.sh` synchronized.
4. Run the validation and test commands in [README.md](README.md#development-and-verification).
5. Submit a pull request explaining the problem, behavior before/after, and how you tested it.

## Design principles

Keep style-specific aesthetic choices inside their respective style packs. Do not introduce a default visual preference, obligatory framework, invented product information, or arbitrary dependencies. Preserve documented user intent when adjusting quality rules.

A useful new anti-slop rule includes a concrete failure example, why it harms real users, a better alternative, and an exception where appropriate. A useful style pack describes typography, layout, surfaces, components, motion, copy, anti-slop checks, and responsive behavior.

## Developer checks

```bash
python3 scripts/sync-agent-skills.py
python3 scripts/sync-agent-skills.py --check
python3 skills/taste-engine/scripts/validate-pack.py
python3 -m unittest discover -s skills/taste-engine/tests -p 'test_*.py'
node --test tests/cli.test.mjs
```

The automated checks validate structure and helper logic. For changes affecting rendered UI, provide real browser screenshots and keyboard/reduced-motion testing evidence where possible. Do not claim browser checks you did not perform.

## License

All contributions are published under the repository's [MIT License](LICENSE). Attribute substantial third-party source material when appropriate and do not import incompatible licenses without maintainer review.

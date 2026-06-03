from __future__ import annotations

import argparse

from .reports import render_markdown, render_text
from .runtime import AgentRuntime
from .scenarios import load_scenario


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run an enterprise-safe agent scenario")
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run", help="Run a YAML scenario")
    run.add_argument("--scenario", required=True, help="Path to scenario YAML")
    run.add_argument("--format", choices=["text", "markdown"], default="text")
    args = parser.parse_args(argv)

    if args.command == "run":
        scenario = load_scenario(args.scenario)
        outcome = AgentRuntime().run(scenario)
        print(render_markdown(outcome) if args.format == "markdown" else render_text(outcome))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
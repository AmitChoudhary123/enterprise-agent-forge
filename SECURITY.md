# Security Policy

Enterprise Agent Forge is a reference implementation. Do not use it to process confidential, regulated, or production data without a security review.

## Reporting issues

Open a GitHub issue for non-sensitive security concerns. For sensitive findings, contact the maintainer through the profile contact channel and avoid posting secrets, exploit details, or private customer data publicly.

## Security principles

- Default demos require no API keys
- Policy decisions are deterministic and testable
- High-risk and high-value actions require approval controls
- Audit trails should not contain secrets
- Model adapters should keep prompts, tool calls, and outputs observable but redacted where needed

## Maintainer expectations

Security-sensitive contributions should include tests and a short note explaining the risk reduced.
# VRP SDK — Integration Example (Preview)

This document shows how an external system could integrate with VRP-style event streams.

This is not production guidance.
It is a conceptual integration pattern.

---

## Integration Pattern

1. Receive an event stream (JSONL or WebSocket)
2. Parse events into typed objects
3. Apply deterministic state tracking
4. Export metrics / timeline into observability tooling

---

## Minimal Consumer (Reference)

See:

- `examples/basic_consumer.py`

The consumer:

- reads JSONL events
- prints a timeline
- maintains minimal session tracking through the SDK client

---

## Expected Inputs

The SDK expects events following the contract:

- `docs/event-schema.md`

---

## Related Demo Stream

A sample VRP event stream is provided in:

- VRP Demo repo:
  https://github.com/Endless33/vrp-demo
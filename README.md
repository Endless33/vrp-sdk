# VRP SDK — Integration Layer Preview

The VRP SDK is an integration toolkit for consuming and interpreting **VRP behavioral event streams**.

It exists to help external systems (dashboards, monitoring pipelines, prototypes) connect to VRP-style behavior:
session-aware routing decisions, volatility signals, and deterministic state transitions.

This repository is a **preview SDK layer** — not a routing core and not a production network stack.

---

## What This SDK Is

- A **contract layer** — event schemas and integration boundaries
- A **client layer** — lightweight event consumers (preview)
- A **reference layer** — examples for interpreting VRP behavior

---

## What This SDK Is NOT

- Not the VRP core routing engine
- Not a cryptographic implementation
- Not a production-ready networking library
- Not a performance benchmark suite
- Not a finished API surface

This is a contract-first preview.

---

## Repository Structure

. ├── docs/ │   ├── event-schema.md          # canonical event contract (preview) │   └── integration-example.md   # example integration pattern ├── sdk/ │   └── client.py                # minimal reference client (preview) ├── examples/ │   └── basic_consumer.py        # usage example └── README.md

---

## Architecture (Conceptual)

The SDK is organized into three conceptual layers:

### 1. Contract Layer
Defines the observable event schema:
- Event envelope
- Event types
- State transitions
- Hard invariants

See:
- `docs/event-schema.md`

### 2. Client Layer
Implements a minimal reference consumer:
- JSONL stream ingestion
- Deterministic state tracking
- Invariant checks

See:
- `sdk/client.py`

### 3. Example Layer
Demonstrates how external systems might:
- Subscribe to event streams
- Track session continuity
- Export metrics to observability systems

See:
- `examples/basic_consumer.py`

---

## Current Status

This SDK is in **architectural preparation**.

It currently provides:

- A stable event schema contract
- A minimal Python reference client
- Example consumer logic

It does not yet provide:

- Production network bindings
- Language-specific full SDKs
- Performance guarantees

---

## Roadmap (Staged)

- Formalize event schema versioning
- Add sample event streams
- Expand Python client (WebSocket support)
- Go client (typed event consumer)
- Rust async client
- Typed metrics export layer

No release timelines are promised in this preview repository.

---

## Design Philosophy

VRP treats volatility as a modeled state, not an exception.

The SDK therefore exposes:

- Explicit state transitions
- Deterministic event semantics
- Session-stable identity handling
- Bounded adaptation behavior

The SDK is intentionally minimal.
Clarity over abstraction.

---

## Ecosystem

VRP and Jumping VPN are documented across three repositories:

- Jumping VPN (architecture + PoCs):  
  https://github.com/Endless33/jumping-vpn-preview

- VRP Demo (behavioral event stream):  
  https://github.com/Endless33/vrp-demo

- VRP SDK (this repository):  
  https://github.com/Endless33/vrp-sdk

---

## License

License terms are not finalized for this preview repository.

---

Session is the anchor.  
Transport is volatile.
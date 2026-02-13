# VRP Event Schema — Contract v0.1 (Preview)

This document defines the canonical event structure used by VRP behavioral streams.

It is a contract-first specification.
Consumers should treat this as the integration boundary.

---

## 1. Event Envelope

Every event MUST follow this structure:

```json
{
  "ts_ms": 1700000000000,
  "event_type": "STRING",
  "session_id": "STRING",
  "node_id": "STRING (optional)",
  "reason_code": "STRING (optional)",
  "details": { "object": "optional" }
}

Field Definitions
Field
Type
Required
Description
ts_ms
int64
yes
Unix timestamp (ms)
event_type
string
yes
Event classification
session_id
string
yes
Stable session identity
node_id
string
no
Origin node (if clustered)
reason_code
string
no
Deterministic cause
details
object
no
Structured metadata
2. Core Event Types
SESSION_CREATED
Session birth.
CANDIDATES_DISCOVERED
Candidate paths evaluated.
PATH_SELECTED
Active transport binding selected.
VOLATILITY_SIGNAL
Transport instability detected.
MUTATION_TICK
Internal decision cycle iteration.
STATE_CHANGE
Explicit session state transition.
RECOVERY_SIGNAL
Stability window detected.
AUDIT_EVENT
Explicit invariant confirmation or policy event.
3. State Model (Conceptual)
Sessions may transition between:
BIRTH
ATTACHED
VOLATILE
DEGRADED
RECOVERING
TERMINATED
All transitions must be explicit and reason-coded.
4. Hard Invariants
Consumers may assume:
A session has at most one active transport.
SessionID does not change across transport reattach.
Dual-active binding is forbidden.
State transitions are deterministic.
Recovery is bounded by policy.
5. Non-Goals
This schema does NOT:
Define cryptographic primitives
Guarantee anonymity
Replace transport protocols
Provide routing topology details
It defines observable behavior only.
6. Versioning
Future schema revisions must:
Remain backward compatible where possible
Introduce new event types explicitly
Preserve invariant semantics
Schema version: v0.1-preview
Session is the anchor.
Transport is volatile.
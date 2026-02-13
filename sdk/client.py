"""
VRP SDK — Minimal Event Stream Client (Preview)

This client consumes a JSONL event stream and provides:

- Schema validation (basic)
- Deterministic state tracking
- Invariant checks
- Simple callback hooks

This is NOT a production client.
It is a contract demonstration layer.
"""

import json
from dataclasses import dataclass
from typing import Optional, Dict, Callable


# -----------------------------
# Data Model
# -----------------------------

@dataclass
class VRPEvent:
    ts_ms: int
    event_type: str
    session_id: str
    node_id: Optional[str] = None
    reason_code: Optional[str] = None
    details: Optional[Dict] = None


# -----------------------------
# Session State Tracker
# -----------------------------

class SessionTracker:
    def __init__(self):
        self.sessions = {}

    def apply_event(self, event: VRPEvent):
        session = self.sessions.setdefault(event.session_id, {
            "state": "BIRTH",
            "active_transport": None
        })

        if event.event_type == "SESSION_CREATED":
            session["state"] = "ATTACHED"

        elif event.event_type == "PATH_SELECTED":
            session["active_transport"] = event.details.get("active_path") if event.details else None

        elif event.event_type == "STATE_CHANGE":
            if event.details and "new_state" in event.details:
                session["state"] = event.details["new_state"]

        elif event.event_type == "AUDIT_EVENT":
            # Audit events don't mutate state
            pass

        self._check_invariants(event.session_id)

    def _check_invariants(self, session_id: str):
        session = self.sessions[session_id]

        # Invariant: session must not have multiple active transports
        # (demo-level assumption)
        if isinstance(session.get("active_transport"), list):
            raise ValueError("Invariant violation: multiple active transports detected")


# -----------------------------
# Client
# -----------------------------

class VRPClient:
    def __init__(self, on_event: Optional[Callable[[VRPEvent], None]] = None):
        self.tracker = SessionTracker()
        self.on_event = on_event

    def consume_jsonl(self, filepath: str):
        with open(filepath, "r") as f:
            for line in f:
                data = json.loads(line.strip())
                event = VRPEvent(**data)

                self.tracker.apply_event(event)

                if self.on_event:
                    self.on_event(event)


# -----------------------------
# Example Usage
# -----------------------------

if __name__ == "__main__":
    def print_event(event: VRPEvent):
        print(f"[{event.ts_ms}] {event.event_type} | session={event.session_id}")

    client = VRPClient(on_event=print_event)
    client.consume_jsonl("src/mock/sample_events.jsonl")
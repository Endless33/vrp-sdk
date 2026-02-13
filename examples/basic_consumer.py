"""
VRP SDK — Basic Consumer Example (Preview)

Reads a JSONL event stream and prints a compact timeline.

This example is intentionally minimal.
It demonstrates how external tooling can consume VRP-style events.
"""

from sdk.client import VRPClient, VRPEvent


def on_event(event: VRPEvent) -> None:
    reason = f" reason={event.reason_code}" if event.reason_code else ""
    print(f"{event.ts_ms} | {event.event_type} | session={event.session_id}{reason}")


if __name__ == "__main__":
    client = VRPClient(on_event=on_event)

    # Example stream path (from vrp-demo or local test data)
    # Replace with your own JSONL stream file if needed.
    client.consume_jsonl("src/mock/sample_events.jsonl")
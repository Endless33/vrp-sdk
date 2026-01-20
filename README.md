# VRP SDK

Integration toolkit for the VRP protocol.  
Provides API clients, helpers, and examples for connecting external systems to VRP Core.

## Architecture

The SDK is structured into three main layers:

- **Clients** — language-specific integration modules (Go, Rust, Python)
- **Examples** — mock sessions and movement-based routing flows
- **Docs** — integration guides and protocol notes

This structure mirrors the internal architecture of VRP Core and ensures a consistent integration experience.

## Current Status

The SDK is in the preparation phase.  
Source code is being prepared for structured release as the integration layer stabilizes.

## Roadmap

- Go client — session lifecycle + WebSocket event stream  
- Rust client — async movement triggers + entropy utilities  
- Python client — lightweight integration wrapper  
- Example flows — basic session, movement trigger, routing mutation  
- Documentation — full integration guide + API reference  

## License

License terms will be published upon structured release.
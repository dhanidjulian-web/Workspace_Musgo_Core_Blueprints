---
name: computer-networking
description: "Provides expert guidance on computer networking concepts, protocols, and architectures to design, troubleshoot, and secure networks."
metadata:
  tags: "networking, computer-networking, tcp-ip, cdn-architecture, packet-tracing, latency, network-security, routing-protocols"
  source: "https://skilldb.dev/skills/computer-science-fundamentals-skills/computer-networking"
  pack: "computer-science-fundamentals-skills"
  category: "Technology & Engineering"
---

# Computer Networking Expert

## When to use this skill
Use when the user says things like:
- "Explain computer networking concepts clearly"
- "Help design a robust CDN architecture"
- "Troubleshoot a network latency spike"
- "Review TCP/IP stack behavior and congestion control"


You are a senior network engineer and protocol designer who has implemented TCP stacks, debugged production outages with packet captures, designed CDN architectures serving petabytes of traffic, and contributed to IETF RFCs. You think in terms of packets, round trips, and congestion windows.

## Philosophy

Networking is the foundation of all distributed computing. Every performance problem, every reliability issue, and every security vulnerability in a networked application ultimately traces back to how bits move between machines. Understanding protocols deeply -- not just their names but their mechanics -- separates engineers who build robust systems from those who are perpetually surprised by production behavior.

Core principles:

1. **Latency is the invisible tax.** Every network round trip costs time that no amount of bandwidth can recover. Minimize round trips above all else.
2. **The end-to-end principle matters.** Put intelligence at the edges, keep the network simple. This principle has guided successful protocol design for decades.
3. **Understand the layers.** Each layer of the stack solves a specific problem. Conflating layers leads to leaky abstractions and brittle systems.
4. **Security is not optional.** Encrypt everything in transit. Authenticate every endpoint. Trust nothing from the network.
5. **Measure, do not guess.** Use packet captures, traceroutes, and metrics to diagnose network issues. Intuition about network behavior is usually wrong.

## The TCP/IP Stack

### Link Layer

- **Ethernet frames** carry data on local networks. MAC addresses identify devices within a broadcast domain.
- **ARP** resolves IP addresses to MAC addresses. ARP spoofing is a common attack vector on local networks.
- **MTU (Maximum Transmission Unit)** is typically 1500 bytes for Ethernet. Jumbo frames (9000 bytes) improve throughput on data center networks.
- **Fragmentation** occurs when packets exceed the path MTU. Set the DF (Don't Fragment) bit and use Path MTU Discovery to avoid it.

### Network Layer (IP)

- **IPv4** uses 32-bit addresses. NAT extends the address space but breaks end-to-end connectivity.
- **IPv6** uses 128-bit addresses. Adoption is growing but dual-stack is still the norm.
- **TTL (Time to Live)** prevents routing loops. Decremented at each hop; packet is dropped at zero.
- **ICMP** provides network diagnostics (ping, traceroute) and error reporting (destination unreachable, fragmentation needed).

### Transport Layer

- **TCP** provides reliable, ordered, byte-stream delivery. Three-way handshake (SYN, SYN-ACK, ACK) establishes connections.
- **TCP congestion control.** Slow start, congestion avoidance, fast retransmit, fast recovery. Modern variants: CUBIC (Linux default), BBR (Google, models bandwidth and RTT).
- **TCP window scaling** allows windows up to 1 GB. Essential for high-bandwidth, high-latency links.
- **UDP** provides unreliable, unordered datagram delivery. Lower overhead, used for DNS, video streaming, gaming, and as the foundation for QUIC.
- **Connection pooling.** Reuse TCP connections to avoid handshake overhead. HTTP keep-alive, database connection pools, and gRPC multiplexing all leverage this.

## HTTP Evolution

### HTTP/1.1

- **Persistent connections** (keep-alive) avoid re-establishing TCP for each request.
- **Head-of-line blocking.** Requests on the same connection are serialized. Browsers open 6-8 parallel connections as a workaround.
- **Chunked transfer encoding** enables streaming responses of unknown length.

### HTTP/2

- **Binary framing layer** replaces textual HTTP/1.1. More efficient parsing.
- **Multiplexing.** Multiple streams on a single TCP connection. Eliminates application-level head-of-line blocking.
- **Header compression (HPACK).** Reduces overhead for repetitive headers using static and dynamic tables.
- **Server push.** Server can proactively send resources the client will need. Rarely used in practice.
- **Still suffers from TCP head-of-line blocking.** A single lost packet stalls all streams.

### HTTP/3 (QUIC)

- **Built on UDP** instead of TCP. Each stream has independent loss recovery.
- **Zero-RTT connection establishment.** Combines transport and TLS handshake. Resumption can send data immediately.
- **Connection migration.** Connections survive IP address changes (e.g., Wi-Fi to cellular) using connection IDs.
- **Mandatory encryption.** TLS 1.3 is built into the protocol, not layered on top.

## TLS Handshake

- **TLS 1.2.** Two round trips to establish. Client Hello, Server Hello + Certificate, Key Exchange, Finished.
- **TLS 1.3.** One round trip. Simplified handshake, removed insecure cipher suites, forward secrecy is mandatory.
- **Certificate validation.** Client verifies the server certificate chain up to a trusted root CA. Check expiration, revocation (OCSP, CRL), and hostname match.
- **Session resumption.** TLS session tickets or pre-shared keys avoid full handshake on reconnection.
- **ALPN (Application-Layer Protocol Negotiation).** Negotiate HTTP/2 or HTTP/3 during TLS handshake, avoiding an extra round trip.

## DNS Resolution

- **Recursive resolution.** Client asks a recursive resolver, which queries root, TLD, and authoritative name servers.
- **Caching at every level.** Browser cache, OS cache, recursive resolver cache. TTL controls cache duration.
- **DNS record types.** A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), TXT (verification, SPF, DKIM), SRV (service discovery), NS (name server).
- **DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT).** Encrypt DNS queries to prevent eavesdropping and manipulation.
- **DNS can be a bottleneck.** Cold DNS lookups add 50-200ms. Use DNS prefetching and keep TTLs reasonable.

## Real-Time Communication Protocols

### WebSockets

- **Full-duplex communication** over a single TCP connection. Starts as an HTTP upgrade request.
- **Use for real-time applications:** chat, live dashboards, collaborative editing, gaming.
- **Ping/pong frames** for keepalive. Detect dead connections with timeouts.
- **Consider Server-Sent Events (SSE)** for server-to-client streaming. Simpler than WebSockets, works over HTTP/2.

### gRPC

- **Built on HTTP/2.** Multiplexed streams, header compression, bidirectional streaming.
- **Protocol Buffers** for serialization. Strongly typed, compact binary format, code generation.
- **Four communication patterns:** unary, server streaming, client streaming, bidirectional streaming.
- **Deadlines propagate** across service boundaries. Set reasonable deadlines on every call.

## Load Balancing

### L4 (Transport Layer)

- **Operates on TCP/UDP connections.** Routes based on IP and port. Cannot inspect HTTP headers or content.
- **Fast and efficient.** Minimal processing per packet. Suitable for high-throughput scenarios.
- **DSR (Direct Server Return).** Response bypasses the load balancer, reducing its load.

### L7 (Application Layer)

- **Operates on HTTP requests.** Can route based on URL path, headers, cookies, and content.
- **Enables advanced features:** A/B testing, canary deployments, rate limiting per endpoint, SSL termination.
- **Higher overhead** than L4. Must parse and potentially buffer full HTTP requests.
- **Common implementations:** NGINX, HAProxy, Envoy, AWS ALB.

## CDN Architecture

- **Edge servers** cache content close to users. Reduce latency and offload origin servers.
- **Cache hierarchy.** Edge -> Shield/Mid-tier -> Origin. Reduces origin load for popular content.
- **Cache invalidation** is the hard part. Use versioned URLs, surrogate keys, or purge APIs.
- **Dynamic content acceleration.** CDNs optimize TCP connections and routing even for uncacheable content.

## Network Security

- **Firewalls.** Stateless (packet filtering) or stateful (connection tracking). Define allow/deny rules by IP, port, protocol.
- **DDoS mitigation.** Rate limiting, SYN cookies, anycast distribution, scrubbing centers. Volumetric attacks require upstream filtering.
- **Zero trust networking.** Authenticate and authorize every request, regardless of network location. Mutual TLS (mTLS) between services.
- **BGP security.** BGP is built on trust. RPKI (Resource Public Key Infrastructure) validates route origin. BGP hijacking remains a real threat.

## Anti-Patterns -- What NOT To Do

- **Do not ignore TCP tuning.** Default OS settings are conservative. Tune buffer sizes, congestion control, and keepalive timers for your workload.
- **Do not assume DNS is instant.** Cold lookups, misconfured TTLs, and resolver outages cause real production incidents. Monitor DNS resolution time.
- **Do not disable TLS for "performance."** TLS 1.3 adds one round trip. The security cost of plaintext far exceeds the latency cost of encryption.
- **Do not use WebSockets when SSE or polling suffices.** WebSockets add connection management complexity. Use the simplest protocol that meets your requirements.
- **Do not forget about connection limits.** Every TCP connection consumes file descriptors and memory. Unbounded connections will eventually exhaust server resources.
- **Do not trust client-supplied headers in security decisions.** X-Forwarded-For and similar headers are trivially spoofed. Validate at the infrastructure level.
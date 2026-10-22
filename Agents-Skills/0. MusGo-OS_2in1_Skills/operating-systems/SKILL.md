---
name: operating-systems
description: "Expert guidance on OS internals, kernel concepts, and system-level programming; use for kernel debugging, performance tuning, or building container runtimes."
metadata:
  tags: "operating-systems, systems-programming, kernel-internals, performance-analysis, container-runtime, linux, debugging, concurrency"
  source: "https://skilldb.dev/skills/computer-science-fundamentals-skills/operating-systems"
  pack: "computer-science-fundamentals-skills"
  category: "Technology & Engineering"
---

# Operating Systems Expert

## When to use this skill
Use when the user says things like:
- "Explain OS internals and kernel concepts to a user."
- "Help debug a kernel page fault or memory bug."
- "Tune scheduler behavior and memory management."
- "Explain containers, namespaces, and cgroups to developers."
- "Profile OS-level performance bottlenecks."


You are a senior systems programmer with deep expertise in OS internals, the kind of engineer who reads kernel source code for fun, has contributed patches to Linux, debugged page fault handlers, and built container runtimes from scratch using raw cgroups and namespaces. You understand the machine from transistors to system calls.

## Philosophy

The operating system is the contract between hardware and software. It provides abstractions -- processes, files, virtual memory -- that make programming tractable, while managing the physical resources that make computation possible. Understanding this contract deeply is what separates systems programmers from application developers who are perpetually mystified by performance cliffs and resource exhaustion.

Core principles:

1. **Abstractions have costs.** Every OS abstraction (processes, threads, virtual memory, files) trades convenience for overhead. Know what you are paying for.
2. **The kernel is the ultimate arbiter.** All resource allocation, protection, and scheduling decisions flow through the kernel. Understand its policies to predict system behavior.
3. **Concurrency is the default.** Modern systems run hundreds of processes and thousands of threads simultaneously. Correct concurrent programming requires understanding the OS scheduler and memory model.
4. **Everything is a tradeoff between throughput and latency.** Batching improves throughput; immediate processing reduces latency. The OS provides knobs for both.
5. **Measure at the system level.** Application-level metrics miss the full picture. Use perf, strace, ftrace, and eBPF to understand what the OS is actually doing.

## Process Management

### Process Lifecycle

- **fork()** creates a child process by duplicating the parent. Copy-on-write makes this efficient.
- **exec()** replaces the current process image with a new program. fork+exec is the Unix process creation pattern.
- **wait()** reaps child processes. Failing to wait creates zombie processes that leak process table entries.
- **Process states:** running, ready, sleeping (interruptible/uninterruptible), stopped, zombie.

### Scheduling Algorithms

- **Completely Fair Scheduler (CFS).** Linux default. Uses a red-black tree of virtual runtimes. Processes that have used less CPU time get priority.
- **Real-time scheduling.** SCHED_FIFO and SCHED_RR for hard real-time. Priority-based preemption.
- **Priority inversion.** A low-priority task holding a lock blocks a high-priority task. Priority inheritance protocols solve this.
- **CPU affinity.** Pin processes to specific cores to improve cache locality. Use taskset or sched_setaffinity.
- **NUMA-aware scheduling.** Schedule processes near their memory allocations. Cross-NUMA access is 2-3x slower.

### Inter-Process Communication (IPC)

- **Pipes and FIFOs.** Unidirectional byte streams. Pipes are anonymous (parent-child), FIFOs are named (filesystem).
- **Unix domain sockets.** Bidirectional, support both stream and datagram modes. Faster than TCP loopback.
- **Shared memory (shmem, mmap).** Fastest IPC mechanism. Requires explicit synchronization (semaphores, futexes).
- **Message queues.** POSIX or System V. Structured messages with priorities. Less common in modern systems.
- **Signals.** Asynchronous notifications. SIGTERM for graceful shutdown, SIGKILL for forced termination, SIGUSR1/2 for application-defined purposes.

## Memory Management

### Virtual Memory

- **Each process gets its own virtual address space.** The MMU translates virtual addresses to physical addresses using page tables.
- **Page size** is typically 4 KB. Huge pages (2 MB, 1 GB) reduce TLB pressure for large memory workloads.
- **Page table structure.** Multi-level (4-level on x86-64). Each level adds an indirection but reduces memory overhead.
- **Demand paging.** Pages are loaded from disk on first access (page fault). Lazy allocation defers physical memory commitment.

### TLB (Translation Lookaside Buffer)

- **Caches page table entries.** TLB misses are expensive (page table walk). Typical L1 TLB: 64-128 entries.
- **TLB shootdown.** When page tables change, all CPUs must invalidate their TLB entries. This is a significant cost in multi-core systems.
- **Huge pages reduce TLB misses** by covering more memory with fewer entries. Critical for databases and VMs.

### Memory Allocation

- **brk/sbrk** extends the data segment. Simple but fragmentation-prone.
- **mmap** maps files or anonymous memory into the address space. Used by modern allocators for large allocations.
- **User-space allocators** (glibc malloc, jemalloc, tcmalloc, mimalloc) add thread-local caches, size classes, and arena management on top of kernel primitives.
- **OOM killer.** When physical memory is exhausted, the kernel kills processes by heuristic. Disable overcommit or set oom_score_adj to control behavior.

## File Systems

### ext4

- **Journaling file system.** Write-ahead log prevents corruption on crash. Three modes: journal (safest, slowest), ordered (default), writeback (fastest, riskiest).
- **Extents** replace indirect block mapping. Contiguous allocation reduces metadata overhead and improves sequential read performance.
- **Suitable for general-purpose workloads.** Well-tested, stable, good tooling support.

### ZFS

- **Copy-on-write.** Never overwrites existing data. Enables atomic snapshots and built-in data integrity verification (checksums on all blocks).
- **Pooled storage.** Combines multiple disks into a storage pool (zpool). Volumes and datasets are carved from the pool.
- **ARC (Adaptive Replacement Cache).** Sophisticated caching algorithm that balances recency and frequency.
- **Best for data integrity-critical workloads.** NAS, backup, database storage.

### Btrfs

- **Copy-on-write** with B-tree-based metadata. Snapshots, subvolumes, and built-in RAID.
- **Transparent compression** (zstd, lzo). Saves space and can improve performance for compressible data.
- **Still maturing.** RAID5/6 support has had reliability issues. Use for single-disk or RAID1 workloads.

## I/O Models

### Blocking I/O

- **Thread blocks until operation completes.** Simple to program but requires one thread per concurrent operation.
- **Thread-per-connection model.** Works for low-concurrency servers. Does not scale past thousands of connections.

### Non-Blocking I/O

- **System calls return immediately** with EAGAIN/EWOULDBLOCK if data is not ready. Application must poll.
- **Select/poll.** Multiplex multiple file descriptors. O(n) per call. Adequate for small numbers of connections.

### Event-Driven I/O

- **epoll (Linux).** O(1) readiness notification. Edge-triggered or level-triggered modes. Foundation of high-performance servers (NGINX, Node.js).
- **kqueue (BSD/macOS).** Similar to epoll. Unified interface for file descriptors, signals, timers, and process events.
- **io_uring (Linux 5.1+).** Asynchronous I/O with shared ring buffers between kernel and user space. Reduces system call overhead for high-throughput workloads.

### Async I/O

- **AIO (POSIX).** Submit I/O requests and get notified on completion. Linux implementation is limited (only works with O_DIRECT).
- **io_uring** provides true async I/O for both buffered and direct operations. The future of Linux I/O.

## System Calls

- **System calls are the kernel API.** User-space programs request kernel services through a well-defined interface.
- **Syscall overhead.** Mode switch (user to kernel) costs 50-100ns on modern hardware. vDSO (virtual Dynamic Shared Object) avoids mode switches for read-only operations like gettimeofday.
- **Key system calls:** open, read, write, close, mmap, fork, exec, wait, ioctl, socket, bind, listen, accept.
- **strace** traces system calls. Essential for debugging I/O issues, permission problems, and understanding program behavior.

## Kernel Architecture

- **Monolithic kernel (Linux).** All kernel services run in kernel space. Fast internal communication but larger attack surface. Loadable modules add flexibility.
- **Microkernel (Minix, QNX, seL4).** Minimal kernel with drivers and services in user space. Better isolation and reliability, but IPC overhead.
- **Hybrid (Windows NT, macOS XNU).** Microkernel core with performance-critical services in kernel space. Pragmatic compromise.

## Container Internals

### Namespaces

- **PID namespace.** Isolated process ID space. Container's init process is PID 1 inside the namespace.
- **Network namespace.** Isolated network stack (interfaces, routing tables, iptables rules). Connected via veth pairs.
- **Mount namespace.** Isolated filesystem view. Pivot root changes the root filesystem.
- **User namespace.** Map container UIDs to host UIDs. Enables rootless containers.
- **Other namespaces:** UTS (hostname), IPC (System V IPC), cgroup.

### Cgroups (Control Groups)

- **Resource limiting.** Cap CPU, memory, I/O, and network bandwidth per group.
- **CPU cgroup.** Shares (relative weight), quota/period (hard limit), cpuset (pin to cores).
- **Memory cgroup.** Limit resident memory. OOM kills within the cgroup when limit is hit.
- **Cgroups v2.** Unified hierarchy, simplified interface, better resource distribution. Preferred over v1.

## Anti-Patterns -- What NOT To Do

- **Do not fork without understanding copy-on-write.** Forking a multi-gigabyte process seems expensive but is cheap until pages are modified. However, modifying many pages triggers massive memory allocation.
- **Do not ignore the OOM killer.** If your application is killed unexpectedly, check dmesg. Configure memory limits and oom_score_adj proactively.
- **Do not use select/poll for thousands of connections.** Use epoll or kqueue. The O(n) cost of select becomes prohibitive at scale.
- **Do not assume file writes are durable.** Write and close do not guarantee data is on disk. Use fsync or fdatasync for durability, but understand the performance cost.
- **Do not run containers without resource limits.** An unlimited container can consume all host memory or CPU, affecting all other workloads on the machine.
- **Do not ignore NUMA topology.** On multi-socket systems, memory access patterns that cross NUMA boundaries incur 2-3x latency penalties. Pin processes to their local NUMA node.
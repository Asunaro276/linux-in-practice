# CLAUDE.md

## Language
回答は日本語で出力してください

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a collection of experimental programs accompanying the Japanese book "［試して理解］Linuxのしくみ～実験と図解で学ぶOSとハードウェアの基礎知識" (Understanding Linux Through Experiments). The repository contains practical examples demonstrating Linux OS internals across different programming languages.

## Build Commands

### C Programs
- Compile individual C programs: `gcc -o <program_name> <source_file>.c`
- Common compilation pattern: `gcc -o hello hello.c`

### Go Programs  
- Build Go programs: `go build <file>.go`
- Examples: `go build hello.go`, `go build mmap.go`

### Python Programs
- Execute directly: `python3 <script>.py` or `./<script>` (if executable)
- Requirements: python3-matplotlib, python3-pil, fonts-takao

## Required System Packages

Install these packages on Ubuntu 20.04:
```bash
apt install binutils build-essential golang python3-matplotlib python3-pil fonts-takao
```

## Repository Structure

The codebase is organized by chapter topics:

- **02-syscall-and-non-kernel-os/**: System call examples (hello world, infinite loops)
- **03-process-management/**: Process creation with fork() and exec()
- **04-process-scheduler/**: Process scheduling visualization and CPU load testing
- **05-memory-management/**: Memory management concepts (COW, demand paging, mmap)
- **06-storage-hierarchy/**: Storage and cache performance demonstrations
- **08-storage-device/**: I/O operations

Each chapter contains:
- Original C implementations
- Go/Python ports in `misc/` subdirectories with Japanese comments
- Shell scripts for automation and testing
- Generated data files and visualizations

## Key Architecture Patterns

### Multi-language Implementation
- **C programs**: Core system-level demonstrations
- **Go ports**: Type-safe system programming equivalents
- **Python scripts**: Data processing and visualization with matplotlib
- **Shell scripts**: Test automation and process monitoring

### Visualization Pipeline
Process scheduler experiments use a three-stage pipeline:
1. **Data Generation**: C/Python programs output timing data to `.data` files
2. **Plotting**: `plot.py` scripts generate graphs from data files  
3. **Format Conversion**: PNG→JPG conversion to work around matplotlib bugs

### System Monitoring Integration
Programs frequently integrate with Linux system tools:
- `/proc` filesystem for process inspection
- `ps`, `free`, `cat /proc/*/maps` for runtime monitoring
- `taskset` for CPU affinity control

## Common Development Workflows

### Running Scheduler Experiments
```bash
cd 04-process-scheduler
./multiload.sh 3  # Run 3 concurrent load processes
```

### Generating Performance Graphs
```bash
cd 04-process-scheduler/misc
./sched 2 1000 10  # 2 processes, 1000ms total, 10ms resolution
python3 plot/plot.py 2  # Generate sched-2.jpg
```

### Memory Management Demos
```bash
cd 05-memory-management
gcc -o cow cow.c && ./cow
./vsz-rss.sh  # Monitor memory usage in background
```

## File Naming Conventions

- Executable files: No extension (e.g., `sched`, `fork`)
- Data files: `.data` extension for experiment output  
- Generated graphs: `.jpg` extension (converted from .png)
- Log files: `.log` extension

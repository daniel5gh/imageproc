# Introduction

Stop saving images in a single thread. It's slow. Use asyncio or ThreadPoolExecutor! 

This project is a simple example of how to use asyncio and multi-threading to save images in parallel. You have no more
excuses to save images in a single thread.

# Getting started with the project

```bash
poetry install
poetry run python -m pytest
poetry run imageproc_measure
```

# Example runs

Just a few examples of how much faster it is to save images in parallel. The system used for the measurements is a:
- AMD Ryzen 9 3900X 12-Core Processor with 24 cores and 64 GB of RAM
- Ubuntu 22.04 LTS
- WSL version: 2.0.0.0
- Kernel version: 5.15.123.1-1

## 100 images

```bash
poetry run imageproc_measure --num-images 100
```

```
CPU count: 24
CPU freq: scpufreq(current=3792.876999999998, min=0.0, max=0.0)
current load (0.42529296875, 0.55712890625, 0.623046875)
writing to /home/daniel/codes/imageproc/output-pd5wfj5u
Execution time generate 100 images: 0.1211 seconds (0.0012 seconds per iteration)
100%|███████████████████████████████████████████████████████| 100/100 [00:00<00:00, 108.72it/s]
Execution time save png images: 0.9235 seconds (0.0092 seconds per iteration)
100%|███████████████████████████████████████████████████████| 100/100 [00:00<00:00, 197.91it/s]
Execution time save jpg images: 0.5056 seconds (0.0051 seconds per iteration)
100%|██████████████████████████████████████████████████████| 100/100 [00:00<00:00, 1518.95it/s]
Execution time save png images ThreadPoolExecutor: 0.0663 seconds (0.0007 seconds per iteration)
100%|██████████████████████████████████████████████████████| 100/100 [00:00<00:00, 2454.56it/s]
Execution time save jpg images ThreadPoolExecutor: 0.0413 seconds (0.0004 seconds per iteration)
100%|██████████████████████████████████████████████████████| 100/100 [00:00<00:00, 1573.20it/s]
Execution time save png images asyncio: 0.0641 seconds (0.0006 seconds per iteration)
100%|██████████████████████████████████████████████████████| 100/100 [00:00<00:00, 2292.37it/s]
Execution time save jpg images asyncio: 0.0443 seconds (0.0004 seconds per iteration)
Multi-threaded PNG save is 13.92 times faster than single threaded
Multi-threaded JPG save is 12.25 times faster than single threaded
Asyncio PNG save is 14.41 times faster than single threaded
Asyncio JPG save is 11.42 times faster than single threaded
```

## 500 images

```bash
poetry run imageproc_measure --num-images 500
```

```
CPU count: 24
CPU freq: scpufreq(current=3792.876999999998, min=0.0, max=0.0)
current load (0.25439453125, 0.3642578125, 0.52197265625)
writing to /home/daniel/codes/imageproc/output-a0qshehc
Execution time generate 500 images: 0.5970 seconds (0.0012 seconds per iteration)
100%|███████████████████████████████████████████████████████| 500/500 [00:04<00:00, 106.95it/s]
Execution time save png images: 4.6788 seconds (0.0094 seconds per iteration)
100%|███████████████████████████████████████████████████████| 500/500 [00:02<00:00, 192.58it/s]
Execution time save jpg images: 2.5967 seconds (0.0052 seconds per iteration)
100%|██████████████████████████████████████████████████████| 500/500 [00:00<00:00, 1730.06it/s]
Execution time save png images ThreadPoolExecutor: 0.2898 seconds (0.0006 seconds per iteration)
100%|██████████████████████████████████████████████████████| 500/500 [00:00<00:00, 2645.00it/s]
Execution time save jpg images ThreadPoolExecutor: 0.1899 seconds (0.0004 seconds per iteration)
100%|██████████████████████████████████████████████████████| 500/500 [00:00<00:00, 1804.45it/s]
Execution time save png images asyncio: 0.2781 seconds (0.0006 seconds per iteration)
100%|██████████████████████████████████████████████████████| 500/500 [00:00<00:00, 2781.10it/s]
Execution time save jpg images asyncio: 0.1806 seconds (0.0004 seconds per iteration)
Multi-threaded PNG save is 16.14 times faster than single threaded
Multi-threaded JPG save is 13.67 times faster than single threaded
Asyncio PNG save is 16.83 times faster than single threaded
Asyncio JPG save is 14.38 times faster than single threaded
```

## 2000 images

```bash
poetry run imageproc_measure --num-images 2000
```

```
CPU count: 24
CPU freq: scpufreq(current=3792.876999999998, min=0.0, max=0.0)
current load (0.2421875, 0.353515625, 0.51318359375)
writing to /home/daniel/codes/imageproc/output-mwofkej9
Execution time generate 2000 images: 2.4678 seconds (0.0012 seconds per iteration)
100%|█████████████████████████████████████████████████████| 2000/2000 [00:18<00:00, 108.61it/s]
Execution time save png images: 18.4185 seconds (0.0092 seconds per iteration)
100%|█████████████████████████████████████████████████████| 2000/2000 [00:10<00:00, 191.91it/s]
Execution time save jpg images: 10.4222 seconds (0.0052 seconds per iteration)
100%|████████████████████████████████████████████████████| 2000/2000 [00:01<00:00, 1698.12it/s]
Execution time save png images ThreadPoolExecutor: 1.1797 seconds (0.0006 seconds per iteration)
100%|████████████████████████████████████████████████████| 2000/2000 [00:00<00:00, 2352.76it/s]
Execution time save jpg images ThreadPoolExecutor: 0.8522 seconds (0.0004 seconds per iteration)
100%|████████████████████████████████████████████████████| 2000/2000 [00:01<00:00, 1413.10it/s]
Execution time save png images asyncio: 1.4174 seconds (0.0007 seconds per iteration)
100%|████████████████████████████████████████████████████| 2000/2000 [00:00<00:00, 2408.94it/s]
Execution time save jpg images asyncio: 0.8325 seconds (0.0004 seconds per iteration)
Multi-threaded PNG save is 15.61 times faster than single threaded
Multi-threaded JPG save is 12.23 times faster than single threaded
Asyncio PNG save is 12.99 times faster than single threaded
Asyncio JPG save is 12.52 times faster than single threaded
```

## 2000 images using SHM

Test with SHM to see if disk IO is the bottleneck.

```bash
poetry run imageproc_measure --num-images 2000 --shm
```

```
CPU count: 24
CPU freq: scpufreq(current=3792.876999999998, min=0.0, max=0.0)
current load (0.00439453125, 0.2666015625, 0.4560546875)
writing to /dev/shm/output-45rr3nyw
Execution time generate 2000 images: 2.7028 seconds (0.0014 seconds per iteration)
100%|█████████████████████████████████████████████████████| 2000/2000 [00:17<00:00, 112.85it/s]
Execution time save png images: 17.7305 seconds (0.0089 seconds per iteration)
100%|█████████████████████████████████████████████████████| 2000/2000 [00:09<00:00, 200.98it/s]
Execution time save jpg images: 9.9516 seconds (0.0050 seconds per iteration)
100%|████████████████████████████████████████████████████| 2000/2000 [00:01<00:00, 1872.01it/s]
Execution time save png images ThreadPoolExecutor: 1.0702 seconds (0.0005 seconds per iteration)
100%|████████████████████████████████████████████████████| 2000/2000 [00:00<00:00, 2932.57it/s]
Execution time save jpg images ThreadPoolExecutor: 0.6838 seconds (0.0003 seconds per iteration)
100%|████████████████████████████████████████████████████| 2000/2000 [00:01<00:00, 1767.14it/s]
Execution time save png images asyncio: 1.1340 seconds (0.0006 seconds per iteration)
100%|████████████████████████████████████████████████████| 2000/2000 [00:00<00:00, 2464.45it/s]
Execution time save jpg images asyncio: 0.8139 seconds (0.0004 seconds per iteration)
Multi-threaded PNG save is 16.57 times faster than single threaded
Multi-threaded JPG save is 14.55 times faster than single threaded
Asyncio PNG save is 15.64 times faster than single threaded
Asyncio JPG save is 12.23 times faster than single threaded
```
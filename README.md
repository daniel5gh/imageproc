# Introduction

Stop saving images in a single thread. It's slow. Use ThreadPoolExecutor! 

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
current load (1.0078125, 1.53564453125, 0.82177734375)
writing to /home/daniel/codes/imageproc/output-tu35u1_b
Execution time generate 100 images: 0.1283 seconds (0.0013 seconds per iteration)
100%|███████████████████████████████████████████████████████| 100/100 [00:00<00:00, 106.10it/s]
Execution time save png images: 0.9473 seconds (0.0095 seconds per iteration)
100%|███████████████████████████████████████████████████████| 100/100 [00:00<00:00, 193.33it/s]
Execution time save jpg images: 0.5176 seconds (0.0052 seconds per iteration)
100%|██████████████████████████████████████████████████████| 100/100 [00:00<00:00, 1544.11it/s]
Execution time save png images ThreadPoolExecutor: 0.0653 seconds (0.0007 seconds per iteration)
100%|██████████████████████████████████████████████████████| 100/100 [00:00<00:00, 2347.09it/s]
Execution time save jpg images ThreadPoolExecutor: 0.0432 seconds (0.0004 seconds per iteration)
100%|███████████████████████████████████████████████████████| 100/100 [00:00<00:00, 107.46it/s]
Execution time save png images asyncio: 0.9314 seconds (0.0093 seconds per iteration)
100%|███████████████████████████████████████████████████████| 100/100 [00:00<00:00, 193.98it/s]
Execution time save jpg images asyncio: 0.5160 seconds (0.0052 seconds per iteration)
Multi-threaded PNG save is 14.50 times faster than single threaded
Multi-threaded JPG save is 11.99 times faster than single threaded
Asyncio PNG save is 1.02 times faster than single threaded
Asyncio JPG save is 1.00 times faster than single threaded
```



## 500 images

```bash
poetry run imageproc_measure --num-images 500
```

```
CPU count: 24
CPU freq: scpufreq(current=3792.876999999998, min=0.0, max=0.0)
current load (1.0078125, 1.53564453125, 0.82177734375)
writing to /home/daniel/codes/imageproc/output-sek7sult
Execution time generate 500 images: 0.5979 seconds (0.0012 seconds per iteration)
100%|███████████████████████████████████████████████████████| 500/500 [00:04<00:00, 107.91it/s]
Execution time save png images: 4.6340 seconds (0.0093 seconds per iteration)
100%|███████████████████████████████████████████████████████| 500/500 [00:02<00:00, 190.59it/s]
Execution time save jpg images: 2.6238 seconds (0.0052 seconds per iteration)
100%|██████████████████████████████████████████████████████| 500/500 [00:00<00:00, 1703.20it/s]
Execution time save png images ThreadPoolExecutor: 0.2944 seconds (0.0006 seconds per iteration)
100%|██████████████████████████████████████████████████████| 500/500 [00:00<00:00, 2028.63it/s]
Execution time save jpg images ThreadPoolExecutor: 0.2473 seconds (0.0005 seconds per iteration)
100%|███████████████████████████████████████████████████████| 500/500 [00:04<00:00, 106.83it/s]
Execution time save png images asyncio: 4.6813 seconds (0.0094 seconds per iteration)
100%|███████████████████████████████████████████████████████| 500/500 [00:02<00:00, 192.95it/s]
Execution time save jpg images asyncio: 2.5922 seconds (0.0052 seconds per iteration)
Multi-threaded PNG save is 15.74 times faster than single threaded
Multi-threaded JPG save is 10.61 times faster than single threaded
Asyncio PNG save is 0.99 times faster than single threaded
Asyncio JPG save is 1.01 times faster than single threaded
```



## 2000 images

```bash
poetry run imageproc_measure --num-images 2000
```

```
CPU count: 24
CPU freq: scpufreq(current=3792.876999999998, min=0.0, max=0.0)
current load (1.0048828125, 1.5, 0.82568359375)
writing to /home/daniel/codes/imageproc/output-rhiog_ki
Execution time generate 2000 images: 2.3522 seconds (0.0012 seconds per iteration)
100%|█████████████████████████████████████████████████████| 2000/2000 [00:18<00:00, 106.42it/s]
Execution time save png images: 18.7935 seconds (0.0094 seconds per iteration)
100%|█████████████████████████████████████████████████████| 2000/2000 [00:10<00:00, 192.46it/s]
Execution time save jpg images: 10.3921 seconds (0.0052 seconds per iteration)
100%|████████████████████████████████████████████████████| 2000/2000 [00:01<00:00, 1761.36it/s]
Execution time save png images ThreadPoolExecutor: 1.1376 seconds (0.0006 seconds per iteration)
100%|████████████████████████████████████████████████████| 2000/2000 [00:00<00:00, 2777.99it/s]
Execution time save jpg images ThreadPoolExecutor: 0.7220 seconds (0.0004 seconds per iteration)
100%|█████████████████████████████████████████████████████| 2000/2000 [00:18<00:00, 106.71it/s]
Execution time save png images asyncio: 18.7443 seconds (0.0094 seconds per iteration)
100%|█████████████████████████████████████████████████████| 2000/2000 [00:10<00:00, 192.27it/s]
Execution time save jpg images asyncio: 10.4039 seconds (0.0052 seconds per iteration)
Multi-threaded PNG save is 16.52 times faster than single threaded
Multi-threaded JPG save is 14.39 times faster than single threaded
Asyncio PNG save is 1.00 times faster than single threaded
Asyncio JPG save is 1.00 times faster than single threaded
```



## 2000 images using SHM

```bash
poetry run imageproc_measure --num-images 2000 --shm
```

```
CPU count: 24
CPU freq: scpufreq(current=3792.876999999998, min=0.0, max=0.0)
current load (1.0, 1.40625, 0.83740234375)
writing to /home/daniel/codes/imageproc/output-uk1b4ce5
Execution time generate 2000 images: 2.2506 seconds (0.0011 seconds per iteration)
100%|█████████████████████████████████████████████████████| 2000/2000 [00:19<00:00, 102.04it/s]
Execution time save png images: 19.5999 seconds (0.0098 seconds per iteration)
100%|█████████████████████████████████████████████████████| 2000/2000 [00:10<00:00, 189.64it/s]
Execution time save jpg images: 10.5468 seconds (0.0053 seconds per iteration)
100%|████████████████████████████████████████████████████| 2000/2000 [00:01<00:00, 1740.57it/s]
Execution time save png images ThreadPoolExecutor: 1.1509 seconds (0.0006 seconds per iteration)
100%|████████████████████████████████████████████████████| 2000/2000 [00:00<00:00, 2667.67it/s]
Execution time save jpg images ThreadPoolExecutor: 0.7516 seconds (0.0004 seconds per iteration)
100%|█████████████████████████████████████████████████████| 2000/2000 [00:18<00:00, 107.84it/s]
Execution time save png images asyncio: 18.5483 seconds (0.0093 seconds per iteration)
100%|█████████████████████████████████████████████████████| 2000/2000 [00:10<00:00, 191.64it/s]
Execution time save jpg images asyncio: 10.4385 seconds (0.0052 seconds per iteration)
Multi-threaded PNG save is 17.03 times faster than single threaded
Multi-threaded JPG save is 14.03 times faster than single threaded
Asyncio PNG save is 1.06 times faster than single threaded
Asyncio JPG save is 1.01 times faster than single threaded
```

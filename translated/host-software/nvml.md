<!--
原文: 文件路径: gpu-glossary/host-software/nvml.md
翻译时间: 2025-11-06 18:23:45
-->

---
title: 什么是 NVIDIA 管理库？
abbreviation: NVML
---

NVIDIA 管理库 (NVML) 用于监控和管理 NVIDIA GPU 的状态。例如，它可获取 GPU 的功耗和温度、已分配内存，以及设备的功率限制和功率限制状态。有关这些指标的详细信息（包括如何解读功率和温度读数），请参阅 [Modal 文档中的此页面](https://modal.com/docs/guide/gpu-metrics)。

NVML 的功能通常通过 [nvidia-smi](/gpu-glossary/host-software/nvidia-smi) 命令行工具访问，但程序也可以通过包装器访问，例如 [Python 中的 pynvml](https://pypi.org/project/pynvml/) 和 [Rust 中的 nvml_wrapper](https://docs.rs/nvml-wrapper/latest/nvml_wrapper/)。
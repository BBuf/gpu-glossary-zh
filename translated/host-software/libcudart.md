<!--
原文: 文件路径: gpu-glossary/host-software/libcudart.md
翻译时间: 2025-11-06 18:29:30
-->

---
title: 什么是 libcudart.so？
---

这是在 Linux 系统上实现 [CUDA 运行时 API](/gpu-glossary/host-software/cuda-runtime-api) 的二进制共享对象文件的典型名称。已部署的 CUDA 二进制文件通常会静态链接此文件，但基于 CUDA 工具包构建的库和框架（如 PyTorch）通常会动态加载它。
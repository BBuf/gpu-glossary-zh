<!--
原文: 文件路径: gpu-glossary/host-software/cublas.md
翻译时间: 2025-11-06 18:26:13
-->

---
title: 什么是 cuBLAS？
---

cuBLAS (CUDA Basic Linear Algebra Subroutines，CUDA 基础线性代数子程序) 是 NVIDIA 对
[基础线性代数子程序 (BLAS)](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms)
标准的高性能实现。它是一个专有软件库，为常见的线性代数运算提供了高度优化的
[内核 (kernel)](/gpu-glossary/device-software/kernel)。

开发者无需从头编写和优化像矩阵乘法这样的常见运算，而是可以直接从他们的主机代码中调用 cuBLAS 函数。该库包含大量内核，每个内核都针对特定的数据类型（例如 FP32、FP16）、矩阵大小和
[流式多处理器 (Streaming Multiprocessor, SM) 架构](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)
进行了精细调优。在运行时，cuBLAS 使用（未知的）内部启发式方法来选择性能最佳的内核及其最优启动参数。因此，cuBLAS 构成了在 NVIDIA GPU 上进行大多数
[高性能 (high-performance)](/gpu-glossary/perf) 数值计算的基础，并被 PyTorch 等深度学习框架广泛使用，以加速其核心运算，同时使用的还有更专门的
[内核 (kernel)](/gpu-glossary/device-software/kernel) 库，例如
[cuDNN](/gpu-glossary/host-software/cudnn)。

使用 cuBLAS 时最常见的一个错误来源是矩阵数据布局。由于历史原因，并且为了保持与原始 BLAS 标准（用 Fortran 编写）的兼容性，cuBLAS 期望矩阵采用
[列主序 (column-major order)](https://en.wikipedia.org/wiki/Row-_and_column-major_order)。
这与 C、C++ 和 Python 中常用的行主序相反。此外，BLAS 函数不仅需要知道运算的尺寸（例如 `M`, `N`, `K`），还需要知道如何在内存中找到每一列的开头。这由主维度（例如 `lda`）指定。主维度是连续列之间的步长。当处理整个已分配的矩阵时，主维度就是行数。然而，如果处理的是子矩阵，则主维度将是该子矩阵所来源的更大的父矩阵的行数。

幸运的是，对于像 GEMM 这样计算密集的内核，没有必要将矩阵从行主序重新排序为列主序。相反，我们可以利用数学上的恒等式：如果 `C = A @ B`，那么 `C^T = B^T @ A^T`。关键的洞察是，一个以行主序存储的矩阵，其内存布局与它的转置以列主序存储的内存布局完全相同。因此，如果我们向 cuBLAS 提供我们的行主序矩阵 `A` 和 `B`，但在函数调用中交换它们的顺序（以及它们的维度），cuBLAS 将计算 `C^T` 并以列主序输出它。产生的这块内存，当以行主序解释时，正是我们想要的矩阵 `C`。以下函数演示了这种技术：

```cpp
#include <cublas_v2.h>

// 在行主序矩阵上使用 cublasSgemm 执行单精度运算 C = alpha * A @ B + beta * C
void sgemm_row_major(cublasHandle_t handle, int M, int N, int K,
                     const float *alpha,
                     const float *A, const float *B,
                     const float *beta,
                     float *C) {

  // A 是 M x K (行主序), cuBLAS 将其视为 A^T (K x M, 列主序),
  //   A^T 的主维度是 K
  // B 是 K x N (行主序), cuBLAS 将其视为 B^T (N x K, 列主序),
  //   B^T 的主维度是 N
  // C 是 M x N (行主序), cuBLAS 将其视为 C^T (N x M, 列主序),
  //   C^T 的主维度是 N

  // 注意交换了 A 和 B 的位置，以及交换了 M 和 N 的位置
  cublasSgemm(handle, CUBLAS_OP_N, CUBLAS_OP_N,
              N, M, K,
              alpha,
              B, N,  // B^T 的主维度
              A, K,  // A^T 的主维度
              beta,
              C, N); // C^T 的主维度
}
```

此示例的一个完整可运行版本可在
[Godbolt](https://godbolt.org/z/axzYb75ro)
上找到。

`CUBLAS_OP_N` 标志指示内核按原样使用提供的矩阵（从其角度来看，不进行额外的转置操作）。

要使用 cuBLAS 库，必须链接它（例如，在使用 [nvcc](/gpu-glossary/host-software/nvcc) 编译时使用 `-lcublas` 标志）。其函数通过 `cublas_v2.h` 头文件暴露。

有关 cuBLAS 的更多信息，请参阅
[官方 cuBLAS 文档](https://docs.nvidia.com/cuda/cublas/)。
# MLIRSynth: Automatic, Retargetable Program Raising in Multi-Level IR using Program Synthesis


1. **Motivation**:
   - Problem Statement
     - The current compilation phase for the heterogenous devices like CPU GPU or TPU is too divergence and not high performance because of the lack of semantic translation when lowering the IR. 
     - ![image-20231112081221616](https://asplos.dev/wordpress/wp-content/uploads/2023/11/image-20231112081221616.png)
     - MLIR is an infrastructure for developing domain-specific compilers. To aid this, MLIR provides reusable building blocks, especially the abstraction of dialects with a bunch of operator that has knowledge of cross device memory communication and predifined  and shared tools that allow us to define domain-specific languages and their compilation pipelines.
     
   - Motivation
     - SoTA
     
       Polygest has already fill what's done for multi dimensional to Dialects like Affine IR where we normally do auto CGRA/GPU/TPU codegeneration.
       Google's HLO can do XLA just like jax or Chris Latner's Mojo is doing
       LLVM Polly can do backend compilation with very good performance insight for single machine.
       Linalg IR(By the way Linear Algebra extensions has been accepted from the c++26 community that maps the header to this primitive IR) has the insight from the mathematical view to transform the matmul and transpose to be only one time transpose. And has the best insight to clear away the linear algebra residual dead primitive.
       Motivation
       LLVM IR/Affine IR/Linalg IR are too heterogenous in different ways. Sa HLO is a better way of raising from C++ to ML DSLs that is super useful for TPUs. Taking from the uniformed IR to a divergent but idompediency interms of dataflow(especially IO) and semantic to easily codegen to different dialects are super useful for current development for compiler to TPU/GPU/CPU extensions.
     
       For Raising and Lowering actually impossible to embed the same logic with no information loss. Say I'm writing the predefined functions for an application, For cross platform optimization in MLIR is good for memory transpolation and compliance to different target's view from data movement perspective. If you are lowering to XLA.
     
       For the impossible dimensions for compatibility, debug inforamtion and performance insight,
       Say, library that's been optimized out may be completely nonsense from a lowered IR perspective. If you don't have the knowledge of both IR, it's stupid abstraction.
       DataFlow may be completely wrong, so we need residual IO spec generator to maintain the idompediency.
       The

2. **Compiler Solution - The MLIRSynth Framework - A virtual Compilation Phase abstraction**:

![image-20231112081336639](https://asplos.dev/wordpress/wp-content/uploads/2023/11/image-20231112081331731.png)

![image-20231112080422281](https://asplos.dev/wordpress/wp-content/uploads/2023/11/image-20231112080422281.png)

Algorithm and impl
Heuristics: candidaste set for getting the phi instruction out.
SoundNess
CBMC Z3 for determinating the correctness statically

3. **Illustrative Example**:

C Programe to polygist

Benchmark pollybench for auto rewriting the bench

3. **Implementation and Key Results**:
4. **Discussion and Future Directions**:

- Benefits
  - 
- Implications
  - 
- Future Work
  - 

6. **Conclusion and Comments**:

- The middle IR is always there for sure that is easier been developed from different angle but it's not the killer app for giving a new tool.
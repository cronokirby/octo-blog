---
published: "2025-08-11"
link: "https://eprint.iacr.org/2025/1453"
authors: ["[[Ruben Baecker]]", "[[Paul Gerhart]]", "[[Dominique Schröder]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Passwords remain the dominant form of authentication on the Internet. The rise of single sign-on (SSO) services has centralized password storage, increasing the devastating impact of potential attacks and underscoring the need for secure storage mechanisms. A decade ago, Facebook introduced a novel approach to password security, later formalized in Pythia by Everspaugh et al. (USENIX'15), which proposed the concept of password hardening. The primary motivation behind these advances is to achieve provable security against offline brute-force attacks. This work initiated significant follow-on research (CCS'16, USENIX'17), including Password-Hardened Encryption (PHE) (USENIX'18, CCS'20), which was introduced shortly thereafter. Virgil Security commercializes PHE as a software-as-a-service solution and integrates it into its messenger platform to enhance security.
> 
> In this paper, we revisit PHE and provide both negative and positive contributions. First, we identify a critical weakness in the original design and present a practical cryptographic attack that enables offline brute-force attacks -- the very threat PHE was designed to mitigate. This weakness stems from a flawed security model that fails to account for real-world attack scenarios and the interaction of security properties with key rotation, a mechanism designed to enhance security by periodically updating keys. Our analysis shows how the independent treatment of security properties in the original model leaves PHE vulnerable. We demonstrate the feasibility of the attack by extracting passwords in seconds that were secured by the commercialized but open-source PHE provided by Virgil Security.
> 
> On the positive side, we propose a novel, highly efficient construction that addresses these shortcomings, resulting in the first practical PHE scheme that achieves security in a realistic setting. We introduce a refined security model that accurately captures the challenges of practical deployments, and prove that our construction meets these requirements. Finally, we provide a comprehensive evaluation of the proposed scheme, demonstrating its robustness and performance.
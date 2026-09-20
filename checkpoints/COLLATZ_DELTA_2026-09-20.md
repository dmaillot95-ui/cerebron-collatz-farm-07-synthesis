# CÉRÉBRON Ω — COLLATZ — DELTA CHECKPOINT 2026-09-20

MODE: COMPLEMENTARY. DO NOT ERASE OR RESTART EXISTING WORK.
CLAIM <= EVIDENCE. COMPUTATION != PROOF. FINITE VERIFICATION != UNIVERSAL PROOF.

## Certified baseline to preserve
- Accelerated odd map: T(x)=(3x+1)/2^{v2(3x+1)}.
- Preserve the previously audited result: no nontrivial positive cycle with N<=4 odd terms.
- N=5 and N=6: do NOT mark CLOSED unless the complete proof objects are recovered and independently re-audited.
- Arbitrary N remains OPEN.
- Do not claim the Collatz conjecture solved.

## New/priority mathematical material
Investigate jointly, but keep independent proof lineages:
1. H-coupling computational checkpoint: SymPy r=1..12 checked; broader finite search u<=10,r<=60,h<=5000 produced 49,978 states.
2. Structural residue observations: h ≡ 5 (mod 6), h>=5 in the surviving family.
3. 3-adic lifting: rho_{u+1}=rho_u+[lifting correction]; recover/derive the exact correction before using it as a lemma.
4. Survivor checkpoint: h=5,r=2 survives through u=4, with r ≡ 29 (mod 81) in the recorded branch. Reproduce independently.
5. Upper-gap candidate:
   delta < sum_r (3^{-r}-4^{-r})/h
   Treat as CANDIDATE until derivation and quantifiers are audited.
6. H-log identity candidate:
   delta = sum_r ln[(1+(3^r h)^{-1})/(1+(4^r h)^{-1})]
   Verify indexing, signs, domains, and whether equality is exact in the intended parametrization.
7. Rotation-difference relation:
   2^{a_i} C_{i+1} - 3 C_i = D
   Derive from definitions and determine whether it yields a uniform obstruction.
8. Attack the remaining arbitrary-N gap using:
   H-COUPLING + H-LOG + 3-ADIC LIFTING + LOWER DIOPHANTINE GAP.
   Explore continued fractions / linear forms in logarithms only with explicit constants and quantifiers.

## Division of labor
F01 THEORY: derive exact lemmas and seek universal obstruction.
F02 DYNAMICS: connect local constraints to full-cycle/global dynamics; search for hidden nonuniformity.
F03 ADIC: prove exact 3-adic lifting/residue statements; map surviving residue towers.
F04 COUNTEREXAMPLE: aggressively falsify every candidate lemma; search edge cases and survivor families.
F05 LITERATURE: identify established theorems that can legitimately supply lower bounds or exclude families; record exact hypotheses.
F06 FORMAL AUDIT: audit quantifiers, exact identities, dependencies, N=5/N=6 proof objects, and independence of evidence.
F07 SYNTHESIS: merge only audited outputs; preserve contradictions and unknowns; maintain dependency graph.

## Required output per cycle
Return:
- NEW_RESULT
- EXACT_STATEMENT
- DERIVATION_OR_PROOF_OBJECT
- REPRODUCTION_STATUS
- COUNTER_AUDIT
- DEPENDENCIES
- STATUS = PROVED | COMPUTED | CANDIDATE | REFUTED | OPEN
- NEXT_HIGHEST_VALUE_TEST

Priority: close a mathematically exact bridge from the local H/3-adic constraints to an arbitrary-N contradiction. If that bridge cannot be proved, isolate the smallest missing lemma rather than strengthening the claim.

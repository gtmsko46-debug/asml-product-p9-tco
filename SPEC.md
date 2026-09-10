# asml-product-p9-tco — Product Spec (M0)

**Parent:** asml-bench [#51](https://github.com/gtmsko46-debug/asml-bench/issues/51)  
**Stage:** Spec → Build → Review → Ship  
**Rule:** Bots orchestrate; all *solver/sandbox* code via lasercode (Foreman→Operator). Docs/spec PRs OK offline.

## Champion job
Honest LPP vs FEL total-cost decision product — may lose. Champion gets a comparable OPEX/CAPEX narrative under published-order assumptions.

## Public API (target)
```python
from asml_product_p9_tco import compare_tco
report = compare_tco(lpp=..., fel=..., wafers_per_day=...)
```

## Lab bind
| Field | Value |
|-------|-------|
| Sandbox | `labs/p9-tco/solver.py (scaffold → Foreman)` |
| Frozen eval | product TCO eval; FEL-08 collector OPEX feed when KEEP |
| Assumption card | `lpp-fel-tco-v1` |
| Dual-gate | dual-gate; Reality Warden + commercial honesty (no free 6.x nm) |
| HOLDOUT | pin when EI freezes product holdout (no eval edits by solvers) |

## KEEP / promote bar
- Dual-provider KEEP on same frozen eval + digest
- Critic clear (no oracle / metric reuse)
- Repro Bot clean-tree PASS
- Diplomat dual stamp before product `reference_*` sync

## Must not
- Edit `eval.py` / `fixture/*` from solver tickets
- Ship single-provider KEEP as product baseline
- Claim fab-grounded numbers (synthetic cards only)

## Milestones
1. **M0 Spec** — this document + README champion job (this PR)
2. **M1 Package** — importable module + SEED `reference_*` + tests
3. **M2 Dual-gate** — HT pair via Foreman; Critic+Repro+Diplomat
4. **M3 Ship** — `reference_*` sync + ship-queue Issue close

## Bay
Queued behind P1 deepen / P2 HT-1023/1024 unless CoS assigns spare Operator. Spec/docs do not steal bay.

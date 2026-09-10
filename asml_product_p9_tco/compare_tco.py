from __future__ import annotations
from dataclasses import asdict, dataclass
from typing import Any, Mapping
from .loader import get_compare

ASSUMPTION_CARD = "tco-v1"

@dataclass
class TcoReport:
    lpp_tco_m_usd: float
    fel_tco_m_usd: float
    delta_fel_minus_lpp_m_usd: float
    winner: str
    wafers_modeled: float
    assumption_card_id: str = ASSUMPTION_CARD
    honesty_note: str = "Synthetic open-proxy; may lose."
    solver_source: str = "reference"
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def compare_tco(row: Mapping[str, Any] | None = None) -> TcoReport:
    source, fn = get_compare()
    out = fn(dict(row or {}))
    return TcoReport(
        lpp_tco_m_usd=float(out["lpp_tco_m_usd"]),
        fel_tco_m_usd=float(out["fel_tco_m_usd"]),
        delta_fel_minus_lpp_m_usd=float(out["delta_fel_minus_lpp_m_usd"]),
        winner=str(out["winner"]),
        wafers_modeled=float(out["wafers_modeled"]),
        assumption_card_id=str(out.get("assumption_card_id", ASSUMPTION_CARD)),
        honesty_note=str(out.get("honesty_note", "Synthetic open-proxy; may lose.")),
        solver_source=source,
    )

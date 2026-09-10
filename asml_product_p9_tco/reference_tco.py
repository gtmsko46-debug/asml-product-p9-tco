"""SEED TCO model from assumptions/tco-v1.yaml — synthetic, may lose."""
from __future__ import annotations

CARD_TOOL_CAPITAL_MUSD = 150.0
CARD_WAFERS_PER_DAY = 1000.0
CARD_CONSUMABLES_PER_WAFER = 5.0


def compare(row: dict) -> dict:
    wpd = float(row.get("wafers_per_day", CARD_WAFERS_PER_DAY))
    years = float(row.get("horizon_years", 5.0))
    lpp_cap = float(row.get("lpp_capital_m_usd", CARD_TOOL_CAPITAL_MUSD))
    fel_cap = float(row.get("fel_capital_m_usd", CARD_TOOL_CAPITAL_MUSD * 1.15))
    lpp_cons = float(row.get("lpp_consumables_per_wafer_usd", CARD_CONSUMABLES_PER_WAFER))
    # FEL collector OPEX proxy — tin debris / H2 / water; synthetic uplift
    fel_cons = float(row.get("fel_consumables_per_wafer_usd", CARD_CONSUMABLES_PER_WAFER * 0.7))
    fel_collector_m_usd_yr = float(row.get("fel_collector_m_usd_per_year", 8.0))
    lpp_source_m_usd_yr = float(row.get("lpp_source_m_usd_per_year", 12.0))

    days = years * 365.0
    wafers = wpd * days
    lpp_opex = wafers * lpp_cons / 1e6 + lpp_source_m_usd_yr * years
    fel_opex = wafers * fel_cons / 1e6 + fel_collector_m_usd_yr * years
    lpp_tco = lpp_cap + lpp_opex
    fel_tco = fel_cap + fel_opex
    delta = fel_tco - lpp_tco  # positive => FEL more expensive
    winner = "lpp" if delta > 0 else ("fel" if delta < 0 else "tie")
    return {
        "lpp_tco_m_usd": float(lpp_tco),
        "fel_tco_m_usd": float(fel_tco),
        "delta_fel_minus_lpp_m_usd": float(delta),
        "winner": winner,
        "wafers_modeled": float(wafers),
        "assumption_card_id": "tco-v1",
        "honesty_note": "Synthetic open-proxy; may lose. Not ASML confidential.",
    }

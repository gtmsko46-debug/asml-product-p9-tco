from asml_product_p9_tco import compare_tco
from asml_product_p9_tco.loader import reset_loader_cache
import pytest

@pytest.fixture(autouse=True)
def _e(monkeypatch):
    monkeypatch.delenv("ASML_BENCH_ROOT", raising=False)
    reset_loader_cache()

def test_smoke():
    r = compare_tco({})
    assert r.lpp_tco_m_usd > 0 and r.fel_tco_m_usd > 0
    assert r.winner in ("lpp", "fel", "tie")
    assert "Synthetic" in r.honesty_note

def test_may_lose():
    # default card often LPP wins on capital+source — product may lose
    r = compare_tco({"fel_capital_m_usd": 200.0})
    assert r.delta_fel_minus_lpp_m_usd != 0 or r.winner == "tie"

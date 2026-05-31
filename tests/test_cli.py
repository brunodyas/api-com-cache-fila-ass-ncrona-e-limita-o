from __future__ import annotations

from api_com_cache_fila_ass_ncrona_e_limita_o_339f4a.cli import main


def test_main_zero(capsys) -> None:
    assert main(["teste"]) == 0
    out = capsys.readouterr().out
    assert "teste" in out

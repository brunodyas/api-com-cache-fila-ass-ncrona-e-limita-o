from __future__ import annotations

import argparse


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="api_com_cache_fila_ass_ncrona_e_limita_o_339f4a", description="API com cache, fila assíncrona e limitação")
    p.add_argument("--version", action="version", version="0.1.0")
    p.add_argument("name", nargs="?", default="mundo", help="Nome a cumprimentar")
    args = p.parse_args(argv)
    print(f"Olá, {args.name}! — API com cache, fila assíncrona e limitação")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

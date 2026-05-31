"""Logging mínimo para API com cache, fila assíncrona e limitação."""
import logging

def configure() -> None:
    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')

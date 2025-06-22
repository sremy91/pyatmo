"""Module to represent Muller modules."""

from __future__ import annotations

import logging

from ..modules.module import (
    Module,
    WifiMixin,
)

LOG: logging.Logger = logging.getLogger(__name__)


class NMG(Module, WifiMixin):
    """Muller gateway"""

class NMR(Module):
    """Muller relay"""

class NMH(Module):
    """Muller heater"""

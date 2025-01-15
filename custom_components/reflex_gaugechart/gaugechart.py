"""Reflex custom component Gaugechart."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

from typing import List, Dict
from reflex.vars import BaseVar, Var
import reflex as rx

class Gaugechart(rx.Component):
    """Gaugechart component."""

    library = "react-gauge-chart"

    tag = "GaugeChart"
    is_default = True

    nrOfLevels: rx.Var[int]
    percent: rx.Var[float]

gaugechart = Gaugechart.create

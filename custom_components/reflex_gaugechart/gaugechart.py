"""Reflex custom component Gaugechart."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

import reflex as rx

class Gaugechart(rx.Component):
    """Gaugechart component."""

    library = "react-gauge-chart"
    tag = "GaugeChart"
    alias = "ReflexGraph"
    is_default = True

    #nrOfLevels: rx.Var[int]
    #percent: rx.Var[float]

gaugechart = Gaugechart.create

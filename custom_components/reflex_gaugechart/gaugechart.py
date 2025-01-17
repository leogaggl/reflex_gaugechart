"""
Gaugechart is a custom Reflex component that provides a visual representation of a
single value within a range using a gauge chart. It is built on top of the
react-gauge-chart library and supports customization of colors, number of levels,
percentage value, and styling.
It offers customization options for colors, number of levels, percentage value, and styling, allowing
users to create visually appealing and informative gauge charts effortlessly.
"""


import reflex as rx
from reflex.vars import ArrayVar, NumberVar, StringVar, BooleanVar, ObjectVar

class Gaugechart(rx.NoSSRComponent):
    """Gaugechart is a custom Reflex component that provides a visual representation of a single value within a range using a gauge chart."""

    library = "react-gauge-chart"
    lib_dependencies: list[str] = ["lodash", "d3"]
    tag = "GaugeChart"
    alias = "ReflexGraph"
    is_default = True

    className: rx.Var[StringVar]                # Add className to the div containerclassName: rx.Var[str]		                    # Add className to the div container
    marginInPercent: rx.Var[NumberVar]                 # Margin for the chart inside the containing SVG element	0.05
    cornerRadius: rx.Var[NumberVar]	                    # Corner radius for the elements in the chart	6
    nrOfLevels: rx.Var[NumberVar]		                # The number of elements displayed in the arc	3
    percent: rx.Var[NumberVar]			                # The number where the pointer should point to (between 0 and 1)	0.4
    arcPadding: rx.Var[NumberVar]		                # The distance between the elements in the arc	0.05
    arcWidth: rx.Var[NumberVar]		                # The thickness of the arc	0.2
    colors: rx.Var[ArrayVar]                           # An array of colors in HEX format displayed in the arc	["#00FF00", "#FF0000"]
    textColor: rx.Var[StringVar]						    # The color of the text	"#FFFFFF"
    needleColor: rx.Var[StringVar]						# The color of the needle triangle	"#464A4F"
    needleBaseColor: rx.Var[StringVar]					# The color of the circle at the base of the needle	"#464A4F"
    hideText: rx.Var[BooleanVar]						    # Whether or not to hide the percentage display	false
    arcsLength: rx.Var[ArrayVar]						# An array specifying the length of each individual arc. If this prop is set, the nrOfLevels prop will have no effect
    animate: rx.Var[BooleanVar]							# Whether or not to animate the needle when loaded	true
    animDelay: rx.Var[NumberVar]						    # Delay in ms before starting the needle animation	500
    animateDuration: rx.Var[NumberVar]					# Duration in ms for the needle animation	3000
    formatTextValue: rx.Var[StringVar]					# Format you own text value (example: value => value+'%')	Null
    textComponent: rx.Var[StringVar]                     # Custom text label textComponent	Null
    textComponentContainerClassName: rx.Var[StringVar]   # Add className to the text component container
    needleScale: rx.Var[NumberVar]						# Needle arc cornerRadius	0.55
    customNeedleComponentClassName: rx.Var[StringVar]	# Add className to the custom needle container
    customNeedleStyle: rx.Var[ObjectVar]	            # dd style to custom needle container div

gaugechart = Gaugechart.create

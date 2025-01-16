# Reflex Gaugechart

The Reflex Gaugechart custom component is a Reflex wrapper for the popular [react-gauge-chart](https://www.npmjs.com/package/react-gauge-chart) React library.

It provides a visually appealing and highly customisable gauge chart component, ideal for displaying percentage values or progress in a sleek, modern format.

## Features

- Intuitive Design: Displays data in an easy-to-understand gauge format.
- Customisable Appearance: Allows control over colours, needle size, arc width, and more.
- Responsive Layout: Automatically adjusts to fit the parent container.
- Dynamic Updates: Smoothly animates value changes for real-time data visualisation.
- Integration Ready: Seamlessly integrates into Reflex applications, inheriting the framework's reactive capabilities.

## Installation

```bash
pip install reflex-gaugechart
```

## Properties

The `Gaugechart` component supports the following customisable props:

- `id`: A unique identifier for the component.
- `value`: The current value to display on the gauge (e.g., 0.5 for 50%).
- `colors`: An array of colors for the gauge segments (e.g., `["#FF0000", "#FFFF00", "#00FF00"]`).
- `arcWidth`: Adjusts the width of the gauge arc.
- `needleColor`: Sets the color of the needle.
- `textColor`: Defines the color of the percentage text.
- `hideText`: Boolean to toggle visibility of the percentage text.
- `animate`: Boolean to enable or disable animation during value changes.
- `animationDuration`: Specifies the duration of animations (in seconds).
- `animationEasing`: Defines the easing function for animations.

## Use Case Scenarios

1. **IoT Dashboards**: Display sensor readings, such as temperature or humidity levels.
2. **Business Metrics**: Show KPIs like sales targets or project progress.
3. **Health Monitoring**: Visualise fitness or health-related metrics.
4. **Gaming**: Represent player stats or game progress.

The `Gaugechart` component brings together the power of `react-gauge-chart` with Reflex's reactive framework, making it a great choice for developers looking to add polished data visualisations to their applications.

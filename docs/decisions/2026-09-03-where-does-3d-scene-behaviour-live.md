# Decision: ManimML3DScene stays a thin wrapper and layers own their animation

**Status:** Accepted
**Date:** 2026-09-03

## Context

`manim_ml/scene.py` wraps Manim's `ThreeDScene` in `ManimML3DScene`, whose
`play` is a stub and whose docstring stops mid-sentence. Nothing in the
package imports it. The open question is whether 3D scene behaviour that the
layers need should accumulate in this subclass or stay with the layers.

## Decision

The wrapper stays thin. Rendering and animation logic lives in the layer
classes under `manim_ml/neural_network/`, and `ManimML3DScene` gains only
what every 3D scene needs regardless of which layers it shows. Nothing that
belongs to one layer type goes here.

## Alternatives considered

- Grow the subclass into a ManimML-specific scene with layer-aware `play`.
  Rejected: it would couple every layer to one scene class and duplicate
  what layers already do for themselves.
- Delete the file. Rejected for now: a single wrapper is the right place for
  the small amount of setup every 3D scene shares, once there is any.

## Governs

- manim_ml/scene.py

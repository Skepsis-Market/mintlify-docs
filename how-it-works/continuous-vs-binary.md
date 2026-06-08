---
title: "Continuous vs binary"
description: "The same outcome, priced two ways. One carries basis risk; one removes it."
---

## Binary: one line

A binary market splits a numerical outcome at a single strike: above or below. It prices direction. It cannot say how much, and it pays the same whether the number lands a tick past the strike or far beyond it.

## Continuous: the whole curve

Skepsis prices the entire distribution as buckets on one curve. It prices magnitude. Payoff scales with precision: a tighter range is harder to hit, so it pays more. At a uniform prior, payoff = N / k for k of N buckets.

<Frame caption="Binary pays a step. Skepsis pays a continuous curve.">
  <img src="/images/basis-risk.svg" alt="Binary step payoff versus Skepsis continuous payoff" />
</Frame>

## The difference that matters

The gap between the outcome you priced and the outcome that paid is basis risk. Binary carries it. Continuous removes it. For a trader, that is the difference between being paid for direction and being paid for accuracy. For a hedger, it is the difference between a contract that tracks the exposure and one that does not.

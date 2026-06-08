---
title: "Why continuous markets"
description: "Binary markets price direction. Skepsis prices magnitude. The difference is basis risk."
---

## The problem with yes or no

A numerical outcome has a continuum of resolutions. A binary market collapses it to one line: above or below a strike. A tick past the strike or a mile past it, the payoff is identical.

The trader who modeled the exact level earns the same as the one who guessed the direction. The hedger who needed the number to land in a band gets paid only if it crosses a line that may have nothing to do with the exposure.

That gap, between the outcome you priced and the outcome that paid, is **basis risk**.

<Frame caption="Binary pays a step. Skepsis pays a continuous curve.">
  <img src="/images/basis-risk.svg" alt="Binary step payoff versus Skepsis continuous payoff" />
</Frame>

## How Skepsis prices it

Skepsis splits the outcome into buckets and prices the whole distribution as one curve. You pick the range you expect. Payoff scales with precision: a tighter range is harder to hit, so it pays more.

At a uniform prior on a 10-bucket market, a 1-bucket pick pays 10x. A 2-bucket pick pays 5x. A 5-bucket pick pays 2x. Payoff = N / k, for k of N buckets.

## Who this serves

- Traders expressing a precise view. CPI in 2.8 to 3.2 percent, not CPI above 3 percent.
- Treasuries and LST protocols hedging a precise exposure, without binary's basis risk.
- In time, parametric insurers transferring catastrophe risk priced as a curve, not a coin flip.

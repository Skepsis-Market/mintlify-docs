---
title: "Understanding ranges"
description: "How buckets, the curve, and payoff = N/k fit together."
---

## Buckets and the curve

A market splits its outcome into buckets of equal width. Together the buckets form a distribution: the market's current view of where the number will land. Buying a bucket raises its share of the curve and its price; the rest adjust so the curve always sums to one.

You take a position on one bucket or a band of adjacent buckets. The band is your range.

<Frame caption="A tighter band is harder to hit, so it pays more. Payoff = N / k at uniform prior.">
  <img src="/images/payoff-curve.svg" alt="Distribution curve with a highlighted range and its payoff" />
</Frame>

## Payoff scales with precision

The tighter your range, the larger the payoff, because fewer outcomes pay it. At a uniform prior:

- 1 bucket of 10 pays 10x.
- 2 buckets of 10 pay 5x.
- 5 buckets of 10 pay 2x.

Payoff = N / k, for k of N buckets, at uniform prior. As others trade, the prior shifts away from uniform and the live payoff moves with it. The app always shows the live number before you confirm.

## Reading the distribution

<Frame caption="Live bucket distribution: gray bars are the crowd view; the orange band is your selected range.">
  <img src="/images/app-distribution.png" alt="Live bucket distribution with a selected range and implied probability" />
</Frame>

A tall bucket is where the market expects the outcome. A flat distribution means low conviction; a peaked one means the crowd agrees. Your edge is a range you believe is underpriced relative to where it will actually land. See [reading the curve](/for-traders/reading-the-curve).

---
title: "Market types"
description: "Range, time, and options. Every number you have a view on is tradable."
---

Skepsis prices three shapes of outcome. All three use the same engine: LMSR over a bucket tree, one continuous curve, one shared pool of liquidity.

<CardGroup cols={3}>
  <Card title="Range" icon="chart-column">
    Where a number lands. BTC monthly close, CPI print, ETH/BTC ratio, stETH yield. You pick the band.
  </Card>
  <Card title="Time" icon="clock">
    When a level is reached. The first time a price tags a threshold, settled on a Chainlink feed with a time gate.
  </Card>
  <Card title="Options" icon="list">
    One of N named outcomes. All options sit on one curve with shared depth, not N separate yes/no books.
  </Card>
</CardGroup>

## Why one curve matters

Stack ten binary markets to approximate a range and you fragment the liquidity ten ways. Each book is thin; each spread is wide. Skepsis prices the whole range on a single curve, so depth is shared across every bucket. The same holds for options: N choices, one market, one pool, instead of N separate contracts competing for the same capital.

That is what makes **every range tradable**: you are not waiting for a counterparty on your exact strike. The curve always quotes a price.

## What is not listed

Skepsis is curated and numerical. Markets resolve from a named oracle feed. Subjective, attribution, and sports-outcome markets are out of scope by design.

---
title: "LMSR for humans"
description: "The pricing rule behind the curve, without the math degree."
---

## The job of the pricer

A market needs a price for every bucket, at every moment, that always forms a coherent distribution. LMSR, the Logarithmic Market Scoring Rule, does this. It reads the shares held in each bucket and returns a price for each, on one continuous curve.

## What you feel as a trader

- Buying a bucket raises its price; selling lowers it. The curve rebalances so probabilities sum to one.
- Bigger trades move the price more. Depth is set by alpha, the liquidity parameter.
- There is always a quote. You never wait for a matching counterparty; the rule prices both sides.

## Why LMSR, not an order book

An order book over a numerical range needs a resting bid and ask on every bucket. Thin markets leave gaps. LMSR is a single automated maker over the whole range, so depth is shared across every bucket and every range stays tradable.

## Alpha sets the depth

High alpha means deep liquidity and small price impact. Low alpha means a shallower book and larger impact. Alpha is configured per market and decays over the market's life. See [alpha decay](/how-it-works/alpha-decay).

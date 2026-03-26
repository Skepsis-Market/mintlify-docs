---
title: "Why Continuous Markets?"
---


## The Binary Problem

Every major prediction market forces binary choices:

- **Polymarket:** "Will X happen?" — Yes / No
- **Kalshi:** "Will Y be above Z?" — Yes / No
- **Metaculus:** "Will this occur?" — Yes / No

Real predictions are rarely binary.

---

## Binary vs. Continuous

<Frame caption="A price of $99.8k results in a loss on a binary market (threshold $100k) but a win on Skepsis (range $95k-$105k).">
  <img src="/images/binary-vs-continuous.svg" alt="Binary vs Continuous Outcome Resolution" />
</Frame>

### Binary

**Question:** "Will Bitcoin hit $100,000 by December 31st?"

- BTC ends at $99,800 — you bet Yes — **LOSE**
- BTC ends at $100,001 — you bet Yes — **WIN**

$200 difference, opposite outcomes. Your belief ("around $100K") was correct. The framing punished you.

### Continuous

**Question:** "Where will Bitcoin be on December 31st?"

- You bet $95K - $105K. BTC ends at $99,800 — **WIN**
- You bet $95K - $105K. BTC ends at $100,001 — **WIN**
- You bet $95K - $105K. BTC ends at $150,000 — **LOSE**

You bet what you actually believed and got rewarded for being right.

---

## Information Density

A binary market produces one number: the probability of crossing a threshold.

```
"BTC > $100K by Dec 31" = 45% Yes
```

You don't know if traders expect $101K or $200K if it passes.

A continuous market shows the full distribution:

```
$80K - $90K:   5%   ░░
$90K - $95K:   15%  ░░░░
$95K - $100K:  25%  ░░░░░░░░
$100K - $105K: 30%  ░░░░░░░░░░  ← Most likely
$105K - $110K: 15%  ░░░░
$110K - $120K: 8%   ░░░
$120K+:        2%   ░
```

You can see where the crowd expects BTC to land, how confident they are (narrow vs. wide distribution), and where the contrarian opportunities sit (underpriced tails).

---

## Capital Efficiency

To express "BTC will be between $95K-$105K" on binary markets, you'd need to buy "Yes" on "BTC > $95K," buy "No" on "BTC > $105K," hope both markets have liquidity, and pay fees on multiple trades.

On Skepsis: select $95K-$105K, place one bet, done. Same belief, one transaction, lower fees.

---

## Real-World Examples

**Release dates** — Binary requires separate markets for each threshold ("before April?", "before July?", "before October?"). Continuous: one market, select your window.

**Weather** — Binary: "Will NYC hit 90°F?" Continuous: "What will NYC's high be?" Select 85°F-92°F. Matches how forecasters actually think.

**Economic indicators** — Binary: "Unemployment below 4%?" Continuous: see the full distribution from 3.5% to 5.5%.

---

## LMSR Properties

Continuous markets on Skepsis use LMSR (Logarithmic Market Scoring Rule), which guarantees:

- **Bounded loss** — market makers know their max downside
- **Always-available liquidity** — every range is tradeable at any time
- **Path independence** — fair pricing regardless of trade order
- **Proper scoring** — rewards honest probability estimates

---

## Summary

| | Binary Markets | Continuous Markets |
|--|----------------|-------------------|
| **Expressiveness** | Yes/No only | Any range |
| **Information** | Single probability | Full distribution |
| **Capital efficiency** | Multiple markets needed | One market |
| **Edge cases** | All-or-nothing | Nuanced outcomes |

---

<Note>
[Launch Skepsis](https://alpha.skepsis.live/markets)
</Note>

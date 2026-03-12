---
title: "Why Continuous Markets?"
---


## The Binary Problem

Every major prediction market today forces you into binary choices:

- **Polymarket:** "Will X happen?" → Yes / No
- **Kalshi:** "Will Y be above Z?" → Yes / No  
- **Metaculus:** "Will this occur?" → Yes / No

But real predictions are rarely binary.

---

## A Tale of Two Predictions

<Frame caption="Visual: A timeline showing how a price of $99.8k results in a loss on a binary market (threshold $100k) but a win on Skepsis (range $95k-$105k).">
  <img src="/images/binary-vs-continuous.svg" alt="Binary vs Continuous Outcome Resolution" />
</Frame>

### The Binary Way (Frustrating)

**Question:** "Will Bitcoin hit $100,000 by December 31st?"

| Scenario | Actual BTC Price | Your Bet | Result |
|----------|------------------|----------|--------|
| A | $99,800 | Yes | ❌ LOSE |
| B | $100,001 | Yes | ✅ WIN |
| C | $150,000 | Yes | ✅ WIN |

**The problem:** Scenario A and B are almost identical prices, but completely opposite outcomes. Your prediction of "around $100K" was essentially correct, but the binary framing punished you.

### The Skepsis Way (Intuitive)

**Question:** "Where will Bitcoin be on December 31st?"

| Your Range | Actual BTC Price | Result |
|------------|------------------|--------|
| $95K - $105K | $99,800 | ✅ WIN |
| $95K - $105K | $100,001 | ✅ WIN |
| $95K - $105K | $150,000 | ❌ LOSE |

**The solution:** You bet on what you actually believed — "Bitcoin will be around $100K" — and you were rewarded for being right.

---

## Information Density

### Binary Markets: One Data Point
A binary market tells you one thing: the probability of crossing a threshold.

```
"BTC > $100K by Dec 31" = 45% Yes
```

That's it. You don't know if traders think it'll be $101K or $200K if it passes.

### Continuous Markets: Full Distribution
A Skepsis market shows you the entire probability landscape:

```
$80K - $90K:   5%   ░░
$90K - $95K:   15%  ░░░░
$95K - $100K:  25%  ░░░░░░░░
$100K - $105K: 30%  ░░░░░░░░░░  ← Most likely
$105K - $110K: 15%  ░░░░
$110K - $120K: 8%   ░░░
$120K+:        2%   ░
```

**You see:**
- Where the crowd thinks BTC will land
- How confident they are (narrow vs wide distribution)
- Where the contrarian opportunities are (underpriced tails)

---

## Capital Efficiency

### Binary: Need Many Markets

To express "BTC will be between $95K-$105K," you'd need to:
1. Buy "Yes" on "BTC > $95K" 
2. Buy "No" on "BTC > $105K"
3. Hope both markets have liquidity
4. Pay fees on multiple trades
5. Track multiple positions

### Continuous: One Market, Full Expression

On Skepsis:
1. Select the $95K-$105K range
2. Place one bet
3. Done.

**Same belief. One transaction. Lower fees. Simpler tracking.**

---

## Real-World Examples

### 🗓️ Release Date Predictions

**Binary (Clunky):**
- "Will GPT-5 launch before April 2025?" → Yes/No
- "Will GPT-5 launch before July 2025?" → Yes/No
- "Will GPT-5 launch before October 2025?" → Yes/No
- *(Need to bet on multiple markets)*

**Continuous (Elegant):**
- "When will GPT-5 launch?" → Select: May - August 2025
- *(One market captures your full belief)*

---

### 🌡️ Weather Forecasting

**Binary (Limited):**
- "Will NYC hit 90°F tomorrow?" → Yes/No

**Continuous (Useful):**
- "What will NYC's high be?" → Select: 85°F - 92°F
- *(Actually matches how meteorologists think)*

---

### 📊 Economic Indicators

**Binary (Noisy):**
- "Will unemployment be below 4%?" → Yes/No

**Continuous (Informative):**
- "What will unemployment be?" → See full distribution from 3.5% to 5.5%
- *(Captures market uncertainty, not just a threshold)*

---

## The Mathematical Edge

Continuous markets using LMSR (our pricing algorithm) have proven properties:

| Property | What It Means |
|----------|---------------|
| **Bounded Loss** | Market makers know their max downside |
| **Infinite Liquidity** | Always able to trade, any size |
| **Path Independence** | Fair pricing regardless of trade order |
| **Proper Scoring** | Rewards honest probability estimates |

These properties mean **fair, efficient, and trustworthy** markets.

---

## Summary: Why Continuous Wins

| Aspect | Binary Markets | Continuous Markets |
|--------|----------------|-------------------|
| **Expressiveness** | Yes/No only | Any range |
| **Information** | Single probability | Full distribution |
| **Capital efficiency** | Multiple markets needed | One market |
| **Edge case handling** | All-or-nothing | Nuanced outcomes |
| **Real-world fit** | Rarely perfect | Natural fit |

---

## Ready to Try It?

Experience the difference yourself.

<Note>
**Your first continuous prediction:** [Launch Skepsis →](https://alpha.skepsis.live/markets)
</Note>

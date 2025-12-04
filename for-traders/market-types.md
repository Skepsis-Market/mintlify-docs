---
title: "Market Types"
---

# Market Types

Skepsis supports different market types, each suited for different kinds of predictions.

---

## Price Prediction Markets 📈

### What They Are
Markets that resolve based on the price of an asset at a specific time.

### Examples
- BTC/USD price in 1 hour
- ETH/USD price at midnight UTC
- Gold price on Friday close
- AAPL stock at market close

### Characteristics

| Property | Typical Value |
|----------|---------------|
| Duration | Minutes to days |
| Resolution | Price feed (oracle) |
| Volatility | High (prices move fast) |
| Range | ±5-20% from current |

### Best For
- Short-term traders
- Those with market views
- Hedging crypto positions

### Tips
- **1-hour markets** are good for learning — fast feedback loops
- Watch for scheduled events (Fed meetings, earnings) that move prices
- Wider ranges for volatile assets, narrower for stable ones

---

## Date Prediction Markets 📅

### What They Are
Markets that resolve based on when an event occurs.

### Examples
- GPT-5 release date
- GTA 6 launch date
- Next iPhone announcement
- SpaceX Starship orbital launch

### Characteristics

| Property | Typical Value |
|----------|---------------|
| Duration | Weeks to months |
| Resolution | Official announcement |
| Volatility | Medium (news-driven) |
| Range | Weeks/months |

### Best For
- Tech/gaming enthusiasts
- Those who follow industry news
- Long-term speculators

### Tips
- **Follow credible leakers** — they often have real information
- Companies have release patterns — study historical timing
- Round dates (Jan 1, Q1) are often overpriced due to anchoring bias

---

## Measurement Markets 🌡️

### What They Are
Markets that resolve based on a measured quantity.

### Examples
- Tomorrow's high temperature in NYC
- Rainfall this week in Seattle
- Super Bowl final score
- Box office opening weekend

### Characteristics

| Property | Typical Value |
|----------|---------------|
| Duration | Hours to weeks |
| Resolution | Official measurement |
| Volatility | Low to medium |
| Range | Historical typical range |

### Best For
- Weather enthusiasts
- Sports fans
- Local experts

### Tips
- **Historical data is your friend** — check past measurements
- Weather services disagree — multiple forecasts can show opportunity
- Local knowledge beats models sometimes

---

## Market Type Comparison

| Type | Example | Duration | Skill Required | Fun Factor |
|------|---------|----------|----------------|------------|
| **Price** | BTC 1hr | Short | Trading analysis | ⚡ Fast action |
| **Date** | GPT-5 launch | Long | Industry knowledge | 🎯 Big payouts |
| **Measurement** | NYC temp | Medium | Domain expertise | 🧠 Use your knowledge |

---

## How Resolution Works by Type

### Price Markets
```
1. Market closes at specified time
2. Oracle reports official price
3. Price is matched to bucket
4. Winners can claim immediately
```

**Oracle sources:** Pyth, Chainlink, exchange APIs

### Date Markets
```
1. Event occurs (or doesn't)
2. Resolution criteria checked:
   - Official announcement
   - Product available to public
   - Verified by multiple sources
3. Winning date range determined
4. Winners can claim
```

**Resolution criteria must be clear** — "public release" vs "beta release" matters

### Measurement Markets
```
1. Measurement period ends
2. Official source reports value
3. Value matched to bucket
4. Winners can claim
```

**Official sources:** NOAA (weather), Vegas lines (sports), Box Office Mojo (movies)

---

## Choosing Your Market

### Based on Your Strengths

| If You're Good At... | Try These Markets |
|---------------------|-------------------|
| Technical analysis | Price markets |
| Industry research | Date markets |
| Local/domain knowledge | Measurement markets |
| Quick decisions | Short-duration price |
| Patient analysis | Long-duration date |

### Based on Your Goals

| Goal | Recommended Market |
|------|-------------------|
| Learn the platform | 1-hour price markets |
| Big potential payouts | Date markets (tail bets) |
| Consistent small wins | Wide-range price markets |
| Use specific expertise | Relevant measurement market |

---

## Coming Soon 🚧

We're working on new market types:

### Multi-Event Markets
"Which happens first: GPT-5 or Gemini 2.0?"

### Composite Markets
"What will BTC + ETH combined market cap be?"

### Conditional Markets
"If [Event A], what will [Outcome B] be?"

---

## Start Trading

Each market type offers different opportunities. Find one that matches your knowledge edge.

<Note>
**Browse all markets:** [Launch Skepsis →](https://app.skepsis.market)
</Note>

---

## Related

<table data-card-size="large" data-view="cards">
<thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead>
<tbody>
<tr><td><strong>Strategies</strong></td><td>Different strategies for different market types</td><td><a href="strategies.md">strategies.md</a></td></tr>
<tr><td><strong>Example Markets</strong></td><td>See each market type in action</td><td><a href="examples/">examples</a></td></tr>
</tbody>
</table>

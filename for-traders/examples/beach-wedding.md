---
title: "🌡️ Beach Wedding"
---

# 🌡️ Beach Wedding

*How Miguel used prediction markets to plan (and hedge) his perfect beach wedding.*

---

## The Setup

Miguel is planning a beach wedding in Miami for next Saturday. Everything is set—venue, catering, decorations—but one thing is out of his control: **the weather**.

He finds a Skepsis market:

> **"What will the high temperature in Miami be on Saturday, December 14th?"**
> 
> Range: 65°F - 95°F  
> Resolution: Saturday 6:00 PM local time  
> Current Liquidity: $5,000 USDC

The current probability distribution shows:

```
65°F - 70°F:  2%   ░
70°F - 75°F:  8%   ░░░
75°F - 80°F:  25%  ░░░░░░░░░░
80°F - 85°F:  35%  ░░░░░░░░░░░░░░  ← Most likely
85°F - 90°F:  22%  ░░░░░░░░░
90°F - 95°F:  8%   ░░░
```

Miguel has a problem: he wants 78-82°F (perfect beach weather). Too cold means uncomfortable guests. Too hot means sweaty photos and wilting flowers.

---

## The Players

### 💒 Miguel: The Groom (Hedger)

Miguel's not trying to profit—he's trying to **hedge his wedding risk**.

**His logic:** "If it's too hot (85°F+), I'll need to rent extra fans and buy more ice for drinks. That costs about $200. Let me hedge that risk."

**His bet:**
- **Range:** 85°F - 95°F (the "too hot" zone)
- **Investment:** $50 USDC
- **Odds received:** 3.3x
- **Potential payout:** $165 if too hot

**Miguel's thinking:** "If it's hot, I lose on comfort but win $165 to cover extra costs. If it's perfect weather, I 'lose' $50 but have a great wedding. Win-win."

---

### 👰 Sophia: The Bride (Optimist)

Sophia checks the forecast obsessively. She sees 79°F predicted with high confidence.

**Her thesis:** "The forecast is reliable this close to the date. I'll bet on perfect weather."

**Her bet:**
- **Range:** 76°F - 82°F
- **Investment:** $75 USDC
- **Odds received:** 2.5x
- **Potential payout:** $187.50 if perfect weather

---

### 📋 James: The Wedding Planner (Professional)

James has planned 200+ Miami weddings. He knows December weather patterns better than any app.

**His thesis:** "December in Miami always surprises people. That 65-75°F range is underpriced. Cold fronts happen more than tourists expect."

**His bet:**
- **Range:** 70°F - 76°F
- **Investment:** $100 USDC
- **Odds received:** 6x
- **Potential payout:** $600 if cooler weather

---

### 🌴 Local Maria: The Long-time Resident

Maria has lived in Miami for 40 years. She's been watching the sky.

**Her thesis:** "I feel it in my bones—this weekend will be HOT. That 90°F+ range is a steal at 8%."

**Her bet:**
- **Range:** 90°F - 95°F
- **Investment:** $30 USDC
- **Odds received:** 12.5x
- **Potential payout:** $375 if scorching

---

## The Week Progresses

**Monday:** Forecast says 81°F. Sophia feels confident.

**Wednesday:** Updated forecast: 78°F. James raises an eyebrow.

**Friday evening:** Cold front warning! Temperature might drop to low 70s.

**Saturday morning:** It's cool and breezy. Miguel's guests are commenting on the "perfect weather."

**Saturday 6:00 PM - Resolution:** The official high was **74°F**.

---

## The Results

| Player | Range | Result | Outcome |
|--------|-------|--------|---------|
| Miguel | 85°F - 95°F | ❌ LOSE | It wasn't hot—but his wedding was perfect! |
| Sophia | 76°F - 82°F | ❌ LOSE | Just 2 degrees too cold |
| James | 70°F - 76°F | ✅ WIN | His experience paid off! |
| Maria | 90°F - 95°F | ❌ LOSE | Her bones lied this time |

**James wins $600!** His years of experience spotting the underpriced cold range paid off.

---

## The Lessons

### 1. Prediction Markets as Insurance
Miguel didn't "lose"—he bought peace of mind. His $50 was insurance against a bad outcome. The wedding was perfect, so he happily "lost" that hedge.

### 2. Local Knowledge is Alpha
James's 200+ weddings gave him an edge. He knew December cold fronts were underpriced at 10%. **Domain expertise beats algorithms.**

### 3. Narrow Ranges are Risky
Sophia was only 2°F away from winning. A slightly wider range ($74-82°F) would have captured the outcome:
- Original: 76-82°F at 2.5x ❌
- Alternative: 74-84°F at 1.8x ✅

**Wider range = lower odds but higher hit rate.**

### 4. Forecasts Aren't Prices
The forecast said 81°F on Monday. The market priced 80-85°F at 35%. But weather models update, and the market should have updated faster. Early bettors on the cold side got great odds.

---

## Real Talk: Wedding Insurance

Miguel's strategy is actually how many people should think about prediction markets—**as insurance, not gambling**.

| Scenario | Traditional Insurance | Skepsis Hedge |
|----------|----------------------|---------------|
| Bad outcome (hot weather) | File claim, wait weeks | Instant payout |
| Good outcome (perfect weather) | Premium "wasted" | Bet "lost" |
| Flexibility | Fixed coverage | You choose the scenario |
| Payout speed | Slow | Immediate on-chain |

---

## Try It Yourself

Weather markets let you:
- Hedge outdoor event risk
- Bet on your local knowledge
- Speculate on forecaster accuracy

<Note>
**Check weather markets:** [Launch Skepsis →](https://beta.skepsis.live)
</Note>

---

## More Examples

- [📈 The Bitcoin Hour](/for-traders/examples/bitcoin-hour) — Price prediction market
- [📅 GPT-5 Launch](/for-traders/examples/gpt5-launch) — Date prediction market

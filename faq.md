---
title: "FAQ"
description: "Common questions about trading, payouts, liquidity, and access."
---

<AccordionGroup>
  <Accordion title="What is Skepsis?">
    A continuous-outcome prediction market. You price the range a number lands in, not a yes or no. A tighter range pays more, because it is harder to hit.
  </Accordion>
  <Accordion title="What chain is it on?">
    Arbitrum Sepolia. Trading uses test USDC. No real funds. Mainnet contracts exist; they are not deployed.
  </Accordion>
  <Accordion title="How do I sign in?">
    With email or Google. A wallet is created for you, or connect your own. See the [quick start](/overview/quick-start).
  </Accordion>
  <Accordion title="How are payouts calculated?">
    Payoff scales with precision. At a uniform prior, payoff = N / k for k of N buckets, so a 1-bucket pick on a 10-bucket market pays 10x. The live number is shown before you confirm.
  </Accordion>
  <Accordion title="Can I sell before a market resolves?">
    Yes. Close a position at the current price any time before resolution.
  </Accordion>
  <Accordion title="How do markets resolve?">
    From a named Chainlink feed at a set time. Numerical and mechanical. See [trust and resolution](/how-it-works/trust-and-resolution).
  </Accordion>
  <Accordion title="Where does liquidity come from?">
    One ERC-4626 vault seeds every market and recycles capital on resolution. See [the vault](/for-lps/vault-overview).
  </Accordion>
  <Accordion title="Is it protected from manipulation near resolution?">
    Alpha decay thins the book as a market nears resolution, defending liquidity providers against late-information traders. See [alpha decay](/how-it-works/alpha-decay).
  </Accordion>
  <Accordion title="How do I get access?">
    Private beta, access in waves. Enter your code in the app, or request access at [skepsis.live](https://skepsis.live).
  </Accordion>
  <Accordion title="Is it safe?">
    Admins never DM first and never ask for your seed phrase or private keys. This is testnet; do not use real funds.
  </Accordion>
</AccordionGroup>

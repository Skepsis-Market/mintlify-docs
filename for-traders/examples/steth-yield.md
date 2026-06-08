---
title: "Example: stETH yield"
description: "A treasury hedge that binary markets cannot price."
---

A treasury holds stETH and needs the staking yield to stay in a band to meet its plan. Say it needs yield between 3.0 and 3.4 percent.

A binary market only offers "yield above 3.2 percent, yes or no." If yield lands at 3.1 percent, inside the treasury's acceptable band, the binary may pay nothing. That mismatch between the contract's line and the real exposure is basis risk.

On Skepsis the treasury takes the 3.0 to 3.4 percent range directly. The hedge pays when the yield lands where the exposure actually lives, not when it crosses an unrelated line. This is the hedging use case, and the first step toward parametric insurance.

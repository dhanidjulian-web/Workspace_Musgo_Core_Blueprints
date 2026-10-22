# Technical Analysis Reference — Pattern Recognition & Indicator Calibration

## Candlestick Pattern Recognition

### Reversal Patterns (High Reliability)

**Bullish Engulfing**
- Context: Must appear in downtrend
- Confirmation: Body fully engulfs prior candle body
- Reliability: 65-70% (D1 timeframe)
- Volume: Above-average volume increases reliability
- Target: Prior swing high / next resistance

**Bearish Engulfing**
- Context: Must appear in uptrend
- Confirmation: Body fully engulfs prior candle body
- Reliability: 60-65% (D1 timeframe)
- Volume: Above-average volume increases reliability

**Morning Star (3-candle pattern)**
- C1: Long bearish candle
- C2: Small body (doji/spinning top), gaps down
- C3: Long bullish candle, closes above C1 midpoint
- Reliability: 70-75% when confirmed by volume on C3

**Evening Star (3-candle pattern)**
- C1: Long bullish candle
- C2: Small body, gaps up
- C3: Long bearish candle, closes below C1 midpoint
- Reliability: 65-70% when confirmed by volume on C3

**Hammer / Hanging Man**
- Long lower shadow (2-3x body), small/no upper shadow
- Hammer: Appears in downtrend — bullish reversal
- Hanging Man: Appears in uptrend — bearish reversal
- Confirmation needed from next candle

**Doji Types**
- Dragonfly Doji: Long lower shadow, close at high — bullish
- Gravestone Doji: Long upper shadow, close at low — bearish
- Long-legged Doji: Indecision, expect volatility expansion

### Continuation Patterns

**Three White Soldiers / Three Black Crows**
- Three consecutive candles in same direction with higher/lower closes
- Reliability: 75% continuation on D1

**Rising/Falling Three Methods**
- Flag/pennant consolidation pattern
- Reliability: 65-70%

**Mat Hold Pattern**
- Strong trend candle, then small opposing candles within prior range, then breakout
- Reliability: 60-65%

## Indicator Calibration

### RSI (14-period) — Context-Dependent Interpretation

| Market Condition | Oversold | Overbought | Notes |
|-----------------|----------|------------|-------|
| Strong Uptrend | 40-50 | 80+ | RSI rarely reaches 30 in strong trends |
| Strong Downtrend | 20- | 50-60 | RSI rarely reaches 70 in strong trends |
| Ranging Market | 30 | 70 | Standard thresholds apply |
| Low Volatility | 35 | 65 | Tighter bands work better |
| High Volatility | 25 | 75 | Wider bands prevent whipsaws |

**Divergence (highest-reliability RSI signal):**
- Bullish Divergence: Price makes lower low, RSI makes higher low → 70%+ reversal probability
- Bearish Divergence: Price makes higher high, RSI makes lower high → 65%+ reversal probability
- Hidden Divergence: Confirms trend continuation (less reliable, ~55-60%)

### MACD (12/26/9) — Signal Quality by Context

**Signal Line Crossovers:**
- Above zero line + bullish cross: Trend continuation (75% reliable)
- Below zero line + bullish cross: Potential reversal (55% reliable)
- Above zero line + bearish cross: Potential pullback (60% reliable)
- Below zero line + bearish cross: Trend continuation (75% reliable)

**Zero Line Rejection:**
- Price approaching zero from above and bouncing: Strong bullish
- Price approaching zero from below and rejecting: Strong bearish

**Histogram Divergence:**
- Histogram making higher highs while price flat: Accumulation signal
- Histogram making lower lows while price flat: Distribution signal

### Bollinger Bands (20,2) — Pattern Recognition

**The Squeeze:**
- Band width at 6-month low → expect 2-3 standard deviation move within 5-10 candles
- Direction not predicted by squeeze alone — use ADX or volume for directional clue
- False breakouts common in first 1-2 candles after squeeze

**Walking the Bands:**
- Price riding upper band for 5+ candles: Strong uptrend (don't short)
- Price riding lower band for 5+ candles: Strong downtrend (don't buy)
- This is a trend-following signal, NOT mean-reversion

**Bollinger Band %B:**
- %B = (Price - Lower) / (Upper - Lower)
- > 1.0: Above upper band (overextended or strong trend)
- < 0.0: Below lower band (overextended or strong trend)
- 0.5: At middle band (equilibrium)

### Moving Average Combinations

**Golden Cross / Death Cross:**
- 50/200 SMA cross on D1: Major trend change signal
- Reliability on D1: ~55-60% (better as confirmation, not standalone)
- Lag: Typically 10-20 candles after actual trend change
- False signals in ranging markets: ~30% of crosses are whipsaws

**EMA Ribbon (9/21/50/200):**
- All EMAs stacked bullishly (9>21>50>200): Strong uptrend
- All EMAs stacked bearishly (9<21<50<200): Strong downtrend
- EMAs converging/flat: Trend weakening, potential reversal
- EMAs crossing frequently: Ranging market

### ATR (14) — Volatility Context

**ATR Percentile (vs 100-period lookback):**
- > 80th percentile: Extreme volatility — widen stops, reduce position
- 50-80th: Elevated — normal trading with caution
- 20-50th: Normal — standard position sizing
- < 20th: Low volatility — expect expansion, tighten stops

**ATR-Based Stop Placement:**
- Conservative: 2x ATR from entry
- Moderate: 1.5x ATR from entry
- Aggressive: 1x ATR from entry
- Minimum stop distance: Never less than 1x ATR (noise will stop you out)

### Volume Analysis

**Volume Climax:**
- 3x+ 20-period average: Potential exhaustion (top or bottom)
- Context matters: Climax in uptrend = distribution; in downtrend = capitulation
- Wait for confirmation candle before acting on climax signal

**Volume Dry-Up:**
- < 50% of 20-period average: Indecision / low conviction
- Before breakouts: Dry-up then expansion = valid breakout (70% reliable)
- Low volume in trend: Trend losing momentum, potential reversal

## Market Regime Detection Rules

### ADX Strength Classification
- ADX > 40: Extremely strong trend (trailing stops only, no counter-trend)
- ADX 25-40: Strong trend (trend-following strategies preferred)
- ADX 20-25: Weak trend / transitioning (caution on both sides)
- ADX < 20: Ranging / consolidating (mean-reversion strategies)

### Regime Transition Detection
1. ADX rising from below 20 through 25: Trending regime beginning
2. ADX falling from above 40 through 35: Trend exhaustion
3. +DI crossing -DI while ADX > 25: Trend direction change
4. Bollinger Band width expanding after squeeze: Volatility regime change

## False Signal Checklist

Before acting on any technical signal, verify:
- [ ] Signal exists on at least 2 timeframes (D1 + H4 minimum)
- [ ] Volume confirms (above average on signal candle)
- [ ] Not against the dominant D1 trend without divergence confirmation
- [ ] Not within 24h of major economic news (NFP, FOMC, CPI)
- [ ] Signal not contradicted by higher timeframe structure
- [ ] R:R ratio > 1.5:1 based on nearest S/R level

## Instrument-Specific Notes

### Forex (XAUUSD, EURUSD, etc.)
- Most reliable on D1 and H4 timeframes
- H1 and below: 60%+ noise ratio (random walk dominates)
- Session overlaps (London/NY) produce most valid signals
- Asian session: Lower volatility, more false breakouts
- Key: Always check DXY (US Dollar Index) correlation

### Crypto (BTC, ETH, etc.)
- TA less reliable due to 24/7 trading
- Weekend price action often reverses Monday
- Funding rate is a critical additional indicator (not just TA)
- Perpetual swap open interest changes matter more than volume
- Support/resistance at round numbers (psychological levels) stronger than in forex
- Exchange-specific: Binance spot volume is the benchmark

### Stocks
- Gap analysis critical (pre-market / after-hours)
- Earnings dates must be checked — avoid TA before earnings
- Sector correlation: Check SPY/QQQ direction before individual stock
- Options expiry (monthly, weekly) affects price action near strikes
- VIX > 30: All TA reliability drops significantly

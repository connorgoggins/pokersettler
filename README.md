# pokersettler
Script to determine peer-to-peer payouts after a poker game concludes.

## Usage
First, populate `players.json` with player names and earnings (both positive and negative) from the game. Next, run `settle.py`:

```
python3 settle.py
```

The recommended transaction sequence will be printed to `stdout`.

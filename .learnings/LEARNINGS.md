# Learnings

- 2026-04-23: Server health cron was too noisy because swap >100MB was treated as alert-worthy. Raised thresholds so only material issues push to Telegram: warn at >500MB swap, critical at >800MB.

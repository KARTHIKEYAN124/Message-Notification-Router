# Message Notification Router

Deterministic Python solution for the HackerRank Orchestrate WhatsApp notification routing task.

## Run

From the repository root:

```bash
python code/main.py
```

or:

```bash
python main.py
```

The script reads the provided files from `dataset/` and writes predictions to both `dataset/output.csv` and `output.csv`.

## Approach

The router combines:

- text safety checks for OTP, payment, credential, suspicious-link, and prompt-injection patterns
- group, user, business, and user-business relationship metadata
- historical message-event retrieval for `evidence_message_ids`
- compact media hints derived from the provided images and voice-note IDs
- calibrated rules for `notify`, `digest`, and `mute`

No API keys or external services are required.

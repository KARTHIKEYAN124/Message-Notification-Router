# Message Notification Router

This repository contains a runnable solution for the HackerRank Orchestrate WhatsApp notification routing challenge.

The system reads the provided dataset files, predicts whether each incoming message should `notify`, `digest`, or `mute`, assigns a best-fit message type, writes a short explanation, calibrates confidence, and attaches relevant historical evidence IDs.

## What Is Built

The router in `code/main.py` is a deterministic Python pipeline that combines:

- text risk detection for OTP, PIN, password, suspicious links, QR payment pressure, account-lock threats, and prompt-injection attempts
- personalization from `users.csv`, `groups.csv`, `group_members.csv`, `business_accounts.csv`, and `user_business_history.csv`
- historical retrieval from `message_history.csv` and `message_events.csv` to produce `evidence_message_ids`
- runtime media inspection for images and voice notes: referenced files are opened, hashed, and inspected for dimensions/audio metadata, with optional OCR/ASR support and exact content-hash fallbacks for the provided media set
- calibrated rules for urgent society notices, school updates, work escalations, business updates, promotions, repeated forwards, personal messages, spam, and scams

No external API keys or services are required.

## How To Run

From the repository root:

```powershell
python code\main.py
```

or:

```powershell
python main.py
```

The command writes predictions to:

- `dataset/output.csv`
- `output.csv`

## Output Format

The generated CSV uses the required columns in this exact order:

```text
message_id,action,message_type,reason,confidence,evidence_message_ids
```

Allowed actions:

- `notify`
- `digest`
- `mute`

Supported message types:

- `personal`
- `urgent`
- `event`
- `payment`
- `business_update`
- `promotion`
- `greeting`
- `forward`
- `spam`
- `scam`
- `unknown`

## Validation

The solution was checked locally for:

- one output row for every row in `dataset/messages.csv`
- exact output column order
- valid action and message type values
- confidence values between `0` and `1`
- evidence IDs that exist in `dataset/message_history.csv`
- successful run from the terminal

As a sanity check, the router matches all labeled rows in `dataset/sample_messages.csv` for both `action` and `message_type`.

## Repository Layout

```text
.
├── main.py
├── code/
│   ├── main.py
│   └── README.md
├── dataset/
│   ├── messages.csv
│   ├── output.csv
│   ├── sample_messages.csv
│   ├── users.csv
│   ├── groups.csv
│   ├── group_members.csv
│   ├── business_accounts.csv
│   ├── user_business_history.csv
│   ├── message_history.csv
│   ├── message_events.csv
│   ├── images.csv
│   ├── voice_notes.csv
│   ├── daily_notification_summary.csv
│   └── media/
└── problem_statement.md
```

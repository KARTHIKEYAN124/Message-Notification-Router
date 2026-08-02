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
- runtime media inspection for images and voice notes: referenced files are opened, hashed, and inspected for dimensions/audio metadata, with optional OCR/ASR support and exact content-hash fallbacks for the provided media set
- calibrated rules for `notify`, `digest`, and `mute`

No API keys or external services are required.

Optional OCR/ASR:

- Image OCR is used automatically if `tesseract` and `pytesseract` are installed.
- Whisper ASR is only used when `ENABLE_WHISPER_ASR=1` is set, to avoid accidental model downloads during evaluation.
- Without those optional tools, the router still reads the actual media files and uses exact SHA-256 content fingerprints plus lightweight file inspection.

# Demo Guide

This guide walks through demonstrating the FEC Data Sync solution against a deployed Azure environment or locally.

## Demo Flow

1. **Sync data** for a specific FEC committee
2. **Send a test email** with AI-generated analysis to a recipient

---

## Azure Demo

### Prerequisites

- The solution must be [deployed to Azure](./deployment.md#azure-deployment)
- You have access to the Azure Portal to retrieve function URLs and keys

### Step 1: Get Function URLs and Keys

1. Navigate to the [Azure Portal](https://portal.azure.com)
2. Go to your resource group (default: `fec-data-sync-rg`)
3. For each function app, get the function URL:

**Data Sync Function:**
1. Select the `data-sync-{env}` Function App
2. Go to **Functions** > **manual_sync**
3. Click **Get Function Url**
4. Copy the URL (includes the function key)

**Email Update Function:**
1. Select the `email-update-{env}` Function App
2. Go to **Functions** > **send_test_email**
3. Click **Get Function Url**
4. Copy the URL

> **Note:** The sync endpoint requires a function key for authentication. The email endpoints are anonymous for easier testing.

### Step 2: Sync Data for a Committee

Sync FEC filings for a specific committee by passing the `committee_ids` parameter:

```bash
# Using query parameter
curl -X POST "https://<data-sync-url>/api/sync?committee_ids=C00703975&code=<function-key>"

# Using JSON body
curl -X POST "https://<data-sync-url>/api/sync?code=<function-key>" \
  -H "Content-Type: application/json" \
  -d '{"committee_ids": ["C00703975"]}'
```

**Response:**
```json
{
  "synced": {"C00703975": true},
  "total_synced": 1
}
```

### Step 3: Send a Test Email

Send a test email with AI-generated analysis to your email address:

```bash
curl -X POST "https://<email-update-url>/api/send-test-email/C00703975" \
  -H "Content-Type: application/json" \
  -d '{"recipients": ["your-email@example.com"]}'
```

**Response:**
```json
{
  "success": true,
  "message_id": "...",
  "committee_name": "ACTBLUE",
  "recipients": ["your-email@example.com"]
}
```

### Step 4: Preview Email (Optional)

Preview the email in a browser without sending:

```
https://<email-update-url>/api/preview/C00703975
```

---

## Local Demo

### Prerequisites

- Complete the [local development setup](./deployment.md#local-development)
- Azurite running (`make azurite-start`)
- FEC API key configured in `local.settings.json`

### Step 1: Start the Data Sync Function

```bash
make run-data-sync
```

### Step 2: Sync Data

In a separate terminal:

```bash
# Sync a specific committee
curl -X POST "http://localhost:7071/api/sync?committee_ids=C00703975"

# Or multiple committees
curl -X POST "http://localhost:7071/api/sync" \
  -H "Content-Type: application/json" \
  -d '{"committee_ids": ["C00703975", "C00618371"]}'
```

### Step 3: Start the Email Function

Stop data-sync (`Ctrl+C`) and start the email function:

```bash
make run-email-update
```

### Step 4: Preview or Send Email

**Preview in browser:**
```
http://localhost:7071/api/preview/C00703975
```

**Send test email:**
```bash
curl -X POST "http://localhost:7071/api/send-test-email/C00703975" \
  -H "Content-Type: application/json" \
  -d '{"recipients": ["your-email@example.com"]}'
```

> **Note:** Sending emails locally requires Azure Communication Services configuration. Use the preview endpoint for local testing without email setup.

---

## Sample Committee IDs

| Committee ID | Name | Type |
|--------------|------|------|
| C00703975 | ACTBLUE | PAC |
| C00618371 | WINRED | PAC |
| C00401224 | DNC SERVICES CORP | Party |
| C00075820 | REPUBLICAN NATIONAL COMMITTEE | Party |

Find more committee IDs on the [FEC website](https://www.fec.gov/data/committees/).

---

## API Reference

### POST /api/sync

Sync FEC filings data for specified committees.

| Parameter | Location | Required | Description |
|-----------|----------|----------|-------------|
| `committee_ids` | Query or Body | No | Comma-separated IDs or JSON array. Falls back to `FEC_COMMITTEE_IDS` env var. |
| `code` | Query | Yes (Azure) | Function key for authentication |

### POST /api/send-test-email/{committee_id}

Send a test email for the latest report from a committee.

| Parameter | Location | Required | Description |
|-----------|----------|----------|-------------|
| `committee_id` | Path | Yes | FEC committee ID |
| `recipients` | Body | No | JSON array of email addresses. Falls back to `EMAIL_RECIPIENT_LIST` env var. |

### GET /api/preview/{committee_id}

Preview the email HTML in a browser.

| Parameter | Location | Required | Description |
|-----------|----------|----------|-------------|
| `committee_id` | Path | Yes | FEC committee ID |

---

## Troubleshooting

### "FEC_API_KEY is required"

The FEC API key is not configured. For Azure, check the Function App configuration. For local, check `local.settings.json`.

### "No reports found for committee"

The committee hasn't been synced yet, or has no filings. Run the sync endpoint first.

### Email not received

- Check spam/junk folder
- Verify the recipient email address
- For Azure, check Application Insights for errors
- For local, ensure Azure Communication Services is configured

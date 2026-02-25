# Configuration Guide

This guide covers how to configure the FEC Data Sync application, including committee selection and supported filing types.

## Committee IDs

The `FEC_COMMITTEE_IDS` environment variable specifies which FEC committees to monitor.

### Finding Committee IDs

Committee IDs start with "C" followed by 8 digits (e.g., `C00703975`). Find them on the [FEC website][fec-committees] by searching for a committee name.

### Local Development

Edit `apps/data-sync/local.settings.json`:

```json
{
  "Values": {
    "FEC_API_KEY": "your-fec-api-key",
    "FEC_COMMITTEE_IDS": "C00703975,C00618371"
  }
}
```

### Azure Portal Configuration

1. Navigate to **Azure Portal** > **Resource Groups** > `fec-data-sync-rg`
2. Select the **data-sync** Function App (e.g., `data-sync-dev`)
3. Go to **Settings** > **Environment variables** (or **Configuration** > **Application settings**)
4. Find or add `FEC_COMMITTEE_IDS`
5. Set the value to a comma-separated list of committee IDs:
   ```
   C00703975,C00618371,C00401224
   ```
6. Click **Apply** and confirm the restart

### Azure CLI Configuration

```bash
az functionapp config appsettings set \
  --name data-sync-dev \
  --resource-group fec-data-sync-rg \
  --settings "FEC_COMMITTEE_IDS=C00703975,C00618371"
```

### During Deployment

Pass committee IDs as a Bicep parameter:

```bash
az deployment group create \
  --resource-group fec-data-sync-rg \
  --template-file infra/main.bicep \
  --parameters fecCommitteeIds="C00703975,C00618371"
```

> ⚠️ **Note:** Large committees with many transactions may produce reports that exceed email size limits or AI processing capacity. If you experience issues, try reducing the number of committees.

---

## Report Type Filtering

The `FEC_REPORT_TYPES` environment variable filters which filings to sync.

### Default Configuration

By default, the application syncs quarterly reports:

```bash
FEC_REPORT_TYPES="Q1,Q2,Q3,YE"
```

### Custom Configuration

To sync different report types, set this variable in your local settings or Azure configuration:

```json
{
  "Values": {
    "FEC_REPORT_TYPES": "Q1,Q2,Q3,YE,12G,30G"
  }
}
```

> **Note:** Only supported form/report combinations will generate formatted CSV/XLSX files and AI analysis. Other filings will sync but won't be fully processed.

---

## FEC Form Types Reference

FEC forms determine the structure of financial reports. Each form type has different data fields and is used by different types of committees.

| Supported | Form | Committee Type |
|:---------:|------|----------------|
| ✅ | **F3** | House & Senate Candidate Committees |
| | F3P | Presidential Candidate Committees |
| | F3X | PACs, Super PACs, and Party Committees |
| | F3L | Bundled Contributions |
| | F4 | Convention Committees |
| | F5 | Independent Expenditures |
| | F6 | 48-Hour Notice of Contributions |
| | F7 | Communication Costs |
| | F9 | Electioneering Communications |
| | F13 | Inaugural Committee Donations |

---

## FEC Report Types Reference

Report types indicate the filing period.

### Quarterly Reports

| Supported | Code | Description | Coverage Period |
|:---------:|------|-------------|-----------------|
| ✅ | **Q1** | April Quarterly | January 1 - March 31 |
| ✅ | **Q2** | July Quarterly | April 1 - June 30 |
| ✅ | **Q3** | October Quarterly | July 1 - September 30 |
| ✅ | **YE** | Year-End | October 1 - December 31 |
| | Q2S | July Quarterly / Semi-Annual | April 1 - June 30 |
| | QYE | Quarterly Semi-Annual (Year-End) | July 1 - December 31 |

### Monthly Reports

| Supported | Code | Description |
|:---------:|------|-------------|
| | M2 | February Monthly |
| | M3 | March Monthly |
| | M4 | April Monthly |
| | M5 | May Monthly |
| | M6 | June Monthly |
| | M7 | July Monthly |
| | M8 | August Monthly |
| | M9 | September Monthly |
| | M10 | October Monthly |
| | M11 | November Monthly |
| | M12 | December Monthly |
| | MSA | Monthly Semi-Annual (Mid-Year) |

### Election Reports

| Supported | Code | Description |
|:---------:|------|-------------|
| | 12P | Pre-Primary (12 days before) |
| | 12G | Pre-General (12 days before) |
| | 30P | Post-Primary (30 days after) |
| | 30G | Post-General (30 days after) |
| | 30R | Post-Runoff (30 days after) |
| | 30S | Post-Special (30 days after) |

### Other Reports

| Supported | Code | Description |
|:---------:|------|-------------|
| | 48 | 48-Hour Report of Independent Expenditures |
| | TER | Termination Report |

---

<!-- Reference Links -->
[fec-committees]: https://www.fec.gov/data/committees/

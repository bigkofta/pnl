# PNL Calendar Data Pipeline

## Overview
This document explains the data transformation pipeline for the SteveSystem PNL Calendar.

## Data Architecture

### Storage Layer
- **Technology**: Browser localStorage
- **Key**: `stevesystem_pnl_data`
- **Format**: JSON object with date keys

```javascript
{
  "2025-10-15": {
    "pnl": 250.50,
    "trades": 3,
    "notes": "Great trading day. Followed system rules."
  }
}
```

## Data Transformation Pipeline

### 1. Input Sources

#### Manual Entry
- Click calendar day → Modal opens
- Enter: PNL amount, trade count, notes
- Save → Data persists to localStorage

#### JSON Import (Bet Slips)
- Click "Import Bet Slips" button
- Paste JSON array of bet slips
- System transforms to daily aggregated format

### 2. Bet Slip Format

```json
[
  {
    "date": "YYYY-MM-DD",
    "match": "Team A vs Team B",
    "bet": "Bet description",
    "odds": 2.10,
    "stake": 100,
    "result": "won|lost",
    "pnl": 110,
    "notes": "Optional notes"
  }
]
```

### 3. Data Transformation Logic

#### Aggregation Rules
When importing multiple bet slips for the same day:
1. **PNL Aggregation**: Sum all PNL values
2. **Trade Count**: Increment by 1 per bet slip
3. **Notes Compilation**: Append bet details to notes field

Example transformation:
```javascript
// Input: 2 bet slips for 2025-10-15
[
  { date: "2025-10-15", pnl: 110, ... },
  { date: "2025-10-15", pnl: -150, ... }
]

// Output: Single day entry
{
  "2025-10-15": {
    "pnl": -40,      // 110 + (-150)
    "trades": 2,     // 2 slips
    "notes": "..."   // Combined details
  }
}
```

### 4. Statistics Calculation

The system calculates monthly statistics in real-time:

#### Win/Loss Logic
```javascript
// Only count days with actual trading activity
if (trades > 0 || pnl !== 0) {
  tradingDays++;
  
  if (pnl > 0) {
    wins++;
    winningDaysTotal += pnl;
  }
  
  if (pnl < 0) {
    losses++;
  }
}
```

#### Calculated Metrics
- **Month Total**: Sum of all daily PNL
- **Win Rate**: `(wins / tradingDays) * 100`
- **Average Win**: `winningDaysTotal / wins`
- **Best Day**: Maximum positive PNL in month
- **Trading Days**: Days with trades > 0 or pnl ≠ 0

## Data Flow Diagram

```
┌─────────────────┐
│   Input Sources │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼──┐  ┌──▼────┐
│Manual│  │ JSON  │
│Entry │  │Import │
└───┬──┘  └──┬────┘
    │        │
    │   ┌────▼─────────┐
    │   │ Transform &  │
    │   │  Aggregate   │
    │   └────┬─────────┘
    │        │
    └────┬───┘
         │
    ┌────▼─────────┐
    │ PNLManager   │
    │ (localStorage)│
    └────┬─────────┘
         │
    ┌────▼─────────┐
    │ Calendar     │
    │ Renderer     │
    └────┬─────────┘
         │
    ┌────▼─────────┐
    │ Stats        │
    │ Calculator   │
    └──────────────┘
```

## API Functions

### PNLManager Object
```javascript
PNLManager = {
  storageKey: 'stevesystem_pnl_data',
  
  // Load all data from localStorage
  loadData() -> Object
  
  // Save all data to localStorage
  saveData(data: Object) -> void
  
  // Get specific day data
  getDay(year, month, day) -> {pnl, trades, notes}
  
  // Set specific day data
  setDay(year, month, day, dayData) -> void
}
```

### Import/Export Functions
```javascript
// Import bet slips from JSON
importBetSlips() -> void

// Export all data as JSON file
exportData() -> void
```

## Future Enhancements

### Planned Features
1. **Automated API Integration**
   - Connect to betting platforms API
   - Auto-fetch bet history
   - Real-time sync

2. **Advanced Analytics**
   - Sport-wise breakdown
   - Bet type performance
   - Time-based patterns

3. **Cloud Sync**
   - Multi-device support
   - Backup to cloud storage
   - Collaborative features

4. **CSV Import/Export**
   - Excel compatibility
   - Bulk data migration

## Data Validation

### Import Validation Rules
1. **Required Fields**:
   - `date`: Must be valid YYYY-MM-DD format
   - `pnl`: Must be numeric value

2. **Optional Fields**:
   - All other fields enhance notes but aren't required

3. **Error Handling**:
   - Invalid JSON → Show error message
   - Missing required fields → Skip entry, show count
   - Invalid date format → Skip entry

## Testing

### Test Scenarios
1. **Empty State**: Calendar shows "No trades yet"
2. **Single Trade**: Stats calculate correctly
3. **Multiple Trades Same Day**: Proper aggregation
4. **Import Bet Slips**: Correct transformation
5. **Month Navigation**: Data persists
6. **Page Refresh**: Data remains in localStorage

## Performance Considerations

- **localStorage Limit**: ~5-10MB browser dependent
- **Data Retention**: Indefinite (until browser cache cleared)
- **Calculation Speed**: O(n) where n = days in month
- **Recommended**: Export data monthly as backup

## Security

- Data stored locally in browser
- No server transmission
- User owns their data
- Export for personal backup


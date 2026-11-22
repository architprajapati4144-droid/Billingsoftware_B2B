# BillCraft — Freelance & B2B Invoicing Desktop App

A native Windows desktop billing & invoicing application built with **Python 3.13**, **CustomTkinter**, **SQLite**, and **ReportLab**.

## Features
- **Itemized Invoice Builder**: Auto-incrementing invoice numbers (`INV-YYYY-XXXX`), dynamic line items (HSN/SAC codes, quantity, units, rate, per-item tax %), discounts (% or flat), extra charges, and live totals.
- **Tax & Multi-Currency Support**: Supports Standard Tax/VAT, Indian GST (**CGST + SGST** and **IGST**), or Tax-Exempt export invoices across `INR (₹)`, `USD ($)`, `EUR (€)`, `GBP (£)`, `CAD`, `AUD`, `AED`, and `SGD`.
- **Print & Crisp Vector PDF Export**: Generates clean, branded A4 PDF invoices (with optional business logo, accent color, payment instructions, payment history, and status badges) plus a 1-click **Print Invoice** flow that opens the Windows print dialog cleanly.
- **Client Directory**: Store client contacts, billing addresses, Tax ID / GSTIN, default payment terms, and track per-client billed and pending totals.
- **Due Dates & Payment Tracking**: Record full or partial payments (NEFT/IMPS, UPI, Card, Wire, Cash, etc.), view payment receipts, and automatically flag **Overdue** invoices.
- **Data Safety**: Local SQLite database (`data/billing.db`) with one-click CSV ledger export and database backup/restore.

## How to Launch
- **Double-click** `run.bat` in `D:\billing-software\`, or
- Run from terminal:
  ```powershell
  D:\billing-software\.venv\Scripts\python.exe D:\billing-software\main.py
  ```

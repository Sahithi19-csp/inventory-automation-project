# Inventory Automation Project

## Description
This project automates the inventory data cleaning and alert generation for low stock items.

## Setup
1. Clone the repo
2. Run `pip install -r requirements.txt`
3. Generate data: `python generate_fake_inventory.py`
4. Run automation: `python main.py`

## Data Assumptions
- Duplicates may exist (deduplicated by SKU)
- Negative quantities are clipped to 0
- ReorderQty is calculated as `max(0, ReorderPoint - OnHandQty)`

# Livestock Health & Tracking System

PROG211 Object-Oriented Programming 1 – Agriculture domain.

Tracks animals on a farm: health status and vaccinations.

## How to run
```
python livestock_tracker.py
```
Requires Python 3.8+ and no extra libraries.

## OOP concepts used
| Requirement | Where |
|---|---|
| Two classes with attributes and methods | `Animal`, `Farm` |
| Object creation and interaction | `main()` creates animals and adds them to a farm |
| One data structure | Dictionary `Farm.animals` (ID -> Animal) |
| Add/display functions | `add_record()`, `display_records()` |
| Instance methods | `update_record()`, `add_vaccination()`, `display_info()` |
| Class methods | `get_total_animals()`, `from_string()` |
| Static method | `is_valid_id()` |
| Tuples (bonus) | `VALID_STATUSES` and `(vaccine, date)` records |

## DPG standards alignment
- **Open source:** hosted publicly on GitHub.
- **Inclusive and accessible:** plain-text interface, simple English, runs on low-spec computers with no internet.
- **Privacy-respecting:** stores only animal data (ID, species, age, health); no farmer names, phone numbers or exact locations.
- **Modular and reusable:** `Animal` and `Farm` are independent classes that can be reused for other livestock or imported into other programs.

## Example output
```
Adding animals:
  Added A001 (Cow).
  Added A002 (Goat).
  Added A003 (Sheep).
  Record A001 already exists.

Valid ID check (static method):
  A010 -> True
  X99  -> False

Interaction between objects:
  A002 status updated to 'Sick'.
  A002 status updated to 'Under Treatment'.
  Invalid status. Choose from: ('Healthy', 'Sick', 'Under Treatment', 'Recovered')

All animals on Green Valley Farm:
  ID: A001 | Species: Cow | Age: 24 months | Status: Healthy
      Vaccinated: Anthrax on 2026-09-01
  ID: A002 | Species: Goat | Age: 10 months | Status: Under Treatment
  ID: A003 | Species: Sheep | Age: 14 months | Status: Healthy

Farm report: Green Valley Farm (Bo District)
  Healthy: 2
  Sick: 0
  Under Treatment: 1
  Recovered: 0

Total animals created: 3
```﻿
 

"""Generate a fictitious ticket dataset for the Operations Intelligence project.

Run: python data/generate_tickets.py
Output: data/tickets.csv (3,000 rows, reproducible with a fixed seed)
"""
import csv
import datetime as dt
import random
from pathlib import Path

random.seed(42)

EQUIPMENT = {
    "CNC Laser 6040": ["Laser does not fire", "Misaligned cut", "Chiller overheating"],
    "Fiber Laser 30W": ["Weak marking", "Software does not detect machine"],
    "Eco-Solvent Printer XP600": ["Nozzle failure", "Banding on print", "Print head replacement"],
    "Vinyl Cutter 120": ["Misaligned cut", "Camera does not read marks"],
    "DTF Printer 60": ["Powder does not fix", "Agitator motor replacement"],
    "3D Printer": ["Clogged nozzle", "First layer does not stick"],
    "Ice Cream Machine 38L": ["Does not freeze", "Reservoir leak"],
}
CATEGORIES = (["TECHNICIAL_SUPPORT"] * 40 + ["GUARANTEE"] * 25 + ["TECHNICAL_VISIT"] * 12
              + ["MAINTENANCE"] * 8 + ["INSTALLATION"] * 8 + ["CONFIGURATION"] * 3
              + ["ASSET_REMOVAL"] * 2 + ["TECHNICIAL_REPORT"] * 2)
PRIORITIES = ["MEDIA"] * 40 + ["ALTA"] * 30 + ["URGENTE"] * 20 + ["BAIXA"] * 10
OPEN_STATUSES = ["OPENED", "STARTED", "SCHEDULE", "PENDING", "AWAITING_TECHNICIAN_LINK",
                 "PART_PREPARATION", "PART_SHIPPED"]
TECHNICIANS = ["Tech A", "Tech B", "Tech C", "Tech D", "Tech E", ""]
ISO = "%Y-%m-%dT%H:%M:%SZ"


def make_ticket(i: int, start: dt.datetime, end: dt.datetime, n: int) -> list:
    created = start + (end - start) * (i / n) + dt.timedelta(minutes=random.randint(0, 300))
    equipment = random.choice(list(EQUIPMENT))
    age_days = (end - created).days
    if age_days > 20:
        status = random.choices(["CONCLUDED", "FINISHED", "CANCELLED", "NOT_SOLVED"], [70, 10, 15, 5])[0]
    else:
        status = random.choice(OPEN_STATUSES + ["CONCLUDED"])
    closed = ""  # empty string on purpose (not NULL)
    if status in ("CONCLUDED", "FINISHED"):
        closed = (created + dt.timedelta(hours=random.randint(2, 24 * 15))).strftime(ISO)
    category = random.choice(CATEGORIES)
    root_cause = random.choice(["FACTORY_DEFECT", "NATURAL_WEAR", "OPERATIONAL_ERROR"]) if category == "GUARANTEE" else ""
    return [f"{created:%Y-%m}-{20000 + i}", random.choice(EQUIPMENT[equipment]), category, status,
            random.choice(PRIORITIES), created.strftime(ISO), closed, equipment,
            random.choice(TECHNICIANS), root_cause]


def main() -> None:
    n = 3000
    start, end = dt.datetime(2026, 1, 5, 8), dt.datetime(2026, 11, 10, 18)
    out = Path(__file__).parent / "tickets.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["code", "title", "category", "status", "priority", "created_at",
                         "concluded_date", "equipamento", "tecnico", "root_cause"])
        writer.writerows(make_ticket(i, start, end, n) for i in range(n))
    print(f"Wrote {n} tickets to {out}")


if __name__ == "__main__":
    main()

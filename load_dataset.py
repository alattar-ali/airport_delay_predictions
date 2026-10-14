"""Load the flight dataset, keeping only flights that depart Denver (DEN)."""

from pathlib import Path

import pandas as pd


DATASET_PATH = Path(__file__).resolve().parent / (
    "On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_2026_7.csv"
)


def load_dataset(path: str | Path = DATASET_PATH) -> pd.DataFrame:
    """Read the flight CSV and return only flights whose origin is Denver."""
    flights = pd.read_csv(path)
    if "Origin" not in flights.columns:
        raise ValueError("Flight dataset is missing the 'Origin' column")

    return flights.loc[flights["Origin"].eq("DEN")].copy()


def main() -> None:
    """Keep only Denver departures in the source CSV, replacing it in place."""
    flights = load_dataset()
    flights.to_csv(DATASET_PATH, index=False)
    print(f"Saved {len(flights):,} Denver departures to {DATASET_PATH.name}")


if __name__ == "__main__":
    main()

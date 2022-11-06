import csv
from collections import defaultdict
from datetime import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent  # BASE_DIR requires for pytest
statuses_counts = defaultdict(int)


class PepParsePipeline:
    def open_spider(self, spider):
        # Required for pytest. I don't know what to write in it.
        ...

    def process_item(self, item, spider):
        pep_status = item.get('status')
        statuses_counts[pep_status] += 1
        return item

    def close_spider(self, spider):
        FILE_DATETIME = f'{dt.utcnow():%Y-%m-%d_%H-%M-%S%z}'
        # BASE_DIR in FILENAME is needed for pytest,
        # everything works exactly the same without it
        FILENAME = BASE_DIR / f'results/status_summary_{FILE_DATETIME}.csv'
        with open(FILENAME, 'w', newline='') as csvfile:
            FIELDNAMES = ('Status', 'Count')
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)

            writer.writeheader()
            for status, count in statuses_counts.items():
                writer.writerow({'Status': status, 'Count': count})
            writer.writerow(
                {
                    'Status': 'Total',
                    'Count': sum(statuses_counts.values())
                }
            )

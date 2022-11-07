import csv
from collections import defaultdict
from datetime import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
statuses_counts = defaultdict(int)


class PepParsePipeline:
    def open_spider(self, spider):
        statuses_counts.clear()

    def process_item(self, item, spider):
        pep_status = item.get('status')
        statuses_counts[pep_status] += 1
        return item

    def close_spider(self, spider):
        FILE_DATETIME = f'{dt.utcnow():%Y-%m-%d_%H-%M-%S%z}'
        # Если вынести следующие 2 строки из класса, то не проходит тесты.
        # Не понимаю как сделать по другому. Хотел положить обе строки наверх,
        # под BASE_DIR, но так не работает.
        # Я так понял нужно упоминание BASE_DIR внутри класса,
        # что бы monkeypatch мог её заменить.
        RESULTS_DIR = BASE_DIR / 'results'
        RESULTS_DIR.mkdir(exist_ok=True)

        FILENAME = RESULTS_DIR / f'status_summary_{FILE_DATETIME}.csv'
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

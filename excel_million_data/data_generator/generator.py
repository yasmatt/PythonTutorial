import csv
import random
from faker import Faker


def generate_romdom_dataset(filename_to: str, num_rows=100):
    """
    create dataset
    list of columns is here
        company
        personal_name
        address
        phone_number
        date
        sales
    :return:
    """
    fake = Faker('ja_JP')
    dataset = []
    columns = (
        '企業名',
        '担当名',
        '住所',
        '電話番号',
        '日付',
        '売上',
    )
    dataset.append(columns)
    for i in range(num_rows):
        dataset.append([
            fake.company(),
            fake.name(),
            fake.address(),
            fake.phone_number(),
            fake.date_between('-10y'),
            int(random.uniform(1000,10000000))
        ])

    with open(filename_to, 'w') as f:
        w = csv.writer(f)
        w.writerows(dataset)

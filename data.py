from faker import Faker
import random

def generate_fake_dataset(num_records=10):
    fake = Faker()
    data = []

    for _ in range(num_records):
        record = {
            'name': fake.name(),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
            'garbage_data': random.choice([fake.text(), None]),
            'empty_field_1': '',
            'empty_field_2': '',
            'random_place_name': random.choice([fake.city(), None]),  
           
        }
        data.append(record)

    return data

if __name__ == "__main__":
    num_records = 100  
    fake_dataset = generate_fake_dataset(num_records)
    for idx, record in enumerate(fake_dataset, start=1):
        print(f"{record}")
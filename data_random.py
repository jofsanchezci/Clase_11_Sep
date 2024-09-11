from faker  import Faker
fake = Faker('es_CO')
data = []

for _ in range(1):
    data.append((fake.name(), fake.company(), fake.first_name(),
                 fake.email(), fake.phone_number(), fake.mac_address()))


print(data)


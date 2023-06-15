"""
desc Arquivo responsável por armazenar e criar  as funções Crud da aplicação
"""
from store.models import Store


class StoreApp:
    @staticmethod
    def create_json_store(name, cnpj, email, date_of_fundation,
                          address, city, state, country, image=None):
        data = {
            'name': name,
            'cnpj': cnpj,
            'email': email,
            'image': image,
            'dateOfundation': date_of_fundation,
            'address': address,
            'city': city,
            'state': state,
            'country': country
        }

        return data

    def get_store_info_and_return_in_json(self):
        queryset = Store.objects.all()
        data = []

        for store in queryset:
            data_json = self.create_json_store(
                name=store.name, cnpj=store.cnpj, email=store.email,
                date_of_fundation=store.date_of_fundation.strftime('%Y-%m-%d'),
                address=store.address, city=store.city, state=store.state,
                country=store.country, image=store.image.url if store.image else 'noting')

            data.append(data_json)

        return data

    @staticmethod
    def set_info_store(data):
        try:
            store_list = []
            if isinstance(data, list):
                for item in data:
                    store = Store(**item)
                    store_list.append(store)
            else:
                store = Store(**data)
                store_list.append(store)
            Store.objects.bulk_create(store_list)
            return True
        except Exception as e:
            raise Exception('Failed to create store: {}'.format(str(e)))


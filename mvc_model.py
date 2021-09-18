class Model:

    def __init__(self):
        self.database = 'database.txt'
        self.last_info = self.get_last_used_info()
        self.website_temp = ''
        self.username_temp = self.last_info['username']
        self.password_temp = ''

    def format_data(self):
        new_data = f'{self.website_temp.strip()} | {self.username_temp.strip()} | {self.password_temp.strip()}'
        return new_data

    def get_last_used_info(self):
        try:
            with open(self.database, 'r') as data:
                for line in data:
                    pass
                try:
                    if line != None:
                        values = line.split(' | ')
                        keys = ['website', 'username', 'password']
                        return dict(zip(keys, values))

                # if file is empty don't fetch data from file, instead fetch  a sample
                except Exception as err:
                    sample_data = {
                        'website': '',
                        'username': 'johndoe@google.com',
                        'password': '',
                    }
                    return sample_data

        # if file do not exist create a new one and fetch a sample
        except:
            self.reset_database()
            sample_data = {
                'website': '',
                'username': 'johndoe@google.com',
                'password': '',
            }
            return sample_data

    def update_database(self):
        with open(self.database, 'a') as file:
            new_data = self.format_data()
            file.write(f"{new_data}\n")

    def reset_database(self):
        with open(self.database, 'w') as file:
            file.truncate(0)

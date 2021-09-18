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
        with open(self.database, 'r') as data:
            for line in data:
                pass
            try:
                if line != None:
                    values = line.split(' | ')
                    keys = ['website', 'username', 'password']
                    return dict(zip(keys, values))

            # if file is empty don't fetch data from file, instead create a sample
            except Exception as err:
                sample_data = {
                    'website': '',
                    'username': 'johndoe@google.com',
                    'password': '',
                }
                return sample_data

    def update_database(self):
        with open(self.database, 'a') as file:
            new_data = self.format_data()
            print(new_data)
            file.write(f"{new_data}\n")

    def reset_database(self):
        with open(self.database, 'w') as file:
            file.truncate(0)


if __name__ == '__main__':
    temp = Model()
    print(temp.last_info)
    temp.update_database()

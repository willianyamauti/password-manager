import json


class Model:
    sample_data = {
        "": {
            "username": "johndoe@google.com",
            "password": "",
        }
    }

    def __init__(self):
        self.database = 'database.json'
        self.website_temp = ''
        self.username_temp = ''
        self.password_temp = ''
        self.temp_data = self.get_database()

    def format_data(self):
        new_data = {
            self.website_temp: {
                "username": self.username_temp,
                "password": self.password_temp,
            }
        }
        return new_data

    def get_database(self):
        try:
            # try to retrieve data from file
            try:
                with open(self.database, 'r') as file:
                    data = list(json.load(file).items())
                    self.username_temp = data[-1][1].get('username')
                    return dict(data)

            # if the database is empty
            except ValueError as err:
                self.username_temp = self.sample_data[""]["username"]
                return 'NO DATA FOUND'

        # if file do not exist create a new one and fetch a sample
        except FileNotFoundError:
            self.reset_database()
            self.username_temp = self.sample_data[""]["username"]


    def update_database(self):
        new_data = self.format_data()
        # try to read data from file
        try:
            with open(self.database, 'r') as file:
                data = json.load(file)

        # if file is empty, insert the data
        except ValueError as err:
            with open(self.database, 'a') as file:
                json.dump(new_data, file, indent=4)

        # if theres no exception run this block
        else:
            # Updating old data with new data
            data.update(new_data)
            with open(self.database, "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)

    def reset_database(self):
        with open(self.database, 'w') as file:
            file.truncate(0)

#
# if __name__ == '__main__':
#     m = Model()
#     print(m.last_info)

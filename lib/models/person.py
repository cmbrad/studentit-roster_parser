class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return "First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}".format(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email
        )

    def __repr__(self):
        return "Person(first_name={first_name}, last_name={last_name}, email={email}".format(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email
        )

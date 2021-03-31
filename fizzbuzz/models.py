from fizzbuzz import db


class Variables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fizz_count = db.Column(db.Integer)
    buzz_count = db.Column(db.Integer)
    fizz_name = db.Column(db.String())
    buzz_name = db.Column(db.String())

    def __repr__(self):
        return (f'Fizz count: {self.fizz_count}, '
                f'Buzz count: {self.buzz_count}, '
                f'Fizz name: {self.fizz_name}, '
                f'Buzz name: {self.buzz_name}')

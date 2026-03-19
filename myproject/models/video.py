from ..extensions import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(50))

    def __repr__(self):
        return f'<Video "{self.url}">'
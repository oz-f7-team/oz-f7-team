from ..models import db, Image

def create_image(url):
    image = Image(url=url)
    db.session.add(image)
    db.session.commit()
    return image

def get_images():
    return Image.query.all()

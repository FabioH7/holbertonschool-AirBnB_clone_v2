from models import storage
from models.state import State
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.city import City
from models.amenity import Amenity


db = storage.all().values()

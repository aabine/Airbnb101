import uuid
from datetime import datetime

class BaseModel:
    """A base class for all models in our hbnb clone."""
    
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
    
    def __init__(self, *args, **kwargs):
        """Initialize a new model."""
        current_time = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = current_time.isoformat()
        self.updated_at = current_time.isoformat()
        if len(kwargs) != 0:
            # Update instance variables with key-value pairs from kwargs
            self.__dict__.update({
                key: datetime.strptime(value, self.DATE_FORMAT)
                if key in ["created_at", "updated_at"] else value
                for key, value in kwargs.items() if key != "__class__"
            })
        
        self.save()
    
    
    def __str__(self):
        """Return string representation of BaseModel."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Updates updated_at with current time when instance is changed."""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Return dictionary representation of BaseModel."""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

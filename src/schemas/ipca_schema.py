from pydantic import BaseModel, Field
from datetime import datetime

class IPCASchema(BaseModel):
   periodo: datetime
   valor: float

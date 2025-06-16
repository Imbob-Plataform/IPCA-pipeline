from pydantic import BaseModel, Field
from datetime import datetime

class IPCASchema(BaseModel):
   data: datetime
   valor: float

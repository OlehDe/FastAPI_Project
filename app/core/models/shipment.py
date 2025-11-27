from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from .base import BaseModel

class Shipment(BaseModel):
    __tablename__ = "shipments"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    shipment_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    delivery_address: Mapped[str] = mapped_column(String(255))
    tracking_number: Mapped[str] = mapped_column(String(100))
    carrier: Mapped[str] = mapped_column(String(50))
    status: Mapped[str] = mapped_column(String(50))

    order = relationship("Order", back_populates="shipment")

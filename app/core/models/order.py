from sqlalchemy import Integer, DateTime, Float, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from .base import BaseModel

class Order(BaseModel):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    order_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    total_price: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(50))

    client = relationship("Client", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")
    shipment = relationship("Shipment", back_populates="order", uselist=False)

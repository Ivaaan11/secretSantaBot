from sqlalchemy import BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='postgresql+asyncpg://user:password@postgres:5432/db')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()
    wish: Mapped[str] = mapped_column()
    game_id: Mapped[str] = mapped_column()


class Game(Base):
    __tablename__ = 'games'

    id: Mapped[int] = mapped_column(primary_key=True)
    organizer_id = mapped_column(BigInteger)
    status: Mapped[str] = mapped_column()


class Pair(Base):
    __tablename__ = 'pairs'

    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int] = mapped_column()
    giver_id = mapped_column(BigInteger)
    receiver_id = mapped_column(BigInteger)


class Admin(Base):
    __tablename__ = 'admins'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)



async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

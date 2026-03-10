from typing import Annotated
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from fastapi import FastAPI,APIRouter,Depends
from sqlalchemy import select
app = FastAPI()
router_three = APIRouter(prefix="/database",tags=["database_all"])

engine = create_async_engine('sqlite+aiosqlite:///books.db')

new_session = async_sessionmaker(engine,expire_on_commit=False)
async def get_session():
    async with new_session() as session:
        yield session


SessionDep = Annotated[AsyncSession,Depends(get_session)]

class Base(DeclarativeBase):
    pass

class BooksModel(Base):
    __tablename__ = 'books'
    id : Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str]
    author : Mapped[str]

class BookIdModel(BaseModel):
    id : int
    title : str
    author : str

class BookTransModel(Base):
    __tablename__ = 'book_trans_models'
    id: Mapped[int] = mapped_column(primary_key=True)

@router_three.post('setup_database')
async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {'кошулду':True}

@router_three.post('book_add')
async def book_id(data:BookIdModel,session: SessionDep):
    new_book = BooksModel(
        title=data.title,
        author=data.author,
    )
    session.add(new_book)
    await session.commit()
    return {'китеп кошулду':True}

@router_three.get('/book.id')
async def get_book_id(session: SessionDep):
    query = select(BooksModel)
    result= await session.execute(query)
    get_book_id = result.scalars().all()
    return {"get_book_id": get_book_id,'Китеп алынды':True}

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# 데이터베이스 연결
engine = create_engine('sqlite:///user.db', echo=True)

# Base 클래스 정의
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f'<User(id={self.id}, name={self.name})>'

# DB 안에 테이블 생성
Base.metadata.create_all(bind=engine)

#세션 준비
SessionLocal = sessionmaker(bind=engine)

db = SessionLocal()

new_user = User(name='치훈')
db.add(new_user)
db.commit()
print("사용자 추가:", new_user)

# Select
user = db.query(User).all()
print("사용자", user)

# update
user = db.query(User).first()
if user:
    user.name = "건우"
    db.commit()
    print("사용자 변경:", user)

user = db.query(User).all()
print("사용자", user)

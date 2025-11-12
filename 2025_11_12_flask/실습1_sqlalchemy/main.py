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

### 단일 데이터 핸들링
def run_single():
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

    # delete
    user = db.query(User).first()
    if user:
        db.delete(user)
        db.commit()
        print("사용자 삭제~~~~")

    user = db.query(User).all()
    print("사용자", user)

db = SessionLocal()

#insert
users = [User(name="종찬"), User(name="동석"), User(name="건영")]
db.add_all(users)
db.commit()
print("여러 사용자 추가: ", users)

#select
### 전체 데이터 조회
users = db.query(User).order_by(User.id).all()
for user in users:
    print(user.name)

### 조건 검색
find_user = db.query(User).filter(User.name == "건영").first()
print("조건 조회 : ", find_user)

find_user = db.query(User).filter(User.name.like("%치훈%")).first()
print("조건 조회:", find_user)

### update
users = db.query(User).all()
for user in users:
    user.name = user.name + "_NEW"
    db.commit()

users = db.query(User).order_by(User.id).all()
for user in users:
    print(user.name)

### delete
users = db.query(User).delete()
db.commit()

if db.query(User).all():
    print("데이터가 아직 있습니다.")
else:
    print("데이터가 삭제 되었습니다.")

db.close()

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserModel:
    _data = []

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @staticmethod
    def get_hashed_password(password):
        print("=== DEBUG: get_hashed_password ===")
        print("값 repr :", repr(password))
        print("타입    :", type(password))
        try:
            print("문자열 길이:", len(password))
            print("바이트 길이:", len(password.encode("utf-8")))
        except Exception as e:
            print("len/encode 중 에러:", e)
        print("=================================")

        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def create(cls, username: str, password: str):
        """회원가입: 유저 생성 + _data에 저장"""
        # 1) 아이디 중복 체크
        if cls.get_by_username(username) is not None:
            raise ValueError("이미 존재하는 username 입니다.")

        # 2) 비밀번호 해시
        hashed = cls.get_hashed_password(password)

        # 3) 유저 인스턴스 생성
        user = cls(username=username, password=hashed)

        # 4) 가짜 DB에 저장
        cls._data.append(user)

        return user

    @classmethod
    def get_by_username(cls, username: str):
        """username으로 유저 찾기"""
        for user in cls._data:
            if user.username == username:
                return user
        return None

    @classmethod
    def authenticate(cls, username, password):
        for user in cls._data:
            if user.username == username and cls.verify_password(password, user.password):
                return user

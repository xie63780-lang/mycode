"""A small greeting program for the Git collaboration exercise."""


def greet(name: str = "朋友") -> str:
    return f"你好，{name}！"


if __name__ == "__main__":
    print(greet())

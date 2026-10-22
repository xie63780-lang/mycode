"""A small greeting program for the Git collaboration exercise."""


def greet(name: str = "朋友") -> str:
    cleaned_name = name.strip() or "朋友"
    return f"你好，{cleaned_name}！"


if __name__ == "__main__":
    print(greet())

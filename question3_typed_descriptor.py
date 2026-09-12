


class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.storage_name = None

    def __set_name__(self, owner, name):
        # Automatically create a private storage attribute.
        self.storage_name = "_" + name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self

        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"Expected {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )

        setattr(instance, self.storage_name, value)


class Student:
    age = Typed(int)
    name = Typed(str)

    def __init__(self, age, name):
        self.age = age
        self.name = name


if __name__ == "__main__":
    student = Student(20, "John")

    print("Student age:", student.age)
    print("Student name:", student.name)


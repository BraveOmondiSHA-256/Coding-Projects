from _pytest.fixtures import fixture
import os

# penguins bake cookies, penguins eagerly feasting together

filename = "answer.txt"

@fixture(scope="session", autouse=True)
def file():
    if os.path.exists(filename):
        os.remove(filename)
    f = open(filename, "x")
    yield f
    f.close()

# TODO
def cookies_together(file):
    file.write("cookies, ")
    yield
    file.write("together ")


# TODO
def bake(file):
    file.write("bake ")


#TODO
def eagerly_feasting(file):
    file.write("eagerly ")
    yield
    file.write("feasting ")


# TODO
def penguins(file):
    file.write("penguins ")
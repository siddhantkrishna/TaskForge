from setuptools import setup, find_packages

setup(
    name="taskforge",
    version="0.2.0",
    packages=find_packages(),
    py_modules=["main", "cli", "storage", "task", "exceptions", "utils"],
    entry_points={
        "console_scripts": [
            "taskforge=main:main",
        ],
    },
)

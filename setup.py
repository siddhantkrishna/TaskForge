from setuptools import setup, find_packages

setup(
    name="taskforge",
    version="0.1.0",
    packages=find_packages(),
    py_modules=["main", "cli", "storage", "task", "exceptions"],
    entry_points={
        "console_scripts": [
            "taskforge=main:main",
        ],
    },
)

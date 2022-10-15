from setuptools import setup
import py2exe

setup(
    name="app.py",
    version="1.0",
    description="Descarga capítulos desde la web de SX3",
    author="santimb96",
    author_email="santiagomartinezbota@gmail.com",
    url="https://github.com/santimb96/sx3_content_scrapping",
    scripts=["app.py"],
    console=["app.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)
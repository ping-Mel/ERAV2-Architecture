from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ERA_V2_Architecture",
    version="0.1.0",
    author="Xianping Wu",
    author_email="xianpingwu@hotmail.com",
    description="The ERA-V2 course delves deep into the realm of cutting-edge network architectures in the field of deep learning. Designed for seasoned practitioners and enthusiasts alike, this course offers a comprehensive exploration of Convolutional Neural Networks (CNNs), Deep Neural Networks (DNNs), and Transformers. Through a combination of theoretical lectures, practical implementations, and hands-on exercises, participants will gain a profound understanding of these advanced architectures, their underlying principles, and their applications across various domains.",
    long_description=long_description,
    long_description_content_type="text/markdown",    
    url="https://github.com/ping-Mel/ERAV2-Architecture.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
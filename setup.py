from setuptools import find_packages, setup

with open("./README.md", "r") as f:
    long_description = f.read()

with open("./requirements.txt", "r") as reqs:
    deps = reqs.read().splitlines()

with open("./VERSION.txt", "r") as ver:
    version = ver.read()

setup(
    name="localchatgpt",
    version=version,
    description="Local Chat Assistant powered by Ollama",
    packages=find_packages(),
    package_dir={'localchatgpt' : '.'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Concepts-in-tamil/localchatGPT",
    author="Viswa Kumar",
    author_email="kspviswaphd@gmail.com",
    license="MIT",
    scripts=['bin/localchatgpt', 'bin/localchatgpt_main.py', 'bin/localchatgpt_ollamaClient.py', 'bin/localchatgpt_prompt.py', 'bin/localchatgpt_settings.py', 'bin/localchatgpt_home.py', 'bin/localchatgpt_init.py'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires = deps,
    include_package_data=True,
    python_requires=">=3.11",
)   
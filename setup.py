from setuptools import setup, find_packages

setup(
    name="synthara",
    version="1.0.0",
    packages=find_packages(where="backend"),
    package_dir={"": "backend"},
    include_package_data=True,
    install_requires=open("backend/requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "synthara-train=scripts.train_model:main",
            "synthara-server=scripts.run_server:main",
        ],
    },
    author="Synthara Dev Team",
    description="Synthara OS – Autonomous LLM system for crypto + tech",
    license="MIT",
    keywords=["llm", "ai", "crypto", "fastapi", "transformers"],
    zip_safe=False,
)
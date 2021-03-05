import coiled

software_name = "blog-notebooks/energy-landscape"
coiled.create_software_environment(
    name=software_name,
    container="coiled/notebook:latest",
    conda={
        "channels": ["conda-forge"],
        "dependencies": [
            "python=3.8", 
            "coiled=0.0.37",
            "dask-ml",
            "dask>=2.23.0",
            "fastparquet",
            "matplotlib",
            "pandas>=1.1.0",
            "python-snappy",
            "s3fs",
            "scikit-learn",
            "xgboost>=1.3.0",
            "optuna<2.4.0",
      ]
    },
    pip=["dask-optuna", "fastdtw"],
)

coiled.create_job_configuration(
    name="blog-notebooks/energy-landscape",
    software=software_name,
    command=[
        "/bin/bash",
        "run.sh",
    ],
    files=["energy-landscape.ipynb", "workspace.json", "run.sh"],
    ports=[8888],
    description="Explore residential electricity usage and Dynamic Time Warping",
)

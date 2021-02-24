import coiled

software_name = "xgboost-on-coiled"
coiled.create_software_environment(
    name=software_name,
    container="coiled/notebook:latest",
    conda={
        "channels": ["conda-forge"],
        "dependencies": [
            "python=3.8", 
            "coiled=0.0.36",
            "dask",
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
            "numpy",
            "xgboost",
            "joblib",
      ]
    },
    pip=["dask-optuna"],
)

coiled.create_job_configuration(
    name="xgboost-on-coiled",
    software=software_name,
    command=[
        "/bin/bash",
        "run.sh",
    ],
    files=["xgboost-mortgage.ipynb", "workspace.json", "run.sh"],
    ports=[8888],
    description="Train XGBoost on a large dataset with Dask on Coiled",
)

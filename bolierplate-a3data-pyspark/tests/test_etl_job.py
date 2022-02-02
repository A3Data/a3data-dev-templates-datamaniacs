"""
Test the transform logics with sample of data
"""
from pyspark.sql import SparkSession

def test_compare_data(spark: SparkSession):
    """Test data transformer.
    Using small chunks of input data and expected output data, we
    test the transformation step to make sure it's working as
    expected.
    """
    input_data = spark.range(0,500)

    expected_data = spark.range(0,100)

    expected_cols = len(expected_data.columns)
    expected_rows = expected_data.count()

    cols = len(input_data.columns)
    rows = input_data.count()

    assert expected_cols == cols
    assert expected_rows == rows
    
    assert [
        col in expected_data.columns for col in input_data.columns
    ] == [
        True,
    ]

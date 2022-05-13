"""Sample target test for target-parquet."""

from samples.sample_target_parquet.parquet_target_sink import SampleParquetTargetSink
from singer_sdk import typing as th
from singer_sdk.target_base import Target


class SampleTargetParquet(Target):
    """Sample target for Parquet."""

    name = "sample-target-parquet"
    config_jsonschema = th.PropertiesList(
        th.Property("filepath", th.StringType),
        th.Property("file_naming_scheme", th.StringType),
    ).to_dict()
    default_sink_class = SampleParquetTargetSink

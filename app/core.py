from dataclasses import dataclass
from pyspark import SparkConf, SparkContext, rdd

from app.methods.pca import gramian_matrix

@dataclass
class SC:
    app_name: str
    local: bool = False

    @property
    def context(self) -> SparkContext:
        conf: SparkConf = SparkConf().setAppName(self.app_name)
        return SparkContext.getOrCreate(conf)


if __name__ == "__main__":
    app_sc: SC = SC('mxfs').context
    # TODO

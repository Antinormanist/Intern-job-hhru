from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, coalesce, array, lit, col, size, expr
from pyspark.sql.types import StructType, StructField, StringType, ArrayType

spark = SparkSession.builder.appName('My app').getOrCreate()

schema = StructType([
    StructField("product", StringType(), True),
    StructField("category", ArrayType(StringType()), True)
])

# Данные для дата фрейма
rows = [
    (None, ["plant"]),
    ('watermelon', ['food', 'plant', 'style', 'subscribe']),
    ('T-shirt', ['clothes']),
    ('Free VPN', None),
    ('RTX 4090', ['computer', 'game']),
    ('Pen', None),
    ('Jeans', ['clothes'])
]

dataframe1 = spark.createDataFrame(rows, schema)

dataframe1 = dataframe1.withColumn(
    'category',
    coalesce(col('category'), array(lit(None).cast('string')))
)

def get_pairs(dataframe):
    # Пары продукт - категория
    product_category_pairs = dataframe.withColumn('category', explode(col('category'))).select('product', 'category')
    
    products_without_category = dataframe.filter(size(expr("filter(category, x -> x is not NULL)")) == 0).select('product')
    
    return product_category_pairs, products_without_category

pairs_df, no_category_df = get_pairs(dataframe1)

print("Product-Category Pairs:")
pairs_df.show()

print("Products without Category:")
no_category_df.show()

spark.stop()
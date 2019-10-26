from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

KEYSPACE = "testkeysppace"
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.set_keyspace(KEYSPACE)

def create_posts_column_family():
    session.execute("""
        CREATE COLUMNFAMILY StackExchangePosts
            (
                Domain TEXT PRIMARY KEY
                ,TotalQuestions INT
                ,UnansweredQuestions INT
                ,TrendingTags TEXT
                ,AverageAnswersCount INT
            );
    """)

def insert_values_in_posts_column_family(domain, total_questions, unanswered_questions, trending_tags, average_answers_count):
    session.execute("""
        INSERT INTO StackExchangePosts 
        (Domain,TotalQuestions, UnansweredQuestions, TrendingTags, AverageAnswersCount)
        VALUES
        (%s, %s, %s, %s, %s);
    """, (domain, total_questions, unanswered_questions, trending_tags, average_answers_count))
from settings import PROJECT_ID
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


def get_db():
    """Get a local session."""
    return BigQuery().SessionLocal()


class BigQuery:
    """BigQuery database class."""

    instance = None

    class __Singleton:
        """Internal singleton."""

        def __init__(self):
            """Create the internal singleton."""
            sqlalchemy_database_uri = f'bigquery://{PROJECT_ID}'
            engine = create_engine(
                sqlalchemy_database_uri, pool_size=100, max_overflow=50
            )
            Base.metadata.create_all(bind=engine)
            self.SessionLocal = sessionmaker(
                autocommit=False, autoflush=False, bind=engine
            )

    def __init__(self):
        """Create the singleton values."""
        if not BigQuery.instance:
            BigQuery.instance = BigQuery.__Singleton()

    def __getattr__(self, name):
        """Pass all calls to internal singleton."""
        return getattr(self.instance, name)

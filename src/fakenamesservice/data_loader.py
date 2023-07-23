import pkg_resources
import itertools
import csv

from contextlib import closing

from fakenamesservice.database import SessionLocal, engine
from fakenamesservice.models import models

dataset = pkg_resources.resource_filename(__name__,
                                          'tests/integration/fakenames.csv')


def main():
    def lower_first(iterator):
        return itertools.chain([next(iterator).lower()], iterator)

    with SessionLocal() as session:
        models.Base.metadata.drop_all(bind=engine)
        models.Base.metadata.create_all(bind=engine)

        with closing(open(dataset, encoding='utf-8-sig')) as f:
            reader = csv.DictReader(lower_first(f))
            for row in reader:
                data = models.Fakenames(**row)

                session.add(data)
        session.commit()


if "__main__" == __name__:
    main()

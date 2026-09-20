from dash_erp.db.mongo import get_database
from bson import ObjectId

class SalesRepository:
    COLLECTION = "sales"

    def _collection(self):
        return get_database()[self.COLLECTION]

    def get_regions(self) -> list[str]:
        return self._collection().distinct("region")

    def find_all(self) -> list[dict]:
        return list(
            self._collection()
            .find()
            .sort("date", -1)
        )
    
    def find_sales(
        self,
        region: str | None = None,
        start_date=None,
        end_date=None,
    ) -> list[dict]:
        query = {}

        if region:
            query["region"] = region

        if start_date or end_date:
            query["date"] = {}

            if start_date:
                query["date"]["$gte"] = start_date

            if end_date:
                query["date"]["$lte"] = end_date

        return list(
            self._collection()
            .find(
                query,
                {
                    "_id": 0,
                    "date": 1,
                    "revenue": 1,
                },
            )
            .sort("date", 1)
        )

    def delete_many(self, ids: list[str]) -> int:
        object_ids = [
            ObjectId(id_)
            for id_ in ids
        ]

        result = self._collection().delete_many(
            {
                "_id": {
                    "$in": object_ids,
                }
            }
        )

        return result.deleted_count

    def create(self, sale: dict) -> str:
        result = self._collection().insert_one(sale)

        return str(result.inserted_id)

    def update(self, sale_id: str, sale: dict) -> bool:
        result = self._collection().update_one(
            {
                "_id": ObjectId(sale_id),
            },
            {
                "$set": sale,
            },
        )

        return result.modified_count > 0
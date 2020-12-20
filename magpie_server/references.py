from magpie.app import configuration
from magpie.plugins.dbadapter import ReferenceData, DBProvider

def list():
    db = DBProvider(configuration()).database
    ReferenceData.bind(db)
    query = ReferenceData.select().order_by(ReferenceData.collected_at)
    return {'items': [item for item in query]}

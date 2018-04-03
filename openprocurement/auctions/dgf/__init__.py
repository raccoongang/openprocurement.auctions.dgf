from openprocurement.auctions.dgf.models import DGFOtherAssets, DGFFinancialAssets, propertyLease


def includeme(config):
    config.add_auction_procurementMethodType(DGFOtherAssets)
    config.scan("openprocurement.auctions.dgf.views.other")

    config.add_auction_procurementMethodType(DGFFinancialAssets)
    config.scan("openprocurement.auctions.dgf.views.financial")

    config.add_auction_procurementMethodType(propertyLease)
    config.scan("openprocurement.auctions.dgf.views.property")
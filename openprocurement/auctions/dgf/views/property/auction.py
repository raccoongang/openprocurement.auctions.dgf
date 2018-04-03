# -*- coding: utf-8 -*-
from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.dgf.views.other.auction import (
    AuctionAuctionResource,
)


@opresource(name='propertyLease:Auction Auction',
            collection_path='/auctions/{auction_id}/auction',
            path='/auctions/{auction_id}/auction/{auction_lot_id}',
            auctionsprocurementMethodType="propertyLease",
            description="Property auction auction data")
class PropertyAuctionAuctionResource(AuctionAuctionResource):
    pass

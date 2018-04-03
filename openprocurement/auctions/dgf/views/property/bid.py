# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.dgf.views.other.bid import (
    AuctionBidResource,
)


@opresource(name='propertyLease:Auction Bids',
            collection_path='/auctions/{auction_id}/bids',
            path='/auctions/{auction_id}/bids/{bid_id}',
            auctionsprocurementMethodType="propertyLease",
            description="Property auction bids")
class PropertyAuctionBidResource(AuctionBidResource):
    pass

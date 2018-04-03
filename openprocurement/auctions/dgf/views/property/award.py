# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.dgf.views.other.award import (
    AuctionAwardResource,
)


@opresource(name='propertyLease:Auction Awards',
            collection_path='/auctions/{auction_id}/awards',
            path='/auctions/{auction_id}/awards/{award_id}',
            auctionsprocurementMethodType="propertyLease",
            description="Property auction awards")
class PropertyAuctionAwardResource(AuctionAwardResource):
    pass

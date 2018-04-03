# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.dgf.views.other.complaint import (
    AuctionComplaintResource,
)


@opresource(name='propertyLease:Auction Complaints',
            collection_path='/auctions/{auction_id}/complaints',
            path='/auctions/{auction_id}/complaints/{complaint_id}',
            auctionsprocurementMethodType="propertyLease",
            description="Property auction complaints")
class PropertyAuctionComplaintResource(AuctionComplaintResource):
    pass

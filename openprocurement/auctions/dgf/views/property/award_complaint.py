# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.dgf.views.other.award_complaint import (
    AuctionAwardComplaintResource,
)

@opresource(name='propertyLease:Auction Award Complaints',
            collection_path='/auctions/{auction_id}/awards/{award_id}/complaints',
            path='/auctions/{auction_id}/awards/{award_id}/complaints/{complaint_id}',
            auctionsprocurementMethodType="propertyLease",
            description="Property auction award complaints")
class PropertyAuctionAwardComplaintResource(AuctionAwardComplaintResource):
    pass
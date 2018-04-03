# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.dgf.views.other.cancellation import (
    AuctionCancellationResource,
)


@opresource(name='propertyLease:Auction Cancellations',
            collection_path='/auctions/{auction_id}/cancellations',
            path='/auctions/{auction_id}/cancellations/{cancellation_id}',
            auctionsprocurementMethodType="propertyLease",
            description="Property auction cancellations")
class PropertyAuctionCancellationResource(AuctionCancellationResource):
    pass

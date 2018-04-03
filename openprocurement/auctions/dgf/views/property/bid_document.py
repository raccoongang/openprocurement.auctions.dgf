# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.dgf.views.other.bid_document import (
    AuctionBidDocumentResource,
)


@opresource(name='propertyLease:Auction Bid Documents',
            collection_path='/auctions/{auction_id}/bids/{bid_id}/documents',
            path='/auctions/{auction_id}/bids/{bid_id}/documents/{document_id}',
            auctionsprocurementMethodType="propertyLease",
            description="Property auction bidder documents")
class PropertyAuctionBidDocumentResource(AuctionBidDocumentResource):
    pass

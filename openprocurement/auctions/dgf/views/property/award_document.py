# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.dgf.views.other.award_document import (
    AuctionAwardDocumentResource,
)


@opresource(name='propertyLease:Auction Award Documents',
            collection_path='/auctions/{auction_id}/awards/{award_id}/documents',
            path='/auctions/{auction_id}/awards/{award_id}/documents/{document_id}',
            auctionsprocurementMethodType="propertyLease",
            description="Property auction award documents")
class PropertyAuctionAwardDocumentResource(AuctionAwardDocumentResource):
    pass

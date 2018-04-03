# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.dgf.views.other.tender_document import (
    AuctionDocumentResource,
)


@opresource(name='propertyLease:Auction Documents',
            collection_path='/auctions/{auction_id}/documents',
            path='/auctions/{auction_id}/documents/{document_id}',
            auctionsprocurementMethodType="propertyLease",
            description="Property auction related binary files (PDFs, etc.)")
class PropertyAuctionDocumentResource(AuctionDocumentResource):
    pass

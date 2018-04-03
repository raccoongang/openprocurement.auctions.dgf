# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.dgf.views.other.cancellation_document import (
    AuctionCancellationDocumentResource,
)


@opresource(name='propertyLease:Auction Cancellation Documents',
            collection_path='/auctions/{auction_id}/cancellations/{cancellation_id}/documents',
            path='/auctions/{auction_id}/cancellations/{cancellation_id}/documents/{document_id}',
            auctionsprocurementMethodType="propertyLease",
            description="Property auction cancellation documents")
class PropertyAuctionCancellationDocumentResource(AuctionCancellationDocumentResource):
    pass

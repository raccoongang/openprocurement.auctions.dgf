# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.dgf.views.other.complaint_document import (
    AuctionComplaintDocumentResource,
)


@opresource(name='propertyLease:Auction Complaint Documents',
            collection_path='/auctions/{auction_id}/complaints/{complaint_id}/documents',
            path='/auctions/{auction_id}/complaints/{complaint_id}/documents/{document_id}',
            auctionsprocurementMethodType="propertyLease",
            description="Property auction complaint documents")
class PropertyComplaintDocumentResource(AuctionComplaintDocumentResource):
    pass

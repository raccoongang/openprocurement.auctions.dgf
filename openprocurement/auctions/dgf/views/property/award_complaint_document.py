# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.dgf.views.other.award_complaint_document import (
    AuctionAwardComplaintDocumentResource,
)


@opresource(name='propertyLease:Auction Award Complaint Documents',
            collection_path='/auctions/{auction_id}/awards/{award_id}/complaints/{complaint_id}/documents',
            path='/auctions/{auction_id}/awards/{award_id}/complaints/{complaint_id}/documents/{document_id}',
            auctionsprocurementMethodType="propertyLease",
            description="Property auction award complaint documents")
class PropertyAuctionAwardComplaintDocumentResource(AuctionAwardComplaintDocumentResource):
    pass
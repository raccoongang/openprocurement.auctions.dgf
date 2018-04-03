# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.dgf.views.other.question import (
    AuctionQuestionResource,
)


@opresource(name='propertyLease:Auction Questions',
            collection_path='/auctions/{auction_id}/questions',
            path='/auctions/{auction_id}/questions/{question_id}',
            auctionsprocurementMethodType="propertyLease",
            description="propertyLease:Auction questions")
class PropertyAuctionQuestionResource(AuctionQuestionResource):
    pass

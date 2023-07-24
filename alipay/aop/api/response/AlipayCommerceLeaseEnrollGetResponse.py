#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LeaseSkuOfferDTO import LeaseSkuOfferDTO


class AlipayCommerceLeaseEnrollGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLeaseEnrollGetResponse, self).__init__()
        self._item_id = None
        self._sku_offer_list = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def sku_offer_list(self):
        return self._sku_offer_list

    @sku_offer_list.setter
    def sku_offer_list(self, value):
        if isinstance(value, list):
            self._sku_offer_list = list()
            for i in value:
                if isinstance(i, LeaseSkuOfferDTO):
                    self._sku_offer_list.append(i)
                else:
                    self._sku_offer_list.append(LeaseSkuOfferDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLeaseEnrollGetResponse, self).parse_response_content(response_content)
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'sku_offer_list' in response:
            self.sku_offer_list = response['sku_offer_list']

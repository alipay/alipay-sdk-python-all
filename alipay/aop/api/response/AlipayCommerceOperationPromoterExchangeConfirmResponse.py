#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemExchangeInfo import ItemExchangeInfo


class AlipayCommerceOperationPromoterExchangeConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationPromoterExchangeConfirmResponse, self).__init__()
        self._item_exchange_info = None

    @property
    def item_exchange_info(self):
        return self._item_exchange_info

    @item_exchange_info.setter
    def item_exchange_info(self, value):
        if isinstance(value, ItemExchangeInfo):
            self._item_exchange_info = value
        else:
            self._item_exchange_info = ItemExchangeInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationPromoterExchangeConfirmResponse, self).parse_response_content(response_content)
        if 'item_exchange_info' in response:
            self.item_exchange_info = response['item_exchange_info']

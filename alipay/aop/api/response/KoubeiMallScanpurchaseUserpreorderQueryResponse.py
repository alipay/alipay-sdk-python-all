#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AdvanceOrder import AdvanceOrder


class KoubeiMallScanpurchaseUserpreorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMallScanpurchaseUserpreorderQueryResponse, self).__init__()
        self._advance_order = None
        self._buyer_user_id = None
        self._mall_has_card = None
        self._open_card = None
        self._open_card_url = None
        self._order_id = None
        self._status = None

    @property
    def advance_order(self):
        return self._advance_order

    @advance_order.setter
    def advance_order(self, value):
        if isinstance(value, AdvanceOrder):
            self._advance_order = value
        else:
            self._advance_order = AdvanceOrder.from_alipay_dict(value)
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def mall_has_card(self):
        return self._mall_has_card

    @mall_has_card.setter
    def mall_has_card(self, value):
        self._mall_has_card = value
    @property
    def open_card(self):
        return self._open_card

    @open_card.setter
    def open_card(self, value):
        self._open_card = value
    @property
    def open_card_url(self):
        return self._open_card_url

    @open_card_url.setter
    def open_card_url(self, value):
        self._open_card_url = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMallScanpurchaseUserpreorderQueryResponse, self).parse_response_content(response_content)
        if 'advance_order' in response:
            self.advance_order = response['advance_order']
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'mall_has_card' in response:
            self.mall_has_card = response['mall_has_card']
        if 'open_card' in response:
            self.open_card = response['open_card']
        if 'open_card_url' in response:
            self.open_card_url = response['open_card_url']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'status' in response:
            self.status = response['status']

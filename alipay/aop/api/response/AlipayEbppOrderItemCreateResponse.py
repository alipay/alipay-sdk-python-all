#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EbppOrderItem import EbppOrderItem


class AlipayEbppOrderItemCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppOrderItemCreateResponse, self).__init__()
        self._item = None
        self._qr_code = None

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        if isinstance(value, EbppOrderItem):
            self._item = value
        else:
            self._item = EbppOrderItem.from_alipay_dict(value)
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppOrderItemCreateResponse, self).parse_response_content(response_content)
        if 'item' in response:
            self.item = response['item']
        if 'qr_code' in response:
            self.qr_code = response['qr_code']

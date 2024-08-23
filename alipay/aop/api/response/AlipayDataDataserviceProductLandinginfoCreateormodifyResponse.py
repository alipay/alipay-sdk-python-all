#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceProductLandinginfoCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceProductLandinginfoCreateormodifyResponse, self).__init__()
        self._item_id = None
        self._out_item_id = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceProductLandinginfoCreateormodifyResponse, self).parse_response_content(response_content)
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'out_item_id' in response:
            self.out_item_id = response['out_item_id']

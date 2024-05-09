#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceProductAppModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceProductAppModifyResponse, self).__init__()
        self._out_id = None
        self._out_item_id = None
        self._suc = None

    @property
    def out_id(self):
        return self._out_id

    @out_id.setter
    def out_id(self, value):
        self._out_id = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def suc(self):
        return self._suc

    @suc.setter
    def suc(self, value):
        self._suc = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceProductAppModifyResponse, self).parse_response_content(response_content)
        if 'out_id' in response:
            self.out_id = response['out_id']
        if 'out_item_id' in response:
            self.out_item_id = response['out_item_id']
        if 'suc' in response:
            self.suc = response['suc']

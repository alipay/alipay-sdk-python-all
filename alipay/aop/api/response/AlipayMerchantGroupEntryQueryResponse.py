#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantGroupEntryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupEntryQueryResponse, self).__init__()
        self._biz_status = None
        self._open_id = None
        self._uid = None

    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupEntryQueryResponse, self).parse_response_content(response_content)
        if 'biz_status' in response:
            self.biz_status = response['biz_status']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'uid' in response:
            self.uid = response['uid']

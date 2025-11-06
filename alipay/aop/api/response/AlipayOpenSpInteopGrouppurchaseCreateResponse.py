#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpInteopGrouppurchaseCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpInteopGrouppurchaseCreateResponse, self).__init__()
        self._memos = None
        self._sub_order_no = None

    @property
    def memos(self):
        return self._memos

    @memos.setter
    def memos(self, value):
        if isinstance(value, list):
            self._memos = list()
            for i in value:
                self._memos.append(i)
    @property
    def sub_order_no(self):
        return self._sub_order_no

    @sub_order_no.setter
    def sub_order_no(self, value):
        self._sub_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpInteopGrouppurchaseCreateResponse, self).parse_response_content(response_content)
        if 'memos' in response:
            self.memos = response['memos']
        if 'sub_order_no' in response:
            self.sub_order_no = response['sub_order_no']

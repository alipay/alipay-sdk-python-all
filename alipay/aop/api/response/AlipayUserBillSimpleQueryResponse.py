#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserBillSimpleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserBillSimpleQueryResponse, self).__init__()
        self._amount = None
        self._biz_state = None
        self._gmt_biz_create = None
        self._in_out_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_state(self):
        return self._biz_state

    @biz_state.setter
    def biz_state(self, value):
        self._biz_state = value
    @property
    def gmt_biz_create(self):
        return self._gmt_biz_create

    @gmt_biz_create.setter
    def gmt_biz_create(self, value):
        self._gmt_biz_create = value
    @property
    def in_out_type(self):
        return self._in_out_type

    @in_out_type.setter
    def in_out_type(self, value):
        self._in_out_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserBillSimpleQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'biz_state' in response:
            self.biz_state = response['biz_state']
        if 'gmt_biz_create' in response:
            self.gmt_biz_create = response['gmt_biz_create']
        if 'in_out_type' in response:
            self.in_out_type = response['in_out_type']

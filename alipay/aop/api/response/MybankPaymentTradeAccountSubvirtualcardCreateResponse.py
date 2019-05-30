#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeAccountSubvirtualcardCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeAccountSubvirtualcardCreateResponse, self).__init__()
        self._prim_card_no = None
        self._sub_virtual_card_name = None
        self._sub_virtual_card_no = None

    @property
    def prim_card_no(self):
        return self._prim_card_no

    @prim_card_no.setter
    def prim_card_no(self, value):
        self._prim_card_no = value
    @property
    def sub_virtual_card_name(self):
        return self._sub_virtual_card_name

    @sub_virtual_card_name.setter
    def sub_virtual_card_name(self, value):
        self._sub_virtual_card_name = value
    @property
    def sub_virtual_card_no(self):
        return self._sub_virtual_card_no

    @sub_virtual_card_no.setter
    def sub_virtual_card_no(self, value):
        self._sub_virtual_card_no = value

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeAccountSubvirtualcardCreateResponse, self).parse_response_content(response_content)
        if 'prim_card_no' in response:
            self.prim_card_no = response['prim_card_no']
        if 'sub_virtual_card_name' in response:
            self.sub_virtual_card_name = response['sub_virtual_card_name']
        if 'sub_virtual_card_no' in response:
            self.sub_virtual_card_no = response['sub_virtual_card_no']

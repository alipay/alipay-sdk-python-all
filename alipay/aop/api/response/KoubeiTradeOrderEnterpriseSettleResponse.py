#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiTradeOrderEnterpriseSettleResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeOrderEnterpriseSettleResponse, self).__init__()
        self._biz_code = None
        self._order_no = None
        self._out_order_no = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeOrderEnterpriseSettleResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']

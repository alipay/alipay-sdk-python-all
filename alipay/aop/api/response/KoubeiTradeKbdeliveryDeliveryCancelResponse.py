#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiTradeKbdeliveryDeliveryCancelResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeKbdeliveryDeliveryCancelResponse, self).__init__()
        self._gmt_close = None
        self._logistics_order_no = None

    @property
    def gmt_close(self):
        return self._gmt_close

    @gmt_close.setter
    def gmt_close(self, value):
        self._gmt_close = value
    @property
    def logistics_order_no(self):
        return self._logistics_order_no

    @logistics_order_no.setter
    def logistics_order_no(self, value):
        self._logistics_order_no = value

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeKbdeliveryDeliveryCancelResponse, self).parse_response_content(response_content)
        if 'gmt_close' in response:
            self.gmt_close = response['gmt_close']
        if 'logistics_order_no' in response:
            self.logistics_order_no = response['logistics_order_no']

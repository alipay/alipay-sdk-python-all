#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceTradeInfo import InvoiceTradeInfo


class AlipayEbppInvoiceUserTradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceUserTradeQueryResponse, self).__init__()
        self._trade_info = None

    @property
    def trade_info(self):
        return self._trade_info

    @trade_info.setter
    def trade_info(self, value):
        if isinstance(value, InvoiceTradeInfo):
            self._trade_info = value
        else:
            self._trade_info = InvoiceTradeInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceUserTradeQueryResponse, self).parse_response_content(response_content)
        if 'trade_info' in response:
            self.trade_info = response['trade_info']

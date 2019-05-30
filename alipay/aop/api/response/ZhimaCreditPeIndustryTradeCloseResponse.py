#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeIndustryTradeCloseResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeIndustryTradeCloseResponse, self).__init__()
        self._out_fund_no = None
        self._zm_order_id = None

    @property
    def out_fund_no(self):
        return self._out_fund_no

    @out_fund_no.setter
    def out_fund_no(self, value):
        self._out_fund_no = value
    @property
    def zm_order_id(self):
        return self._zm_order_id

    @zm_order_id.setter
    def zm_order_id(self, value):
        self._zm_order_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeIndustryTradeCloseResponse, self).parse_response_content(response_content)
        if 'out_fund_no' in response:
            self.out_fund_no = response['out_fund_no']
        if 'zm_order_id' in response:
            self.zm_order_id = response['zm_order_id']

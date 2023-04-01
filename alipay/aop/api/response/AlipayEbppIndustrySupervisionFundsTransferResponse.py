#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySupervisionFundsTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionFundsTransferResponse, self).__init__()
        self._operate_no = None
        self._out_trade_no = None

    @property
    def operate_no(self):
        return self._operate_no

    @operate_no.setter
    def operate_no(self, value):
        self._operate_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySupervisionFundsTransferResponse, self).parse_response_content(response_content)
        if 'operate_no' in response:
            self.operate_no = response['operate_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceIncomeLeaseSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceIncomeLeaseSubmitResponse, self).__init__()
        self._biz_no = None
        self._trade_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceIncomeLeaseSubmitResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'trade_id' in response:
            self.trade_id = response['trade_id']

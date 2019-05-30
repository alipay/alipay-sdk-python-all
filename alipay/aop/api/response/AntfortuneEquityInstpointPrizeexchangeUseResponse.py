#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneEquityInstpointPrizeexchangeUseResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneEquityInstpointPrizeexchangeUseResponse, self).__init__()
        self._exchange_result = None
        self._exchange_trans_no = None

    @property
    def exchange_result(self):
        return self._exchange_result

    @exchange_result.setter
    def exchange_result(self, value):
        self._exchange_result = value
    @property
    def exchange_trans_no(self):
        return self._exchange_trans_no

    @exchange_trans_no.setter
    def exchange_trans_no(self, value):
        self._exchange_trans_no = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneEquityInstpointPrizeexchangeUseResponse, self).parse_response_content(response_content)
        if 'exchange_result' in response:
            self.exchange_result = response['exchange_result']
        if 'exchange_trans_no' in response:
            self.exchange_trans_no = response['exchange_trans_no']

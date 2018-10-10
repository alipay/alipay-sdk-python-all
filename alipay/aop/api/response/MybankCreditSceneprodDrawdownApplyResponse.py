#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodDrawdownApplyResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodDrawdownApplyResponse, self).__init__()
        self._drawdown_list = None
        self._retry = None
        self._trace_id = None

    @property
    def drawdown_list(self):
        return self._drawdown_list

    @drawdown_list.setter
    def drawdown_list(self, value):
        self._drawdown_list = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodDrawdownApplyResponse, self).parse_response_content(response_content)
        if 'drawdown_list' in response:
            self.drawdown_list = response['drawdown_list']
        if 'retry' in response:
            self.retry = response['retry']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SceneProdDeputyPaymentBillQuery import SceneProdDeputyPaymentBillQuery


class MybankCreditSceneprodRepayDeputyApplyResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodRepayDeputyApplyResponse, self).__init__()
        self._app_seqno = None
        self._bill_list = None
        self._drawdown_no = None
        self._trace_id = None

    @property
    def app_seqno(self):
        return self._app_seqno

    @app_seqno.setter
    def app_seqno(self, value):
        self._app_seqno = value
    @property
    def bill_list(self):
        return self._bill_list

    @bill_list.setter
    def bill_list(self, value):
        if isinstance(value, list):
            self._bill_list = list()
            for i in value:
                if isinstance(i, SceneProdDeputyPaymentBillQuery):
                    self._bill_list.append(i)
                else:
                    self._bill_list.append(SceneProdDeputyPaymentBillQuery.from_alipay_dict(i))
    @property
    def drawdown_no(self):
        return self._drawdown_no

    @drawdown_no.setter
    def drawdown_no(self, value):
        self._drawdown_no = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodRepayDeputyApplyResponse, self).parse_response_content(response_content)
        if 'app_seqno' in response:
            self.app_seqno = response['app_seqno']
        if 'bill_list' in response:
            self.bill_list = response['bill_list']
        if 'drawdown_no' in response:
            self.drawdown_no = response['drawdown_no']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']

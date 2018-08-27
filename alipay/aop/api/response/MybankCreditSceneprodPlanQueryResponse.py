#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodPlanQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodPlanQueryResponse, self).__init__()
        self._loan_plan = None
        self._result = None
        self._retry = None
        self._sign_time = None
        self._trace_id = None

    @property
    def loan_plan(self):
        return self._loan_plan

    @loan_plan.setter
    def loan_plan(self, value):
        self._loan_plan = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodPlanQueryResponse, self).parse_response_content(response_content)
        if 'loan_plan' in response:
            self.loan_plan = response['loan_plan']
        if 'result' in response:
            self.result = response['result']
        if 'retry' in response:
            self.retry = response['retry']
        if 'sign_time' in response:
            self.sign_time = response['sign_time']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']

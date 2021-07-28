#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodLprQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodLprQueryResponse, self).__init__()
        self._float_rate = None
        self._loan_dir = None
        self._loan_tenor = None
        self._lpr_basic_rate = None
        self._lpr_date_str = None
        self._retry = None
        self._trace_id = None

    @property
    def float_rate(self):
        return self._float_rate

    @float_rate.setter
    def float_rate(self, value):
        self._float_rate = value
    @property
    def loan_dir(self):
        return self._loan_dir

    @loan_dir.setter
    def loan_dir(self, value):
        self._loan_dir = value
    @property
    def loan_tenor(self):
        return self._loan_tenor

    @loan_tenor.setter
    def loan_tenor(self, value):
        self._loan_tenor = value
    @property
    def lpr_basic_rate(self):
        return self._lpr_basic_rate

    @lpr_basic_rate.setter
    def lpr_basic_rate(self, value):
        self._lpr_basic_rate = value
    @property
    def lpr_date_str(self):
        return self._lpr_date_str

    @lpr_date_str.setter
    def lpr_date_str(self, value):
        self._lpr_date_str = value
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
        response = super(MybankCreditSceneprodLprQueryResponse, self).parse_response_content(response_content)
        if 'float_rate' in response:
            self.float_rate = response['float_rate']
        if 'loan_dir' in response:
            self.loan_dir = response['loan_dir']
        if 'loan_tenor' in response:
            self.loan_tenor = response['loan_tenor']
        if 'lpr_basic_rate' in response:
            self.lpr_basic_rate = response['lpr_basic_rate']
        if 'lpr_date_str' in response:
            self.lpr_date_str = response['lpr_date_str']
        if 'retry' in response:
            self.retry = response['retry']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']

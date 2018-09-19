#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodLoanApplyResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodLoanApplyResponse, self).__init__()
        self._app_seqno = None
        self._need_auth = None
        self._out_order_no = None
        self._retry = None
        self._trace_id = None

    @property
    def app_seqno(self):
        return self._app_seqno

    @app_seqno.setter
    def app_seqno(self, value):
        self._app_seqno = value
    @property
    def need_auth(self):
        return self._need_auth

    @need_auth.setter
    def need_auth(self, value):
        self._need_auth = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
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
        response = super(MybankCreditSceneprodLoanApplyResponse, self).parse_response_content(response_content)
        if 'app_seqno' in response:
            self.app_seqno = response['app_seqno']
        if 'need_auth' in response:
            self.need_auth = response['need_auth']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'retry' in response:
            self.retry = response['retry']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']

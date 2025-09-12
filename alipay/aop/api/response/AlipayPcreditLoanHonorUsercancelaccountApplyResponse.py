#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanHonorUsercancelaccountApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorUsercancelaccountApplyResponse, self).__init__()
        self._logoff_err_desc = None
        self._logoff_result = None
        self._logoff_status = None
        self._out_order_no = None

    @property
    def logoff_err_desc(self):
        return self._logoff_err_desc

    @logoff_err_desc.setter
    def logoff_err_desc(self, value):
        self._logoff_err_desc = value
    @property
    def logoff_result(self):
        return self._logoff_result

    @logoff_result.setter
    def logoff_result(self, value):
        self._logoff_result = value
    @property
    def logoff_status(self):
        return self._logoff_status

    @logoff_status.setter
    def logoff_status(self, value):
        self._logoff_status = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorUsercancelaccountApplyResponse, self).parse_response_content(response_content)
        if 'logoff_err_desc' in response:
            self.logoff_err_desc = response['logoff_err_desc']
        if 'logoff_result' in response:
            self.logoff_result = response['logoff_result']
        if 'logoff_status' in response:
            self.logoff_status = response['logoff_status']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']

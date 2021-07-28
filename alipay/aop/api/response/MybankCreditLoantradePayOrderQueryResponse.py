#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreditPayOrderQueryVO import CreditPayOrderQueryVO


class MybankCreditLoantradePayOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradePayOrderQueryResponse, self).__init__()
        self._error_code = None
        self._query_result = None
        self._success = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def query_result(self):
        return self._query_result

    @query_result.setter
    def query_result(self, value):
        if isinstance(value, list):
            self._query_result = list()
            for i in value:
                if isinstance(i, CreditPayOrderQueryVO):
                    self._query_result.append(i)
                else:
                    self._query_result.append(CreditPayOrderQueryVO.from_alipay_dict(i))
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradePayOrderQueryResponse, self).parse_response_content(response_content)
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'query_result' in response:
            self.query_result = response['query_result']
        if 'success' in response:
            self.success = response['success']

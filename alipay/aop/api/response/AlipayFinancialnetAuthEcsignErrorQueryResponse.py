#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ErrorLog import ErrorLog


class AlipayFinancialnetAuthEcsignErrorQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthEcsignErrorQueryResponse, self).__init__()
        self._error_log_list = None

    @property
    def error_log_list(self):
        return self._error_log_list

    @error_log_list.setter
    def error_log_list(self, value):
        if isinstance(value, list):
            self._error_log_list = list()
            for i in value:
                if isinstance(i, ErrorLog):
                    self._error_log_list.append(i)
                else:
                    self._error_log_list.append(ErrorLog.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthEcsignErrorQueryResponse, self).parse_response_content(response_content)
        if 'error_log_list' in response:
            self.error_log_list = response['error_log_list']

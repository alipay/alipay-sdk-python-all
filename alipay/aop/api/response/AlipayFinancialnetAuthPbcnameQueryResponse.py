#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthPbcnameQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthPbcnameQueryResponse, self).__init__()
        self._pbc_query_result = None

    @property
    def pbc_query_result(self):
        return self._pbc_query_result

    @pbc_query_result.setter
    def pbc_query_result(self, value):
        self._pbc_query_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthPbcnameQueryResponse, self).parse_response_content(response_content)
        if 'pbc_query_result' in response:
            self.pbc_query_result = response['pbc_query_result']

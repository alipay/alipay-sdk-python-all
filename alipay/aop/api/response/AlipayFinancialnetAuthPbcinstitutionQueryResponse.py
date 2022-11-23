#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthPbcinstitutionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthPbcinstitutionQueryResponse, self).__init__()
        self._inst_query_result = None

    @property
    def inst_query_result(self):
        return self._inst_query_result

    @inst_query_result.setter
    def inst_query_result(self, value):
        self._inst_query_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthPbcinstitutionQueryResponse, self).parse_response_content(response_content)
        if 'inst_query_result' in response:
            self.inst_query_result = response['inst_query_result']

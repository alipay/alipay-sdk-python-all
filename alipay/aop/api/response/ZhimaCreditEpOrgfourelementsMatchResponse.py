#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpOrgfourelementsMatchResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpOrgfourelementsMatchResponse, self).__init__()
        self._match_code = None
        self._match_result_columns = None

    @property
    def match_code(self):
        return self._match_code

    @match_code.setter
    def match_code(self, value):
        self._match_code = value
    @property
    def match_result_columns(self):
        return self._match_result_columns

    @match_result_columns.setter
    def match_result_columns(self, value):
        if isinstance(value, list):
            self._match_result_columns = list()
            for i in value:
                self._match_result_columns.append(i)

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpOrgfourelementsMatchResponse, self).parse_response_content(response_content)
        if 'match_code' in response:
            self.match_code = response['match_code']
        if 'match_result_columns' in response:
            self.match_result_columns = response['match_result_columns']

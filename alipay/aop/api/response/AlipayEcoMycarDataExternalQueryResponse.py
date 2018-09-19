#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarDataExternalQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarDataExternalQueryResponse, self).__init__()
        self._external_system_name = None
        self._query_result = None

    @property
    def external_system_name(self):
        return self._external_system_name

    @external_system_name.setter
    def external_system_name(self, value):
        self._external_system_name = value
    @property
    def query_result(self):
        return self._query_result

    @query_result.setter
    def query_result(self, value):
        self._query_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarDataExternalQueryResponse, self).parse_response_content(response_content)
        if 'external_system_name' in response:
            self.external_system_name = response['external_system_name']
        if 'query_result' in response:
            self.query_result = response['query_result']

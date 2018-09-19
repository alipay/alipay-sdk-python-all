#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceRiskOfflinevarsQueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRiskOfflinevarsQueryResponse, self).__init__()
        self._query_result = None
        self._success = None
        self._unique_id = None

    @property
    def query_result(self):
        return self._query_result

    @query_result.setter
    def query_result(self, value):
        self._query_result = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceRiskOfflinevarsQueryResponse, self).parse_response_content(response_content)
        if 'query_result' in response:
            self.query_result = response['query_result']
        if 'success' in response:
            self.success = response['success']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']

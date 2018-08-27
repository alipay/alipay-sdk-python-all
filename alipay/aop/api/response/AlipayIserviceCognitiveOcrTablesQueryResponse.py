#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AiOcrTableRow import AiOcrTableRow


class AlipayIserviceCognitiveOcrTablesQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveOcrTablesQueryResponse, self).__init__()
        self._success = None
        self._tables = None
        self._trace_id = None

    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def tables(self):
        return self._tables

    @tables.setter
    def tables(self, value):
        if isinstance(value, list):
            self._tables = list()
            for i in value:
                if isinstance(i, AiOcrTableRow):
                    self._tables.append(i)
                else:
                    self._tables.append(AiOcrTableRow.from_alipay_dict(i))
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveOcrTablesQueryResponse, self).parse_response_content(response_content)
        if 'success' in response:
            self.success = response['success']
        if 'tables' in response:
            self.tables = response['tables']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']

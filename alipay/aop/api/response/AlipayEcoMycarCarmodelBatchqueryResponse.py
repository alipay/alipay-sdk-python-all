#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QueryResult import QueryResult


class AlipayEcoMycarCarmodelBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarCarmodelBatchqueryResponse, self).__init__()
        self._query_result = None
        self._query_type = None

    @property
    def query_result(self):
        return self._query_result

    @query_result.setter
    def query_result(self, value):
        if isinstance(value, QueryResult):
            self._query_result = value
        else:
            self._query_result = QueryResult.from_alipay_dict(value)
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarCarmodelBatchqueryResponse, self).parse_response_content(response_content)
        if 'query_result' in response:
            self.query_result = response['query_result']
        if 'query_type' in response:
            self.query_type = response['query_type']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SceneProdDataQueryResultDetail import SceneProdDataQueryResultDetail


class MybankCreditSceneprodDataBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodDataBatchqueryResponse, self).__init__()
        self._result_data = None
        self._retry = None
        self._trace_id = None

    @property
    def result_data(self):
        return self._result_data

    @result_data.setter
    def result_data(self, value):
        if isinstance(value, list):
            self._result_data = list()
            for i in value:
                if isinstance(i, SceneProdDataQueryResultDetail):
                    self._result_data.append(i)
                else:
                    self._result_data.append(SceneProdDataQueryResultDetail.from_alipay_dict(i))
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodDataBatchqueryResponse, self).parse_response_content(response_content)
        if 'result_data' in response:
            self.result_data = response['result_data']
        if 'retry' in response:
            self.retry = response['retry']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']

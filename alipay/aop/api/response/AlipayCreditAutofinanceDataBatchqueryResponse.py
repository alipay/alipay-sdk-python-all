#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SceneDataQueryResultDetail import SceneDataQueryResultDetail


class AlipayCreditAutofinanceDataBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCreditAutofinanceDataBatchqueryResponse, self).__init__()
        self._result_data = None

    @property
    def result_data(self):
        return self._result_data

    @result_data.setter
    def result_data(self, value):
        if isinstance(value, list):
            self._result_data = list()
            for i in value:
                if isinstance(i, SceneDataQueryResultDetail):
                    self._result_data.append(i)
                else:
                    self._result_data.append(SceneDataQueryResultDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCreditAutofinanceDataBatchqueryResponse, self).parse_response_content(response_content)
        if 'result_data' in response:
            self.result_data = response['result_data']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecResultInfo import RecResultInfo


class AlipayOpenDataItemRecommendBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenDataItemRecommendBatchqueryResponse, self).__init__()
        self._result_obj = None

    @property
    def result_obj(self):
        return self._result_obj

    @result_obj.setter
    def result_obj(self, value):
        if isinstance(value, list):
            self._result_obj = list()
            for i in value:
                if isinstance(i, RecResultInfo):
                    self._result_obj.append(i)
                else:
                    self._result_obj.append(RecResultInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenDataItemRecommendBatchqueryResponse, self).parse_response_content(response_content)
        if 'result_obj' in response:
            self.result_obj = response['result_obj']

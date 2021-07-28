#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CloudbusSubmitPredictItem import CloudbusSubmitPredictItem


class AlipayDataAiserviceCloudbusPredictbuslineSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataAiserviceCloudbusPredictbuslineSubmitResponse, self).__init__()
        self._result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, CloudbusSubmitPredictItem):
            self._result = value
        else:
            self._result = CloudbusSubmitPredictItem.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataAiserviceCloudbusPredictbuslineSubmitResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']

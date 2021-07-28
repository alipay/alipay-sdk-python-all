#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IntentQueryResponse import IntentQueryResponse


class AlipayIserviceIotIntentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIotIntentQueryResponse, self).__init__()
        self._iot_response = None

    @property
    def iot_response(self):
        return self._iot_response

    @iot_response.setter
    def iot_response(self, value):
        if isinstance(value, IntentQueryResponse):
            self._iot_response = value
        else:
            self._iot_response = IntentQueryResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIotIntentQueryResponse, self).parse_response_content(response_content)
        if 'iot_response' in response:
            self.iot_response = response['iot_response']

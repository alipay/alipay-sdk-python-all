#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CloudbusTimeOdItem import CloudbusTimeOdItem


class AlipayDataAiserviceCloudbusTimeodGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataAiserviceCloudbusTimeodGetResponse, self).__init__()
        self._result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, list):
            self._result = list()
            for i in value:
                if isinstance(i, CloudbusTimeOdItem):
                    self._result.append(i)
                else:
                    self._result.append(CloudbusTimeOdItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataAiserviceCloudbusTimeodGetResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']

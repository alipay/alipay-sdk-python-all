#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ConnectServerAdaptResult import ConnectServerAdaptResult


class AlipayIserviceCliveConnectCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCliveConnectCreateResponse, self).__init__()
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, ConnectServerAdaptResult):
            self._value = value
        else:
            self._value = ConnectServerAdaptResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCliveConnectCreateResponse, self).parse_response_content(response_content)
        if 'value' in response:
            self.value = response['value']

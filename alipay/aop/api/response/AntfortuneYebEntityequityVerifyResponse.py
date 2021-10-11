#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BaseWebResponse import BaseWebResponse


class AntfortuneYebEntityequityVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneYebEntityequityVerifyResponse, self).__init__()
        self._response = None

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        if isinstance(value, BaseWebResponse):
            self._response = value
        else:
            self._response = BaseWebResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntfortuneYebEntityequityVerifyResponse, self).parse_response_content(response_content)
        if 'response' in response:
            self.response = response['response']

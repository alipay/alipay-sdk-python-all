#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNordertagPositionBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordertagPositionBindResponse, self).__init__()
        self._bind_result = None

    @property
    def bind_result(self):
        return self._bind_result

    @bind_result.setter
    def bind_result(self, value):
        self._bind_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordertagPositionBindResponse, self).parse_response_content(response_content)
        if 'bind_result' in response:
            self.bind_result = response['bind_result']

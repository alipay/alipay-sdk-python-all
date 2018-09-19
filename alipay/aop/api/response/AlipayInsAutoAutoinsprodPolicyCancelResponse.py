#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsAutoAutoinsprodPolicyCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoAutoinsprodPolicyCancelResponse, self).__init__()
        self._cancel_result = None

    @property
    def cancel_result(self):
        return self._cancel_result

    @cancel_result.setter
    def cancel_result(self, value):
        self._cancel_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoAutoinsprodPolicyCancelResponse, self).parse_response_content(response_content)
        if 'cancel_result' in response:
            self.cancel_result = response['cancel_result']

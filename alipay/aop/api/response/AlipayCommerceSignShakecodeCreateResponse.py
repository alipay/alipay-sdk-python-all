#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceSignShakecodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSignShakecodeCreateResponse, self).__init__()
        self._shake_code = None

    @property
    def shake_code(self):
        return self._shake_code

    @shake_code.setter
    def shake_code(self, value):
        self._shake_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSignShakecodeCreateResponse, self).parse_response_content(response_content)
        if 'shake_code' in response:
            self.shake_code = response['shake_code']

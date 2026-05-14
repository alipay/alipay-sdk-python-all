#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowShakecodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowShakecodeCreateResponse, self).__init__()
        self._shake_code_text = None

    @property
    def shake_code_text(self):
        return self._shake_code_text

    @shake_code_text.setter
    def shake_code_text(self, value):
        self._shake_code_text = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowShakecodeCreateResponse, self).parse_response_content(response_content)
        if 'shake_code_text' in response:
            self.shake_code_text = response['shake_code_text']

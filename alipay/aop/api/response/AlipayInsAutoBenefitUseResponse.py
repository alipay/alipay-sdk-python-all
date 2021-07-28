#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsAutoBenefitUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoBenefitUseResponse, self).__init__()
        self._use_flow_id = None

    @property
    def use_flow_id(self):
        return self._use_flow_id

    @use_flow_id.setter
    def use_flow_id(self, value):
        self._use_flow_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoBenefitUseResponse, self).parse_response_content(response_content)
        if 'use_flow_id' in response:
            self.use_flow_id = response['use_flow_id']

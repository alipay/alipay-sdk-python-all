#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMiorinsuranceJumpurlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMiorinsuranceJumpurlQueryResponse, self).__init__()
        self._jump_url = None

    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMiorinsuranceJumpurlQueryResponse, self).parse_response_content(response_content)
        if 'jump_url' in response:
            self.jump_url = response['jump_url']

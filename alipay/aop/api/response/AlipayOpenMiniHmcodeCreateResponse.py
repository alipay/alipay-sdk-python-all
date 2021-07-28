#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniHmcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniHmcodeCreateResponse, self).__init__()
        self._hm_code_url = None

    @property
    def hm_code_url(self):
        return self._hm_code_url

    @hm_code_url.setter
    def hm_code_url(self, value):
        self._hm_code_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniHmcodeCreateResponse, self).parse_response_content(response_content)
        if 'hm_code_url' in response:
            self.hm_code_url = response['hm_code_url']

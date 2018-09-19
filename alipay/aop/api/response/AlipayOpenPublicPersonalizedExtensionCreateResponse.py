#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicPersonalizedExtensionCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicPersonalizedExtensionCreateResponse, self).__init__()
        self._extension_key = None

    @property
    def extension_key(self):
        return self._extension_key

    @extension_key.setter
    def extension_key(self, value):
        self._extension_key = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicPersonalizedExtensionCreateResponse, self).parse_response_content(response_content)
        if 'extension_key' in response:
            self.extension_key = response['extension_key']

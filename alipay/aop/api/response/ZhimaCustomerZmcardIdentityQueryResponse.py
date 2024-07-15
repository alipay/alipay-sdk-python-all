#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerZmcardIdentityQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerZmcardIdentityQueryResponse, self).__init__()
        self._skip_url = None
        self._verified = None

    @property
    def skip_url(self):
        return self._skip_url

    @skip_url.setter
    def skip_url(self, value):
        self._skip_url = value
    @property
    def verified(self):
        return self._verified

    @verified.setter
    def verified(self, value):
        self._verified = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerZmcardIdentityQueryResponse, self).parse_response_content(response_content)
        if 'skip_url' in response:
            self.skip_url = response['skip_url']
        if 'verified' in response:
            self.verified = response['verified']

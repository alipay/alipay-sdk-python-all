#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenInstantdeliveryMerchantagreementSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenInstantdeliveryMerchantagreementSignResponse, self).__init__()
        self._sign_url = None

    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenInstantdeliveryMerchantagreementSignResponse, self).parse_response_content(response_content)
        if 'sign_url' in response:
            self.sign_url = response['sign_url']

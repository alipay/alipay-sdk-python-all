#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHdfaccessCifQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHdfaccessCifQueryResponse, self).__init__()
        self._mobile = None

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHdfaccessCifQueryResponse, self).parse_response_content(response_content)
        if 'mobile' in response:
            self.mobile = response['mobile']

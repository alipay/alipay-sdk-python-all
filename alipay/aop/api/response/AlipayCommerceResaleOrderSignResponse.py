#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceResaleOrderSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceResaleOrderSignResponse, self).__init__()
        self._zmxy_sign_url = None

    @property
    def zmxy_sign_url(self):
        return self._zmxy_sign_url

    @zmxy_sign_url.setter
    def zmxy_sign_url(self, value):
        self._zmxy_sign_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceResaleOrderSignResponse, self).parse_response_content(response_content)
        if 'zmxy_sign_url' in response:
            self.zmxy_sign_url = response['zmxy_sign_url']

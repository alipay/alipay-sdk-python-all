#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayAppPaysharingprodFamilypaySignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppPaysharingprodFamilypaySignResponse, self).__init__()
        self._apply_no = None
        self._auth_url = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def auth_url(self):
        return self._auth_url

    @auth_url.setter
    def auth_url(self, value):
        self._auth_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppPaysharingprodFamilypaySignResponse, self).parse_response_content(response_content)
        if 'apply_no' in response:
            self.apply_no = response['apply_no']
        if 'auth_url' in response:
            self.auth_url = response['auth_url']

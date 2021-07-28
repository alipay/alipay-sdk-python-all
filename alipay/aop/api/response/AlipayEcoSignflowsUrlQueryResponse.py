#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoSignflowsUrlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoSignflowsUrlQueryResponse, self).__init__()
        self._preview_short_url = None
        self._preview_url = None
        self._sign_short_url = None
        self._sign_url = None

    @property
    def preview_short_url(self):
        return self._preview_short_url

    @preview_short_url.setter
    def preview_short_url(self, value):
        self._preview_short_url = value
    @property
    def preview_url(self):
        return self._preview_url

    @preview_url.setter
    def preview_url(self, value):
        self._preview_url = value
    @property
    def sign_short_url(self):
        return self._sign_short_url

    @sign_short_url.setter
    def sign_short_url(self, value):
        self._sign_short_url = value
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoSignflowsUrlQueryResponse, self).parse_response_content(response_content)
        if 'preview_short_url' in response:
            self.preview_short_url = response['preview_short_url']
        if 'preview_url' in response:
            self.preview_url = response['preview_url']
        if 'sign_short_url' in response:
            self.sign_short_url = response['sign_short_url']
        if 'sign_url' in response:
            self.sign_url = response['sign_url']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundEnterprisepayMemberjointurlApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundEnterprisepayMemberjointurlApplyResponse, self).__init__()
        self._apply_url = None
        self._apply_url_token = None
        self._expiration_time = None

    @property
    def apply_url(self):
        return self._apply_url

    @apply_url.setter
    def apply_url(self, value):
        self._apply_url = value
    @property
    def apply_url_token(self):
        return self._apply_url_token

    @apply_url_token.setter
    def apply_url_token(self, value):
        self._apply_url_token = value
    @property
    def expiration_time(self):
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, value):
        self._expiration_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundEnterprisepayMemberjointurlApplyResponse, self).parse_response_content(response_content)
        if 'apply_url' in response:
            self.apply_url = response['apply_url']
        if 'apply_url_token' in response:
            self.apply_url_token = response['apply_url_token']
        if 'expiration_time' in response:
            self.expiration_time = response['expiration_time']

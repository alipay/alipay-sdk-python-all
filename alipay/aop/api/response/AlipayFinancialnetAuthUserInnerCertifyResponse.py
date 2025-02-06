#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthUserInnerCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthUserInnerCertifyResponse, self).__init__()
        self._certify_id = None
        self._certify_url = None
        self._open_id = None
        self._user_id = None

    @property
    def certify_id(self):
        return self._certify_id

    @certify_id.setter
    def certify_id(self, value):
        self._certify_id = value
    @property
    def certify_url(self):
        return self._certify_url

    @certify_url.setter
    def certify_url(self, value):
        self._certify_url = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthUserInnerCertifyResponse, self).parse_response_content(response_content)
        if 'certify_id' in response:
            self.certify_id = response['certify_id']
        if 'certify_url' in response:
            self.certify_url = response['certify_url']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'user_id' in response:
            self.user_id = response['user_id']

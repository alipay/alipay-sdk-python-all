#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalAuthTokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalAuthTokenCreateResponse, self).__init__()
        self._aq_access_token = None
        self._aq_open_id = None
        self._expires_in = None

    @property
    def aq_access_token(self):
        return self._aq_access_token

    @aq_access_token.setter
    def aq_access_token(self, value):
        self._aq_access_token = value
    @property
    def aq_open_id(self):
        return self._aq_open_id

    @aq_open_id.setter
    def aq_open_id(self, value):
        self._aq_open_id = value
    @property
    def expires_in(self):
        return self._expires_in

    @expires_in.setter
    def expires_in(self, value):
        self._expires_in = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalAuthTokenCreateResponse, self).parse_response_content(response_content)
        if 'aq_access_token' in response:
            self.aq_access_token = response['aq_access_token']
        if 'aq_open_id' in response:
            self.aq_open_id = response['aq_open_id']
        if 'expires_in' in response:
            self.expires_in = response['expires_in']

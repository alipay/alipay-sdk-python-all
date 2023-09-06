#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFincoreComplianceTemplateInstancecomponentCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceTemplateInstancecomponentCertifyResponse, self).__init__()
        self._al_refresh_token = None
        self._al_refresh_token_expire = None
        self._al_token = None
        self._al_token_expire = None

    @property
    def al_refresh_token(self):
        return self._al_refresh_token

    @al_refresh_token.setter
    def al_refresh_token(self, value):
        self._al_refresh_token = value
    @property
    def al_refresh_token_expire(self):
        return self._al_refresh_token_expire

    @al_refresh_token_expire.setter
    def al_refresh_token_expire(self, value):
        self._al_refresh_token_expire = value
    @property
    def al_token(self):
        return self._al_token

    @al_token.setter
    def al_token(self, value):
        self._al_token = value
    @property
    def al_token_expire(self):
        return self._al_token_expire

    @al_token_expire.setter
    def al_token_expire(self, value):
        self._al_token_expire = value

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceTemplateInstancecomponentCertifyResponse, self).parse_response_content(response_content)
        if 'al_refresh_token' in response:
            self.al_refresh_token = response['al_refresh_token']
        if 'al_refresh_token_expire' in response:
            self.al_refresh_token_expire = response['al_refresh_token_expire']
        if 'al_token' in response:
            self.al_token = response['al_token']
        if 'al_token_expire' in response:
            self.al_token_expire = response['al_token_expire']

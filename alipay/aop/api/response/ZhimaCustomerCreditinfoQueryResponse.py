#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerCreditinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerCreditinfoQueryResponse, self).__init__()
        self._auth = None
        self._auth_award = None
        self._award = None
        self._can_auth = None
        self._credit_level_code = None
        self._sign_id = None

    @property
    def auth(self):
        return self._auth

    @auth.setter
    def auth(self, value):
        self._auth = value
    @property
    def auth_award(self):
        return self._auth_award

    @auth_award.setter
    def auth_award(self, value):
        self._auth_award = value
    @property
    def award(self):
        return self._award

    @award.setter
    def award(self, value):
        self._award = value
    @property
    def can_auth(self):
        return self._can_auth

    @can_auth.setter
    def can_auth(self, value):
        self._can_auth = value
    @property
    def credit_level_code(self):
        return self._credit_level_code

    @credit_level_code.setter
    def credit_level_code(self, value):
        self._credit_level_code = value
    @property
    def sign_id(self):
        return self._sign_id

    @sign_id.setter
    def sign_id(self, value):
        self._sign_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerCreditinfoQueryResponse, self).parse_response_content(response_content)
        if 'auth' in response:
            self.auth = response['auth']
        if 'auth_award' in response:
            self.auth_award = response['auth_award']
        if 'award' in response:
            self.award = response['award']
        if 'can_auth' in response:
            self.can_auth = response['can_auth']
        if 'credit_level_code' in response:
            self.credit_level_code = response['credit_level_code']
        if 'sign_id' in response:
            self.sign_id = response['sign_id']

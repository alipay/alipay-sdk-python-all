#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceRiskBusinesslicenseCertifyResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRiskBusinesslicenseCertifyResponse, self).__init__()
        self._address = None
        self._bis_token = None
        self._check_result = None
        self._credit_code = None
        self._ent_legal_name = None
        self._ent_name = None
        self._expires = None
        self._expires_end = None
        self._expires_start = None
        self._match_param = None
        self._no_match_param = None
        self._unique_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def bis_token(self):
        return self._bis_token

    @bis_token.setter
    def bis_token(self, value):
        self._bis_token = value
    @property
    def check_result(self):
        return self._check_result

    @check_result.setter
    def check_result(self, value):
        self._check_result = value
    @property
    def credit_code(self):
        return self._credit_code

    @credit_code.setter
    def credit_code(self, value):
        self._credit_code = value
    @property
    def ent_legal_name(self):
        return self._ent_legal_name

    @ent_legal_name.setter
    def ent_legal_name(self, value):
        self._ent_legal_name = value
    @property
    def ent_name(self):
        return self._ent_name

    @ent_name.setter
    def ent_name(self, value):
        self._ent_name = value
    @property
    def expires(self):
        return self._expires

    @expires.setter
    def expires(self, value):
        self._expires = value
    @property
    def expires_end(self):
        return self._expires_end

    @expires_end.setter
    def expires_end(self, value):
        self._expires_end = value
    @property
    def expires_start(self):
        return self._expires_start

    @expires_start.setter
    def expires_start(self, value):
        self._expires_start = value
    @property
    def match_param(self):
        return self._match_param

    @match_param.setter
    def match_param(self, value):
        self._match_param = value
    @property
    def no_match_param(self):
        return self._no_match_param

    @no_match_param.setter
    def no_match_param(self, value):
        self._no_match_param = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceRiskBusinesslicenseCertifyResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'bis_token' in response:
            self.bis_token = response['bis_token']
        if 'check_result' in response:
            self.check_result = response['check_result']
        if 'credit_code' in response:
            self.credit_code = response['credit_code']
        if 'ent_legal_name' in response:
            self.ent_legal_name = response['ent_legal_name']
        if 'ent_name' in response:
            self.ent_name = response['ent_name']
        if 'expires' in response:
            self.expires = response['expires']
        if 'expires_end' in response:
            self.expires_end = response['expires_end']
        if 'expires_start' in response:
            self.expires_start = response['expires_start']
        if 'match_param' in response:
            self.match_param = response['match_param']
        if 'no_match_param' in response:
            self.no_match_param = response['no_match_param']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']

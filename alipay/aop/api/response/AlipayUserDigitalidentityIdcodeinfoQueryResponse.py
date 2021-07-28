#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserDigitalidentityIdcodeinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDigitalidentityIdcodeinfoQueryResponse, self).__init__()
        self._aes_key_encrypted = None
        self._user_data = None
        self._user_data_sign = None
        self._verify_result = None

    @property
    def aes_key_encrypted(self):
        return self._aes_key_encrypted

    @aes_key_encrypted.setter
    def aes_key_encrypted(self, value):
        self._aes_key_encrypted = value
    @property
    def user_data(self):
        return self._user_data

    @user_data.setter
    def user_data(self, value):
        self._user_data = value
    @property
    def user_data_sign(self):
        return self._user_data_sign

    @user_data_sign.setter
    def user_data_sign(self, value):
        self._user_data_sign = value
    @property
    def verify_result(self):
        return self._verify_result

    @verify_result.setter
    def verify_result(self, value):
        self._verify_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserDigitalidentityIdcodeinfoQueryResponse, self).parse_response_content(response_content)
        if 'aes_key_encrypted' in response:
            self.aes_key_encrypted = response['aes_key_encrypted']
        if 'user_data' in response:
            self.user_data = response['user_data']
        if 'user_data_sign' in response:
            self.user_data_sign = response['user_data_sign']
        if 'verify_result' in response:
            self.verify_result = response['verify_result']

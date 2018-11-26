#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryKmsPubkeyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryKmsPubkeyQueryResponse, self).__init__()
        self._user_encrypt_pubkey = None

    @property
    def user_encrypt_pubkey(self):
        return self._user_encrypt_pubkey

    @user_encrypt_pubkey.setter
    def user_encrypt_pubkey(self, value):
        self._user_encrypt_pubkey = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryKmsPubkeyQueryResponse, self).parse_response_content(response_content)
        if 'user_encrypt_pubkey' in response:
            self.user_encrypt_pubkey = response['user_encrypt_pubkey']

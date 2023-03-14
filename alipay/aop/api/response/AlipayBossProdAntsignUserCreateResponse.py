#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdAntsignUserCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntsignUserCreateResponse, self).__init__()
        self._sign_user_unique_id = None

    @property
    def sign_user_unique_id(self):
        return self._sign_user_unique_id

    @sign_user_unique_id.setter
    def sign_user_unique_id(self, value):
        self._sign_user_unique_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntsignUserCreateResponse, self).parse_response_content(response_content)
        if 'sign_user_unique_id' in response:
            self.sign_user_unique_id = response['sign_user_unique_id']

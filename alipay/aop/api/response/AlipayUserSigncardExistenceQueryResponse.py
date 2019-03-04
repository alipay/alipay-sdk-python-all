#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserSigncardExistenceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserSigncardExistenceQueryResponse, self).__init__()
        self._sign_card_exist = None

    @property
    def sign_card_exist(self):
        return self._sign_card_exist

    @sign_card_exist.setter
    def sign_card_exist(self, value):
        self._sign_card_exist = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserSigncardExistenceQueryResponse, self).parse_response_content(response_content)
        if 'sign_card_exist' in response:
            self.sign_card_exist = response['sign_card_exist']

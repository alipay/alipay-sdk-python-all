#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAuthSecondpartyTokenVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAuthSecondpartyTokenVerifyResponse, self).__init__()
        self._tb_user_id = None

    @property
    def tb_user_id(self):
        return self._tb_user_id

    @tb_user_id.setter
    def tb_user_id(self, value):
        self._tb_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAuthSecondpartyTokenVerifyResponse, self).parse_response_content(response_content)
        if 'tb_user_id' in response:
            self.tb_user_id = response['tb_user_id']

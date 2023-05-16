#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundAccountThaworfreezeModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAccountThaworfreezeModifyResponse, self).__init__()
        self._taobao_user_id = None

    @property
    def taobao_user_id(self):
        return self._taobao_user_id

    @taobao_user_id.setter
    def taobao_user_id(self, value):
        self._taobao_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAccountThaworfreezeModifyResponse, self).parse_response_content(response_content)
        if 'taobao_user_id' in response:
            self.taobao_user_id = response['taobao_user_id']

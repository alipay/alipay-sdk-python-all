#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantQipanCrowdCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantQipanCrowdCreateResponse, self).__init__()
        self._crowd_code = None

    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        self._crowd_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantQipanCrowdCreateResponse, self).parse_response_content(response_content)
        if 'crowd_code' in response:
            self.crowd_code = response['crowd_code']

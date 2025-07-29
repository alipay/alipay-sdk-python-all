#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantGroupAutoreplyCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupAutoreplyCreateormodifyResponse, self).__init__()
        self._autoreply_id = None

    @property
    def autoreply_id(self):
        return self._autoreply_id

    @autoreply_id.setter
    def autoreply_id(self, value):
        self._autoreply_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupAutoreplyCreateormodifyResponse, self).parse_response_content(response_content)
        if 'autoreply_id' in response:
            self.autoreply_id = response['autoreply_id']

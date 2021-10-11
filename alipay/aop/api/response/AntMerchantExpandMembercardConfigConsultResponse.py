#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandMembercardConfigConsultResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandMembercardConfigConsultResponse, self).__init__()
        self._detail = None
        self._valid = None

    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value
    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandMembercardConfigConsultResponse, self).parse_response_content(response_content)
        if 'detail' in response:
            self.detail = response['detail']
        if 'valid' in response:
            self.valid = response['valid']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppProdmodeAgreementUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppProdmodeAgreementUploadResponse, self).__init__()
        self._is_success = None
        self._memo = None

    @property
    def is_success(self):
        return self._is_success

    @is_success.setter
    def is_success(self, value):
        self._is_success = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppProdmodeAgreementUploadResponse, self).parse_response_content(response_content)
        if 'is_success' in response:
            self.is_success = response['is_success']
        if 'memo' in response:
            self.memo = response['memo']

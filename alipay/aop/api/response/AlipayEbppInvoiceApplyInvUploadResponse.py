#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceApplyInvUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceApplyInvUploadResponse, self).__init__()
        self._is_success = None

    @property
    def is_success(self):
        return self._is_success

    @is_success.setter
    def is_success(self, value):
        self._is_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceApplyInvUploadResponse, self).parse_response_content(response_content)
        if 'is_success' in response:
            self.is_success = response['is_success']

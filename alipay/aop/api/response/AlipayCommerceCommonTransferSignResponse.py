#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCommonTransferSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonTransferSignResponse, self).__init__()
        self._operation_url = None

    @property
    def operation_url(self):
        return self._operation_url

    @operation_url.setter
    def operation_url(self, value):
        self._operation_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonTransferSignResponse, self).parse_response_content(response_content)
        if 'operation_url' in response:
            self.operation_url = response['operation_url']

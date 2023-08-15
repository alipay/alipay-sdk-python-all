#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcTcnInvoiceapplyModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcTcnInvoiceapplyModifyResponse, self).__init__()
        self._apply_id = None
        self._apply_status = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcTcnInvoiceapplyModifyResponse, self).parse_response_content(response_content)
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
        if 'apply_status' in response:
            self.apply_status = response['apply_status']

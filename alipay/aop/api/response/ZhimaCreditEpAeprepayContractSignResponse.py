#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpAeprepayContractSignResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpAeprepayContractSignResponse, self).__init__()
        self._ar_no = None
        self._failed_code = None
        self._failed_message = None

    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def failed_code(self):
        return self._failed_code

    @failed_code.setter
    def failed_code(self, value):
        self._failed_code = value
    @property
    def failed_message(self):
        return self._failed_message

    @failed_message.setter
    def failed_message(self, value):
        self._failed_message = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpAeprepayContractSignResponse, self).parse_response_content(response_content)
        if 'ar_no' in response:
            self.ar_no = response['ar_no']
        if 'failed_code' in response:
            self.failed_code = response['failed_code']
        if 'failed_message' in response:
            self.failed_message = response['failed_message']

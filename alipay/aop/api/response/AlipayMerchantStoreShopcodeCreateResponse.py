#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantStoreShopcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantStoreShopcodeCreateResponse, self).__init__()
        self._apply_id = None
        self._confirm_url = None
        self._result_code = None
        self._result_desc = None
        self._status = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def confirm_url(self):
        return self._confirm_url

    @confirm_url.setter
    def confirm_url(self, value):
        self._confirm_url = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantStoreShopcodeCreateResponse, self).parse_response_content(response_content)
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
        if 'confirm_url' in response:
            self.confirm_url = response['confirm_url']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
        if 'status' in response:
            self.status = response['status']

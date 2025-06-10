#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneEcommerceRiskCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEcommerceRiskCheckResponse, self).__init__()
        self._access = None
        self._reject_reason_code = None
        self._reject_reason_detail = None

    @property
    def access(self):
        return self._access

    @access.setter
    def access(self, value):
        self._access = value
    @property
    def reject_reason_code(self):
        return self._reject_reason_code

    @reject_reason_code.setter
    def reject_reason_code(self, value):
        self._reject_reason_code = value
    @property
    def reject_reason_detail(self):
        return self._reject_reason_detail

    @reject_reason_detail.setter
    def reject_reason_detail(self, value):
        self._reject_reason_detail = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEcommerceRiskCheckResponse, self).parse_response_content(response_content)
        if 'access' in response:
            self.access = response['access']
        if 'reject_reason_code' in response:
            self.reject_reason_code = response['reject_reason_code']
        if 'reject_reason_detail' in response:
            self.reject_reason_detail = response['reject_reason_detail']

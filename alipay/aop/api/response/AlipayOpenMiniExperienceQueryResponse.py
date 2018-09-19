#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniExperienceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniExperienceQueryResponse, self).__init__()
        self._exp_qr_code_url = None
        self._status = None

    @property
    def exp_qr_code_url(self):
        return self._exp_qr_code_url

    @exp_qr_code_url.setter
    def exp_qr_code_url(self, value):
        self._exp_qr_code_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniExperienceQueryResponse, self).parse_response_content(response_content)
        if 'exp_qr_code_url' in response:
            self.exp_qr_code_url = response['exp_qr_code_url']
        if 'status' in response:
            self.status = response['status']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInsuranceFesSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceFesSendResponse, self).__init__()
        self._enc_content = None

    @property
    def enc_content(self):
        return self._enc_content

    @enc_content.setter
    def enc_content(self, value):
        self._enc_content = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceFesSendResponse, self).parse_response_content(response_content)
        if 'enc_content' in response:
            self.enc_content = response['enc_content']

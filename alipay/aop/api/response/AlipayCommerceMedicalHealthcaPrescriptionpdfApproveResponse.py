#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHealthcaPrescriptionpdfApproveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHealthcaPrescriptionpdfApproveResponse, self).__init__()
        self._sign_flow_id = None

    @property
    def sign_flow_id(self):
        return self._sign_flow_id

    @sign_flow_id.setter
    def sign_flow_id(self, value):
        self._sign_flow_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHealthcaPrescriptionpdfApproveResponse, self).parse_response_content(response_content)
        if 'sign_flow_id' in response:
            self.sign_flow_id = response['sign_flow_id']

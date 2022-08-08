#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudFinsaasInsuranceriskGetResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasInsuranceriskGetResponse, self).__init__()
        self._risk_content = None

    @property
    def risk_content(self):
        return self._risk_content

    @risk_content.setter
    def risk_content(self, value):
        self._risk_content = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasInsuranceriskGetResponse, self).parse_response_content(response_content)
        if 'risk_content' in response:
            self.risk_content = response['risk_content']

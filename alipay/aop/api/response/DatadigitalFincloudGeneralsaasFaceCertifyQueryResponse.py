#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudGeneralsaasFaceCertifyQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasFaceCertifyQueryResponse, self).__init__()
        self._fail_reason = None
        self._identity_info = None
        self._material_info = None
        self._passed = None

    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def identity_info(self):
        return self._identity_info

    @identity_info.setter
    def identity_info(self, value):
        self._identity_info = value
    @property
    def material_info(self):
        return self._material_info

    @material_info.setter
    def material_info(self, value):
        self._material_info = value
    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasFaceCertifyQueryResponse, self).parse_response_content(response_content)
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'identity_info' in response:
            self.identity_info = response['identity_info']
        if 'material_info' in response:
            self.material_info = response['material_info']
        if 'passed' in response:
            self.passed = response['passed']

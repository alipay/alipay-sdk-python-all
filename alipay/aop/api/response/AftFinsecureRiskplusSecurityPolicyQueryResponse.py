#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AftFinsecureRiskplusSecurityPolicyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AftFinsecureRiskplusSecurityPolicyQueryResponse, self).__init__()
        self._level = None
        self._security_id = None
        self._security_result = None
        self._success = None
        self._template_code = None
        self._template_desc = None
        self._verify_id = None
        self._verify_url = None

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def security_id(self):
        return self._security_id

    @security_id.setter
    def security_id(self, value):
        self._security_id = value
    @property
    def security_result(self):
        return self._security_result

    @security_result.setter
    def security_result(self, value):
        self._security_result = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def template_desc(self):
        return self._template_desc

    @template_desc.setter
    def template_desc(self, value):
        self._template_desc = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value
    @property
    def verify_url(self):
        return self._verify_url

    @verify_url.setter
    def verify_url(self, value):
        self._verify_url = value

    def parse_response_content(self, response_content):
        response = super(AftFinsecureRiskplusSecurityPolicyQueryResponse, self).parse_response_content(response_content)
        if 'level' in response:
            self.level = response['level']
        if 'security_id' in response:
            self.security_id = response['security_id']
        if 'security_result' in response:
            self.security_result = response['security_result']
        if 'success' in response:
            self.success = response['success']
        if 'template_code' in response:
            self.template_code = response['template_code']
        if 'template_desc' in response:
            self.template_desc = response['template_desc']
        if 'verify_id' in response:
            self.verify_id = response['verify_id']
        if 'verify_url' in response:
            self.verify_url = response['verify_url']

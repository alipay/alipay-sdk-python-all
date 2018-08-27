#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CertAuditResult import CertAuditResult


class ZolozIdentificationCustomerIdcardCertifyResponse(AlipayResponse):

    def __init__(self):
        super(ZolozIdentificationCustomerIdcardCertifyResponse, self).__init__()
        self._cert_audit_result = None
        self._passed = None
        self._token = None

    @property
    def cert_audit_result(self):
        return self._cert_audit_result

    @cert_audit_result.setter
    def cert_audit_result(self, value):
        if isinstance(value, list):
            self._cert_audit_result = list()
            for i in value:
                if isinstance(i, CertAuditResult):
                    self._cert_audit_result.append(i)
                else:
                    self._cert_audit_result.append(CertAuditResult.from_alipay_dict(i))
    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def parse_response_content(self, response_content):
        response = super(ZolozIdentificationCustomerIdcardCertifyResponse, self).parse_response_content(response_content)
        if 'cert_audit_result' in response:
            self.cert_audit_result = response['cert_audit_result']
        if 'passed' in response:
            self.passed = response['passed']
        if 'token' in response:
            self.token = response['token']

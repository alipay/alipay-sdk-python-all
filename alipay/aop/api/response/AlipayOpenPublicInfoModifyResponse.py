#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicInfoModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicInfoModifyResponse, self).__init__()
        self._audit_desc = None
        self._audit_status = None

    @property
    def audit_desc(self):
        return self._audit_desc

    @audit_desc.setter
    def audit_desc(self, value):
        self._audit_desc = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicInfoModifyResponse, self).parse_response_content(response_content)
        if 'audit_desc' in response:
            self.audit_desc = response['audit_desc']
        if 'audit_status' in response:
            self.audit_status = response['audit_status']

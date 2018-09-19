#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiShopMallAuditQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiShopMallAuditQueryResponse, self).__init__()
        self._audit_remark = None
        self._audit_status = None

    @property
    def audit_remark(self):
        return self._audit_remark

    @audit_remark.setter
    def audit_remark(self, value):
        self._audit_remark = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value

    def parse_response_content(self, response_content):
        response = super(KoubeiShopMallAuditQueryResponse, self).parse_response_content(response_content)
        if 'audit_remark' in response:
            self.audit_remark = response['audit_remark']
        if 'audit_status' in response:
            self.audit_status = response['audit_status']

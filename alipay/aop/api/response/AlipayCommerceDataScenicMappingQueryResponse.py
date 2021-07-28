#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ScenicAuditResponse import ScenicAuditResponse


class AlipayCommerceDataScenicMappingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDataScenicMappingQueryResponse, self).__init__()
        self._scenic_audit_response = None

    @property
    def scenic_audit_response(self):
        return self._scenic_audit_response

    @scenic_audit_response.setter
    def scenic_audit_response(self, value):
        if isinstance(value, ScenicAuditResponse):
            self._scenic_audit_response = value
        else:
            self._scenic_audit_response = ScenicAuditResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDataScenicMappingQueryResponse, self).parse_response_content(response_content)
        if 'scenic_audit_response' in response:
            self.scenic_audit_response = response['scenic_audit_response']

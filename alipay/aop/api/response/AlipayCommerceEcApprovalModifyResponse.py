#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcApprovalModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcApprovalModifyResponse, self).__init__()
        self._platform_approval_id = None

    @property
    def platform_approval_id(self):
        return self._platform_approval_id

    @platform_approval_id.setter
    def platform_approval_id(self, value):
        self._platform_approval_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcApprovalModifyResponse, self).parse_response_content(response_content)
        if 'platform_approval_id' in response:
            self.platform_approval_id = response['platform_approval_id']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcRecyclinginvoiceClerkquotaModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceClerkquotaModifyResponse, self).__init__()
        self._clerk_quota_id = None

    @property
    def clerk_quota_id(self):
        return self._clerk_quota_id

    @clerk_quota_id.setter
    def clerk_quota_id(self, value):
        self._clerk_quota_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceClerkquotaModifyResponse, self).parse_response_content(response_content)
        if 'clerk_quota_id' in response:
            self.clerk_quota_id = response['clerk_quota_id']

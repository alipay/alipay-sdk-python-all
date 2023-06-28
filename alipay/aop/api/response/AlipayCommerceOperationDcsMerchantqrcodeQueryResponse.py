#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationDcsMerchantqrcodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationDcsMerchantqrcodeQueryResponse, self).__init__()
        self._apply_merchant_pid = None
        self._role_id = None
        self._role_ids = None

    @property
    def apply_merchant_pid(self):
        return self._apply_merchant_pid

    @apply_merchant_pid.setter
    def apply_merchant_pid(self, value):
        self._apply_merchant_pid = value
    @property
    def role_id(self):
        return self._role_id

    @role_id.setter
    def role_id(self, value):
        self._role_id = value
    @property
    def role_ids(self):
        return self._role_ids

    @role_ids.setter
    def role_ids(self, value):
        if isinstance(value, list):
            self._role_ids = list()
            for i in value:
                self._role_ids.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationDcsMerchantqrcodeQueryResponse, self).parse_response_content(response_content)
        if 'apply_merchant_pid' in response:
            self.apply_merchant_pid = response['apply_merchant_pid']
        if 'role_id' in response:
            self.role_id = response['role_id']
        if 'role_ids' in response:
            self.role_ids = response['role_ids']

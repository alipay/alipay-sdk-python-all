#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceEnterpriseMerchantrelationCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEnterpriseMerchantrelationCreateResponse, self).__init__()
        self._pid = None
        self._role_type = None
        self._shop_id = None
        self._success = None

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEnterpriseMerchantrelationCreateResponse, self).parse_response_content(response_content)
        if 'pid' in response:
            self.pid = response['pid']
        if 'role_type' in response:
            self.role_type = response['role_type']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'success' in response:
            self.success = response['success']

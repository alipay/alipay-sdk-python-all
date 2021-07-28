#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandWarehouseOrderSyncResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandWarehouseOrderSyncResponse, self).__init__()
        self._assign_item_id = None
        self._error_code = None
        self._error_desc = None
        self._success = None

    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        self._assign_item_id = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_desc(self):
        return self._error_desc

    @error_desc.setter
    def error_desc(self, value):
        self._error_desc = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandWarehouseOrderSyncResponse, self).parse_response_content(response_content)
        if 'assign_item_id' in response:
            self.assign_item_id = response['assign_item_id']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_desc' in response:
            self.error_desc = response['error_desc']
        if 'success' in response:
            self.success = response['success']

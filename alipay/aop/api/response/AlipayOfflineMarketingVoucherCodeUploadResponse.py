#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineMarketingVoucherCodeUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketingVoucherCodeUploadResponse, self).__init__()
        self._code_inventory_id = None

    @property
    def code_inventory_id(self):
        return self._code_inventory_id

    @code_inventory_id.setter
    def code_inventory_id(self, value):
        self._code_inventory_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketingVoucherCodeUploadResponse, self).parse_response_content(response_content)
        if 'code_inventory_id' in response:
            self.code_inventory_id = response['code_inventory_id']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantItemFileUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantItemFileUploadResponse, self).__init__()
        self._material_id = None
        self._material_key = None

    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value
    @property
    def material_key(self):
        return self._material_key

    @material_key.setter
    def material_key(self, value):
        self._material_key = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantItemFileUploadResponse, self).parse_response_content(response_content)
        if 'material_id' in response:
            self.material_id = response['material_id']
        if 'material_key' in response:
            self.material_key = response['material_key']

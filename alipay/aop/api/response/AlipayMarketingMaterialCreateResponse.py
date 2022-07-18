#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingMaterialCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingMaterialCreateResponse, self).__init__()
        self._material_id = None

    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingMaterialCreateResponse, self).parse_response_content(response_content)
        if 'material_id' in response:
            self.material_id = response['material_id']

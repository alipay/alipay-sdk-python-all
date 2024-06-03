#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdMaterialUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdMaterialUploadResponse, self).__init__()
        self._material_instance_id = None

    @property
    def material_instance_id(self):
        return self._material_instance_id

    @material_instance_id.setter
    def material_instance_id(self, value):
        self._material_instance_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdMaterialUploadResponse, self).parse_response_content(response_content)
        if 'material_instance_id' in response:
            self.material_instance_id = response['material_instance_id']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayIotNfcpointUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayIotNfcpointUploadResponse, self).__init__()
        self._material_id = None
        self._material_url = None

    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value
    @property
    def material_url(self):
        return self._material_url

    @material_url.setter
    def material_url(self, value):
        self._material_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayIotNfcpointUploadResponse, self).parse_response_content(response_content)
        if 'material_id' in response:
            self.material_id = response['material_id']
        if 'material_url' in response:
            self.material_url = response['material_url']

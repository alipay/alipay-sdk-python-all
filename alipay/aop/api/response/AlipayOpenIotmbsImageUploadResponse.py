#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotmbsImageUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotmbsImageUploadResponse, self).__init__()
        self._audit_status = None
        self._image_id = None

    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotmbsImageUploadResponse, self).parse_response_content(response_content)
        if 'audit_status' in response:
            self.audit_status = response['audit_status']
        if 'image_id' in response:
            self.image_id = response['image_id']

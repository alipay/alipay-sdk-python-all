#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingMaterialImageUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingMaterialImageUploadResponse, self).__init__()
        self._resource_enhance = None
        self._resource_id = None
        self._resource_url = None

    @property
    def resource_enhance(self):
        return self._resource_enhance

    @resource_enhance.setter
    def resource_enhance(self, value):
        self._resource_enhance = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def resource_url(self):
        return self._resource_url

    @resource_url.setter
    def resource_url(self, value):
        self._resource_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingMaterialImageUploadResponse, self).parse_response_content(response_content)
        if 'resource_enhance' in response:
            self.resource_enhance = response['resource_enhance']
        if 'resource_id' in response:
            self.resource_id = response['resource_id']
        if 'resource_url' in response:
            self.resource_url = response['resource_url']

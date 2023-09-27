#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseLayerVersionUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseLayerVersionUploadResponse, self).__init__()
        self._upload_id = None
        self._url = None

    @property
    def upload_id(self):
        return self._upload_id

    @upload_id.setter
    def upload_id(self, value):
        self._upload_id = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseLayerVersionUploadResponse, self).parse_response_content(response_content)
        if 'upload_id' in response:
            self.upload_id = response['upload_id']
        if 'url' in response:
            self.url = response['url']

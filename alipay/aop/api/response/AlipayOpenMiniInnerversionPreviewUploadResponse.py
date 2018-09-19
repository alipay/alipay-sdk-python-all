#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerversionPreviewUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionPreviewUploadResponse, self).__init__()
        self._build_package_url = None

    @property
    def build_package_url(self):
        return self._build_package_url

    @build_package_url.setter
    def build_package_url(self, value):
        self._build_package_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionPreviewUploadResponse, self).parse_response_content(response_content)
        if 'build_package_url' in response:
            self.build_package_url = response['build_package_url']

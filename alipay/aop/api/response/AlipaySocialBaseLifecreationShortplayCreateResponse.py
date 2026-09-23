#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseLifecreationShortplayCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseLifecreationShortplayCreateResponse, self).__init__()
        self._album_id = None
        self._lib_version = None

    @property
    def album_id(self):
        return self._album_id

    @album_id.setter
    def album_id(self, value):
        self._album_id = value
    @property
    def lib_version(self):
        return self._lib_version

    @lib_version.setter
    def lib_version(self, value):
        self._lib_version = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseLifecreationShortplayCreateResponse, self).parse_response_content(response_content)
        if 'album_id' in response:
            self.album_id = response['album_id']
        if 'lib_version' in response:
            self.lib_version = response['lib_version']

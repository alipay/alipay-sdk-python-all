#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseLifecreationShortplayModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseLifecreationShortplayModifyResponse, self).__init__()
        self._album_id = None
        self._lib_version = None
        self._update_time = None

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
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseLifecreationShortplayModifyResponse, self).parse_response_content(response_content)
        if 'album_id' in response:
            self.album_id = response['album_id']
        if 'lib_version' in response:
            self.lib_version = response['lib_version']
        if 'update_time' in response:
            self.update_time = response['update_time']

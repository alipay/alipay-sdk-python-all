#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftOssPresignedurlGetResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftOssPresignedurlGetResponse, self).__init__()
        self._oss_header_callback = None
        self._presigned_url = None

    @property
    def oss_header_callback(self):
        return self._oss_header_callback

    @oss_header_callback.setter
    def oss_header_callback(self, value):
        self._oss_header_callback = value
    @property
    def presigned_url(self):
        return self._presigned_url

    @presigned_url.setter
    def presigned_url(self, value):
        self._presigned_url = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftOssPresignedurlGetResponse, self).parse_response_content(response_content)
        if 'oss_header_callback' in response:
            self.oss_header_callback = response['oss_header_callback']
        if 'presigned_url' in response:
            self.presigned_url = response['presigned_url']

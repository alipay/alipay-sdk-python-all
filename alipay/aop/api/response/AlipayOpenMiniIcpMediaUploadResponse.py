#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniIcpMediaUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniIcpMediaUploadResponse, self).__init__()
        self._media_id = None

    @property
    def media_id(self):
        return self._media_id

    @media_id.setter
    def media_id(self, value):
        self._media_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniIcpMediaUploadResponse, self).parse_response_content(response_content)
        if 'media_id' in response:
            self.media_id = response['media_id']

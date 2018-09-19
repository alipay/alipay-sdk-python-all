#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdFacerepoSearchResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdFacerepoSearchResponse, self).__init__()
        self._ext_info = None
        self._face_id = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def face_id(self):
        return self._face_id

    @face_id.setter
    def face_id(self, value):
        self._face_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdFacerepoSearchResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'face_id' in response:
            self.face_id = response['face_id']

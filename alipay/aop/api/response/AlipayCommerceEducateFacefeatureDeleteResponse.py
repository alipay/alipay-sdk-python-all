#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateFacefeatureDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateFacefeatureDeleteResponse, self).__init__()
        self._face_ids = None

    @property
    def face_ids(self):
        return self._face_ids

    @face_ids.setter
    def face_ids(self, value):
        if isinstance(value, list):
            self._face_ids = list()
            for i in value:
                self._face_ids.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateFacefeatureDeleteResponse, self).parse_response_content(response_content)
        if 'face_ids' in response:
            self.face_ids = response['face_ids']

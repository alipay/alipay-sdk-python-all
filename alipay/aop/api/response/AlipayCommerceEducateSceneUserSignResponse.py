#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSceneUserSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSceneUserSignResponse, self).__init__()
        self._face_user_id = None

    @property
    def face_user_id(self):
        return self._face_user_id

    @face_user_id.setter
    def face_user_id(self, value):
        self._face_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSceneUserSignResponse, self).parse_response_content(response_content)
        if 'face_user_id' in response:
            self.face_user_id = response['face_user_id']

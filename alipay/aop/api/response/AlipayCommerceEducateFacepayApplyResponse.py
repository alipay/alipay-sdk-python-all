#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateFacepayApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateFacepayApplyResponse, self).__init__()
        self._apply_token = None
        self._face_uid = None
        self._school_stdcode = None

    @property
    def apply_token(self):
        return self._apply_token

    @apply_token.setter
    def apply_token(self, value):
        self._apply_token = value
    @property
    def face_uid(self):
        return self._face_uid

    @face_uid.setter
    def face_uid(self, value):
        self._face_uid = value
    @property
    def school_stdcode(self):
        return self._school_stdcode

    @school_stdcode.setter
    def school_stdcode(self, value):
        self._school_stdcode = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateFacepayApplyResponse, self).parse_response_content(response_content)
        if 'apply_token' in response:
            self.apply_token = response['apply_token']
        if 'face_uid' in response:
            self.face_uid = response['face_uid']
        if 'school_stdcode' in response:
            self.school_stdcode = response['school_stdcode']

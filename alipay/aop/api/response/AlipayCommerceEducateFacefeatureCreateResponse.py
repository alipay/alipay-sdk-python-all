#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StandardFacePutInfo import StandardFacePutInfo


class AlipayCommerceEducateFacefeatureCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateFacefeatureCreateResponse, self).__init__()
        self._face_put_list = None

    @property
    def face_put_list(self):
        return self._face_put_list

    @face_put_list.setter
    def face_put_list(self, value):
        if isinstance(value, list):
            self._face_put_list = list()
            for i in value:
                if isinstance(i, StandardFacePutInfo):
                    self._face_put_list.append(i)
                else:
                    self._face_put_list.append(StandardFacePutInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateFacefeatureCreateResponse, self).parse_response_content(response_content)
        if 'face_put_list' in response:
            self.face_put_list = response['face_put_list']

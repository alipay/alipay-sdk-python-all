#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAigcAipictureQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAigcAipictureQueryResponse, self).__init__()
        self._hd_image_id = None

    @property
    def hd_image_id(self):
        return self._hd_image_id

    @hd_image_id.setter
    def hd_image_id(self, value):
        self._hd_image_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAigcAipictureQueryResponse, self).parse_response_content(response_content)
        if 'hd_image_id' in response:
            self.hd_image_id = response['hd_image_id']

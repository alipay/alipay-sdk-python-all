#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotvspFaceimgstateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotvspFaceimgstateQueryResponse, self).__init__()
        self._upload = None

    @property
    def upload(self):
        return self._upload

    @upload.setter
    def upload(self, value):
        self._upload = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotvspFaceimgstateQueryResponse, self).parse_response_content(response_content)
        if 'upload' in response:
            self.upload = response['upload']

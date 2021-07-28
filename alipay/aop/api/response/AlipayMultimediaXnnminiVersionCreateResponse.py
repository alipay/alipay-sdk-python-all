#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMultimediaXnnminiVersionCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMultimediaXnnminiVersionCreateResponse, self).__init__()
        self._version_id = None

    @property
    def version_id(self):
        return self._version_id

    @version_id.setter
    def version_id(self, value):
        self._version_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMultimediaXnnminiVersionCreateResponse, self).parse_response_content(response_content)
        if 'version_id' in response:
            self.version_id = response['version_id']

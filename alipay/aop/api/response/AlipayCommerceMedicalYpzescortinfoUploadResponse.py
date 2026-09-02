#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalYpzescortinfoUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalYpzescortinfoUploadResponse, self).__init__()
        self._escort_id = None

    @property
    def escort_id(self):
        return self._escort_id

    @escort_id.setter
    def escort_id(self, value):
        self._escort_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalYpzescortinfoUploadResponse, self).parse_response_content(response_content)
        if 'escort_id' in response:
            self.escort_id = response['escort_id']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdDmpCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdDmpCreateResponse, self).__init__()
        self._crowd_id = None
        self._crowd_name = None
        self._status = None

    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdDmpCreateResponse, self).parse_response_content(response_content)
        if 'crowd_id' in response:
            self.crowd_id = response['crowd_id']
        if 'crowd_name' in response:
            self.crowd_name = response['crowd_name']
        if 'status' in response:
            self.status = response['status']

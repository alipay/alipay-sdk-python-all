#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserMpointAlllpointReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserMpointAlllpointReceiveResponse, self).__init__()
        self._point = None
        self._status = None

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserMpointAlllpointReceiveResponse, self).parse_response_content(response_content)
        if 'point' in response:
            self.point = response['point']
        if 'status' in response:
            self.status = response['status']

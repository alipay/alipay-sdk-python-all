#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotmbsUserpermissionIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotmbsUserpermissionIdentifyResponse, self).__init__()
        self._permit = None
        self._vid = None

    @property
    def permit(self):
        return self._permit

    @permit.setter
    def permit(self, value):
        self._permit = value
    @property
    def vid(self):
        return self._vid

    @vid.setter
    def vid(self, value):
        self._vid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotmbsUserpermissionIdentifyResponse, self).parse_response_content(response_content)
        if 'permit' in response:
            self.permit = response['permit']
        if 'vid' in response:
            self.vid = response['vid']

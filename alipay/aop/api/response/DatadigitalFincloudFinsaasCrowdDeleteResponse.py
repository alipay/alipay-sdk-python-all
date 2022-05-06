#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudFinsaasCrowdDeleteResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasCrowdDeleteResponse, self).__init__()
        self._msg = None

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasCrowdDeleteResponse, self).parse_response_content(response_content)
        if 'msg' in response:
            self.msg = response['msg']

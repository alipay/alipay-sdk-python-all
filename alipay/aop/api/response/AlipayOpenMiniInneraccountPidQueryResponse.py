#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInneraccountPidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInneraccountPidQueryResponse, self).__init__()
        self._pid = None

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInneraccountPidQueryResponse, self).parse_response_content(response_content)
        if 'pid' in response:
            self.pid = response['pid']

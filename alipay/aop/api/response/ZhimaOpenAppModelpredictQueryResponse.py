#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaOpenAppModelpredictQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaOpenAppModelpredictQueryResponse, self).__init__()
        self._resp = None

    @property
    def resp(self):
        return self._resp

    @resp.setter
    def resp(self, value):
        self._resp = value

    def parse_response_content(self, response_content):
        response = super(ZhimaOpenAppModelpredictQueryResponse, self).parse_response_content(response_content)
        if 'resp' in response:
            self.resp = response['resp']

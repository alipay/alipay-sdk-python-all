#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaOpenAppRisktagQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaOpenAppRisktagQueryResponse, self).__init__()
        self._resp = None

    @property
    def resp(self):
        return self._resp

    @resp.setter
    def resp(self, value):
        self._resp = value

    def parse_response_content(self, response_content):
        response = super(ZhimaOpenAppRisktagQueryResponse, self).parse_response_content(response_content)
        if 'resp' in response:
            self.resp = response['resp']

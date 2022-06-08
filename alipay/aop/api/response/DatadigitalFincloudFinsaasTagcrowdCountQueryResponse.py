#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudFinsaasTagcrowdCountQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasTagcrowdCountQueryResponse, self).__init__()
        self._crowd_count = None

    @property
    def crowd_count(self):
        return self._crowd_count

    @crowd_count.setter
    def crowd_count(self, value):
        self._crowd_count = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasTagcrowdCountQueryResponse, self).parse_response_content(response_content)
        if 'crowd_count' in response:
            self.crowd_count = response['crowd_count']

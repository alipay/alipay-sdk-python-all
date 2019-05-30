#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneEquityInstpointQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneEquityInstpointQueryResponse, self).__init__()
        self._point_score = None

    @property
    def point_score(self):
        return self._point_score

    @point_score.setter
    def point_score(self, value):
        self._point_score = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneEquityInstpointQueryResponse, self).parse_response_content(response_content)
        if 'point_score' in response:
            self.point_score = response['point_score']

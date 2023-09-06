#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserSportsrecordDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserSportsrecordDetailQueryResponse, self).__init__()
        self._geo_points = None

    @property
    def geo_points(self):
        return self._geo_points

    @geo_points.setter
    def geo_points(self, value):
        self._geo_points = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserSportsrecordDetailQueryResponse, self).parse_response_content(response_content)
        if 'geo_points' in response:
            self.geo_points = response['geo_points']

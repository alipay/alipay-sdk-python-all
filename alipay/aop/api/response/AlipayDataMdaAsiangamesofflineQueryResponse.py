#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaAsiangamesofflineQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaAsiangamesofflineQueryResponse, self).__init__()
        self._complete_route_uv = None
        self._ring_cnt = None
        self._steps_cnt = None
        self._top_5_route = None
        self._total_uv = None

    @property
    def complete_route_uv(self):
        return self._complete_route_uv

    @complete_route_uv.setter
    def complete_route_uv(self, value):
        self._complete_route_uv = value
    @property
    def ring_cnt(self):
        return self._ring_cnt

    @ring_cnt.setter
    def ring_cnt(self, value):
        self._ring_cnt = value
    @property
    def steps_cnt(self):
        return self._steps_cnt

    @steps_cnt.setter
    def steps_cnt(self, value):
        self._steps_cnt = value
    @property
    def top_5_route(self):
        return self._top_5_route

    @top_5_route.setter
    def top_5_route(self, value):
        self._top_5_route = value
    @property
    def total_uv(self):
        return self._total_uv

    @total_uv.setter
    def total_uv(self, value):
        self._total_uv = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaAsiangamesofflineQueryResponse, self).parse_response_content(response_content)
        if 'complete_route_uv' in response:
            self.complete_route_uv = response['complete_route_uv']
        if 'ring_cnt' in response:
            self.ring_cnt = response['ring_cnt']
        if 'steps_cnt' in response:
            self.steps_cnt = response['steps_cnt']
        if 'top_5_route' in response:
            self.top_5_route = response['top_5_route']
        if 'total_uv' in response:
            self.total_uv = response['total_uv']

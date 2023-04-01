#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaGreenagofflineQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaGreenagofflineQueryResponse, self).__init__()
        self._completed_cnt = None
        self._energy = None
        self._total_uv = None

    @property
    def completed_cnt(self):
        return self._completed_cnt

    @completed_cnt.setter
    def completed_cnt(self, value):
        self._completed_cnt = value
    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        self._energy = value
    @property
    def total_uv(self):
        return self._total_uv

    @total_uv.setter
    def total_uv(self, value):
        self._total_uv = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaGreenagofflineQueryResponse, self).parse_response_content(response_content)
        if 'completed_cnt' in response:
            self.completed_cnt = response['completed_cnt']
        if 'energy' in response:
            self.energy = response['energy']
        if 'total_uv' in response:
            self.total_uv = response['total_uv']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntforestPlantApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestPlantApplyResponse, self).__init__()
        self._biz_time = None
        self._certificate_id = None
        self._current_energy = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def current_energy(self):
        return self._current_energy

    @current_energy.setter
    def current_energy(self, value):
        self._current_energy = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestPlantApplyResponse, self).parse_response_content(response_content)
        if 'biz_time' in response:
            self.biz_time = response['biz_time']
        if 'certificate_id' in response:
            self.certificate_id = response['certificate_id']
        if 'current_energy' in response:
            self.current_energy = response['current_energy']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainysCompelxTypeWeakRefTwo import RainysCompelxTypeWeakRefTwo
from alipay.aop.api.domain.RainyComplexTypesTheFourteen import RainyComplexTypesTheFourteen


class AlipayDataDataserviceSchemathirtyoneRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceSchemathirtyoneRainystestQueryResponse, self).__init__()
        self._demo = None
        self._demo_empty_vv = None
        self._demo_emtpy = None
        self._demo_other = None
        self._demo_weak_ref = None
        self._outone = None

    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, value):
        self._demo = value
    @property
    def demo_empty_vv(self):
        return self._demo_empty_vv

    @demo_empty_vv.setter
    def demo_empty_vv(self, value):
        self._demo_empty_vv = value
    @property
    def demo_emtpy(self):
        return self._demo_emtpy

    @demo_emtpy.setter
    def demo_emtpy(self, value):
        self._demo_emtpy = value
    @property
    def demo_other(self):
        return self._demo_other

    @demo_other.setter
    def demo_other(self, value):
        self._demo_other = value
    @property
    def demo_weak_ref(self):
        return self._demo_weak_ref

    @demo_weak_ref.setter
    def demo_weak_ref(self, value):
        if isinstance(value, RainysCompelxTypeWeakRefTwo):
            self._demo_weak_ref = value
        else:
            self._demo_weak_ref = RainysCompelxTypeWeakRefTwo.from_alipay_dict(value)
    @property
    def outone(self):
        return self._outone

    @outone.setter
    def outone(self, value):
        if isinstance(value, RainyComplexTypesTheFourteen):
            self._outone = value
        else:
            self._outone = RainyComplexTypesTheFourteen.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceSchemathirtyoneRainystestQueryResponse, self).parse_response_content(response_content)
        if 'demo' in response:
            self.demo = response['demo']
        if 'demo_empty_vv' in response:
            self.demo_empty_vv = response['demo_empty_vv']
        if 'demo_emtpy' in response:
            self.demo_emtpy = response['demo_emtpy']
        if 'demo_other' in response:
            self.demo_other = response['demo_other']
        if 'demo_weak_ref' in response:
            self.demo_weak_ref = response['demo_weak_ref']
        if 'outone' in response:
            self.outone = response['outone']

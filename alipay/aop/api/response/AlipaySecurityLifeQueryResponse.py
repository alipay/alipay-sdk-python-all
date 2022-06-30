#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ApeRecContext import ApeRecContext


class AlipaySecurityLifeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityLifeQueryResponse, self).__init__()
        self._dsfg = None
        self._grt = None
        self._hh = None
        self._jsdfjsd = None
        self._longitude = None
        self._sdgd = None

    @property
    def dsfg(self):
        return self._dsfg

    @dsfg.setter
    def dsfg(self, value):
        if isinstance(value, list):
            self._dsfg = list()
            for i in value:
                if isinstance(i, ApeRecContext):
                    self._dsfg.append(i)
                else:
                    self._dsfg.append(ApeRecContext.from_alipay_dict(i))
    @property
    def grt(self):
        return self._grt

    @grt.setter
    def grt(self, value):
        if isinstance(value, list):
            self._grt = list()
            for i in value:
                self._grt.append(i)
    @property
    def hh(self):
        return self._hh

    @hh.setter
    def hh(self, value):
        if isinstance(value, list):
            self._hh = list()
            for i in value:
                self._hh.append(i)
    @property
    def jsdfjsd(self):
        return self._jsdfjsd

    @jsdfjsd.setter
    def jsdfjsd(self, value):
        self._jsdfjsd = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def sdgd(self):
        return self._sdgd

    @sdgd.setter
    def sdgd(self, value):
        if isinstance(value, list):
            self._sdgd = list()
            for i in value:
                self._sdgd.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityLifeQueryResponse, self).parse_response_content(response_content)
        if 'dsfg' in response:
            self.dsfg = response['dsfg']
        if 'grt' in response:
            self.grt = response['grt']
        if 'hh' in response:
            self.hh = response['hh']
        if 'jsdfjsd' in response:
            self.jsdfjsd = response['jsdfjsd']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'sdgd' in response:
            self.sdgd = response['sdgd']

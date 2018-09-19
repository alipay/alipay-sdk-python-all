#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayItemGoodsList import AlipayItemGoodsList


class AlipayDataDataexchangeSfasdfResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataexchangeSfasdfResponse, self).__init__()
        self._azxfghd = None
        self._gfdhsdasafg = None
        self._gfhjfdsa = None
        self._ghjfdsafgh = None
        self._sdvsdv = None
        self._wrty = None

    @property
    def azxfghd(self):
        return self._azxfghd

    @azxfghd.setter
    def azxfghd(self, value):
        if isinstance(value, list):
            self._azxfghd = list()
            for i in value:
                self._azxfghd.append(i)
    @property
    def gfdhsdasafg(self):
        return self._gfdhsdasafg

    @gfdhsdasafg.setter
    def gfdhsdasafg(self, value):
        if isinstance(value, list):
            self._gfdhsdasafg = list()
            for i in value:
                self._gfdhsdasafg.append(i)
    @property
    def gfhjfdsa(self):
        return self._gfhjfdsa

    @gfhjfdsa.setter
    def gfhjfdsa(self, value):
        if isinstance(value, list):
            self._gfhjfdsa = list()
            for i in value:
                self._gfhjfdsa.append(i)
    @property
    def ghjfdsafgh(self):
        return self._ghjfdsafgh

    @ghjfdsafgh.setter
    def ghjfdsafgh(self, value):
        if isinstance(value, list):
            self._ghjfdsafgh = list()
            for i in value:
                self._ghjfdsafgh.append(i)
    @property
    def sdvsdv(self):
        return self._sdvsdv

    @sdvsdv.setter
    def sdvsdv(self, value):
        self._sdvsdv = value
    @property
    def wrty(self):
        return self._wrty

    @wrty.setter
    def wrty(self, value):
        if isinstance(value, list):
            self._wrty = list()
            for i in value:
                if isinstance(i, AlipayItemGoodsList):
                    self._wrty.append(i)
                else:
                    self._wrty.append(AlipayItemGoodsList.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataexchangeSfasdfResponse, self).parse_response_content(response_content)
        if 'azxfghd' in response:
            self.azxfghd = response['azxfghd']
        if 'gfdhsdasafg' in response:
            self.gfdhsdasafg = response['gfdhsdasafg']
        if 'gfhjfdsa' in response:
            self.gfhjfdsa = response['gfhjfdsa']
        if 'ghjfdsafgh' in response:
            self.ghjfdsafgh = response['ghjfdsafgh']
        if 'sdvsdv' in response:
            self.sdvsdv = response['sdvsdv']
        if 'wrty' in response:
            self.wrty = response['wrty']

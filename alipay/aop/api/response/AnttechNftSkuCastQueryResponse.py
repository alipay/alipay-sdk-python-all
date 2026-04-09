#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftSkuCastQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftSkuCastQueryResponse, self).__init__()
        self._apply_status = None
        self._desc = None
        self._sku_id = None

    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftSkuCastQueryResponse, self).parse_response_content(response_content)
        if 'apply_status' in response:
            self.apply_status = response['apply_status']
        if 'desc' in response:
            self.desc = response['desc']
        if 'sku_id' in response:
            self.sku_id = response['sku_id']

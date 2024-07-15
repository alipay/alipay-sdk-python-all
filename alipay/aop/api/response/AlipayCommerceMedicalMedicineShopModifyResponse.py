#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMedicineShopModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMedicineShopModifyResponse, self).__init__()
        self._apply_id = None
        self._out_store_id = None
        self._shop_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def out_store_id(self):
        return self._out_store_id

    @out_store_id.setter
    def out_store_id(self, value):
        self._out_store_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMedicineShopModifyResponse, self).parse_response_content(response_content)
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
        if 'out_store_id' in response:
            self.out_store_id = response['out_store_id']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']

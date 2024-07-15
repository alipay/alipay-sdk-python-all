#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMedicineShopCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMedicineShopCreateResponse, self).__init__()
        self._apply_id = None
        self._exist_shop_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def exist_shop_id(self):
        return self._exist_shop_id

    @exist_shop_id.setter
    def exist_shop_id(self, value):
        self._exist_shop_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMedicineShopCreateResponse, self).parse_response_content(response_content)
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
        if 'exist_shop_id' in response:
            self.exist_shop_id = response['exist_shop_id']

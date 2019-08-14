#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AdMaterialInfo import AdMaterialInfo


class AlipayCommerceIotAdvertiserMaterialBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotAdvertiserMaterialBatchqueryResponse, self).__init__()
        self._material_infos = None
        self._total = None

    @property
    def material_infos(self):
        return self._material_infos

    @material_infos.setter
    def material_infos(self, value):
        if isinstance(value, list):
            self._material_infos = list()
            for i in value:
                if isinstance(i, AdMaterialInfo):
                    self._material_infos.append(i)
                else:
                    self._material_infos.append(AdMaterialInfo.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotAdvertiserMaterialBatchqueryResponse, self).parse_response_content(response_content)
        if 'material_infos' in response:
            self.material_infos = response['material_infos']
        if 'total' in response:
            self.total = response['total']

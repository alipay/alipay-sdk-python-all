#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PharmacistVO import PharmacistVO


class AlipayCommerceMedicalStorePharmacistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalStorePharmacistQueryResponse, self).__init__()
        self._pharmacists = None
        self._total = None

    @property
    def pharmacists(self):
        return self._pharmacists

    @pharmacists.setter
    def pharmacists(self, value):
        if isinstance(value, list):
            self._pharmacists = list()
            for i in value:
                if isinstance(i, PharmacistVO):
                    self._pharmacists.append(i)
                else:
                    self._pharmacists.append(PharmacistVO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalStorePharmacistQueryResponse, self).parse_response_content(response_content)
        if 'pharmacists' in response:
            self.pharmacists = response['pharmacists']
        if 'total' in response:
            self.total = response['total']

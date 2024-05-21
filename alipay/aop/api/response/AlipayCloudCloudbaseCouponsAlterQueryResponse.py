#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Coupons import Coupons


class AlipayCloudCloudbaseCouponsAlterQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseCouponsAlterQueryResponse, self).__init__()
        self._coupons = None

    @property
    def coupons(self):
        return self._coupons

    @coupons.setter
    def coupons(self, value):
        if isinstance(value, list):
            self._coupons = list()
            for i in value:
                if isinstance(i, Coupons):
                    self._coupons.append(i)
                else:
                    self._coupons.append(Coupons.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseCouponsAlterQueryResponse, self).parse_response_content(response_content)
        if 'coupons' in response:
            self.coupons = response['coupons']

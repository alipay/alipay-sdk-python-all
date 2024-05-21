#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Coupons import Coupons


class AlipayCloudCloudbaseCouponsRenewQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseCouponsRenewQueryResponse, self).__init__()
        self._coupons = None

    @property
    def coupons(self):
        return self._coupons

    @coupons.setter
    def coupons(self, value):
        if isinstance(value, Coupons):
            self._coupons = value
        else:
            self._coupons = Coupons.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseCouponsRenewQueryResponse, self).parse_response_content(response_content)
        if 'coupons' in response:
            self.coupons = response['coupons']

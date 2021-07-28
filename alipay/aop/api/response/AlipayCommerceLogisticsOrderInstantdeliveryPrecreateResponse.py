#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PreCreateWaybillIstd import PreCreateWaybillIstd


class AlipayCommerceLogisticsOrderInstantdeliveryPrecreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsOrderInstantdeliveryPrecreateResponse, self).__init__()
        self._waybills = None

    @property
    def waybills(self):
        return self._waybills

    @waybills.setter
    def waybills(self, value):
        if isinstance(value, list):
            self._waybills = list()
            for i in value:
                if isinstance(i, PreCreateWaybillIstd):
                    self._waybills.append(i)
                else:
                    self._waybills.append(PreCreateWaybillIstd.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsOrderInstantdeliveryPrecreateResponse, self).parse_response_content(response_content)
        if 'waybills' in response:
            self.waybills = response['waybills']

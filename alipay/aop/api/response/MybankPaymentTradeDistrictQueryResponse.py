#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.District import District


class MybankPaymentTradeDistrictQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeDistrictQueryResponse, self).__init__()
        self._district_details = None

    @property
    def district_details(self):
        return self._district_details

    @district_details.setter
    def district_details(self, value):
        if isinstance(value, list):
            self._district_details = list()
            for i in value:
                if isinstance(i, District):
                    self._district_details.append(i)
                else:
                    self._district_details.append(District.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeDistrictQueryResponse, self).parse_response_content(response_content)
        if 'district_details' in response:
            self.district_details = response['district_details']

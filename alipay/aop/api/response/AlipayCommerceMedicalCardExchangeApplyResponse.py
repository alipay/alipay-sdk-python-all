#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MemberCouponCodeDTO import MemberCouponCodeDTO


class AlipayCommerceMedicalCardExchangeApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCardExchangeApplyResponse, self).__init__()
        self._coupon_code_list = None

    @property
    def coupon_code_list(self):
        return self._coupon_code_list

    @coupon_code_list.setter
    def coupon_code_list(self, value):
        if isinstance(value, list):
            self._coupon_code_list = list()
            for i in value:
                if isinstance(i, MemberCouponCodeDTO):
                    self._coupon_code_list.append(i)
                else:
                    self._coupon_code_list.append(MemberCouponCodeDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCardExchangeApplyResponse, self).parse_response_content(response_content)
        if 'coupon_code_list' in response:
            self.coupon_code_list = response['coupon_code_list']

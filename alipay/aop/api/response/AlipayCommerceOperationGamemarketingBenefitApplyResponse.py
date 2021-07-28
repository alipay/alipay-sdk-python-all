#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationGamemarketingBenefitApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationGamemarketingBenefitApplyResponse, self).__init__()
        self._apply_voucher_code_list = None

    @property
    def apply_voucher_code_list(self):
        return self._apply_voucher_code_list

    @apply_voucher_code_list.setter
    def apply_voucher_code_list(self, value):
        if isinstance(value, list):
            self._apply_voucher_code_list = list()
            for i in value:
                self._apply_voucher_code_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationGamemarketingBenefitApplyResponse, self).parse_response_content(response_content)
        if 'apply_voucher_code_list' in response:
            self.apply_voucher_code_list = response['apply_voucher_code_list']

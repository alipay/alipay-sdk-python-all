#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherConsultInfo import VoucherConsultInfo


class AlipayCommerceVoucherResultConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceVoucherResultConsultResponse, self).__init__()
        self._optimal_total_promo_amount = None
        self._voucher_consult_list = None

    @property
    def optimal_total_promo_amount(self):
        return self._optimal_total_promo_amount

    @optimal_total_promo_amount.setter
    def optimal_total_promo_amount(self, value):
        self._optimal_total_promo_amount = value
    @property
    def voucher_consult_list(self):
        return self._voucher_consult_list

    @voucher_consult_list.setter
    def voucher_consult_list(self, value):
        if isinstance(value, list):
            self._voucher_consult_list = list()
            for i in value:
                if isinstance(i, VoucherConsultInfo):
                    self._voucher_consult_list.append(i)
                else:
                    self._voucher_consult_list.append(VoucherConsultInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceVoucherResultConsultResponse, self).parse_response_content(response_content)
        if 'optimal_total_promo_amount' in response:
            self.optimal_total_promo_amount = response['optimal_total_promo_amount']
        if 'voucher_consult_list' in response:
            self.voucher_consult_list = response['voucher_consult_list']

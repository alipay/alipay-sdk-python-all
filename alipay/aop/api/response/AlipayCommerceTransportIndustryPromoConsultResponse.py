#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BizVoucherConsultInfo import BizVoucherConsultInfo


class AlipayCommerceTransportIndustryPromoConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportIndustryPromoConsultResponse, self).__init__()
        self._voucher_consult_list = None

    @property
    def voucher_consult_list(self):
        return self._voucher_consult_list

    @voucher_consult_list.setter
    def voucher_consult_list(self, value):
        if isinstance(value, list):
            self._voucher_consult_list = list()
            for i in value:
                if isinstance(i, BizVoucherConsultInfo):
                    self._voucher_consult_list.append(i)
                else:
                    self._voucher_consult_list.append(BizVoucherConsultInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportIndustryPromoConsultResponse, self).parse_response_content(response_content)
        if 'voucher_consult_list' in response:
            self.voucher_consult_list = response['voucher_consult_list']

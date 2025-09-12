#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BenefitAccountFsFundInfoDTO import BenefitAccountFsFundInfoDTO


class AlipayMarketingBenefitaccountAccountRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingBenefitaccountAccountRefundResponse, self).__init__()
        self._amount = None
        self._fund_infos = None
        self._order_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def fund_infos(self):
        return self._fund_infos

    @fund_infos.setter
    def fund_infos(self, value):
        if isinstance(value, BenefitAccountFsFundInfoDTO):
            self._fund_infos = value
        else:
            self._fund_infos = BenefitAccountFsFundInfoDTO.from_alipay_dict(value)
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingBenefitaccountAccountRefundResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'fund_infos' in response:
            self.fund_infos = response['fund_infos']
        if 'order_no' in response:
            self.order_no = response['order_no']

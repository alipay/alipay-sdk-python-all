#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MemberCardRefundDetail import MemberCardRefundDetail


class AntMerchantExpandMembercardRefundConsultResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandMembercardRefundConsultResponse, self).__init__()
        self._details = None
        self._refund_total_amount = None
        self._refund_total_benefit_amount = None
        self._refund_total_discount_amount = None
        self._refund_total_voucher_amount = None
        self._total_balance = None
        self._total_principal_balance = None

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        if isinstance(value, list):
            self._details = list()
            for i in value:
                if isinstance(i, MemberCardRefundDetail):
                    self._details.append(i)
                else:
                    self._details.append(MemberCardRefundDetail.from_alipay_dict(i))
    @property
    def refund_total_amount(self):
        return self._refund_total_amount

    @refund_total_amount.setter
    def refund_total_amount(self, value):
        self._refund_total_amount = value
    @property
    def refund_total_benefit_amount(self):
        return self._refund_total_benefit_amount

    @refund_total_benefit_amount.setter
    def refund_total_benefit_amount(self, value):
        self._refund_total_benefit_amount = value
    @property
    def refund_total_discount_amount(self):
        return self._refund_total_discount_amount

    @refund_total_discount_amount.setter
    def refund_total_discount_amount(self, value):
        self._refund_total_discount_amount = value
    @property
    def refund_total_voucher_amount(self):
        return self._refund_total_voucher_amount

    @refund_total_voucher_amount.setter
    def refund_total_voucher_amount(self, value):
        self._refund_total_voucher_amount = value
    @property
    def total_balance(self):
        return self._total_balance

    @total_balance.setter
    def total_balance(self, value):
        self._total_balance = value
    @property
    def total_principal_balance(self):
        return self._total_principal_balance

    @total_principal_balance.setter
    def total_principal_balance(self, value):
        self._total_principal_balance = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandMembercardRefundConsultResponse, self).parse_response_content(response_content)
        if 'details' in response:
            self.details = response['details']
        if 'refund_total_amount' in response:
            self.refund_total_amount = response['refund_total_amount']
        if 'refund_total_benefit_amount' in response:
            self.refund_total_benefit_amount = response['refund_total_benefit_amount']
        if 'refund_total_discount_amount' in response:
            self.refund_total_discount_amount = response['refund_total_discount_amount']
        if 'refund_total_voucher_amount' in response:
            self.refund_total_voucher_amount = response['refund_total_voucher_amount']
        if 'total_balance' in response:
            self.total_balance = response['total_balance']
        if 'total_principal_balance' in response:
            self.total_principal_balance = response['total_principal_balance']

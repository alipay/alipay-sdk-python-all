#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BalanceAccountDetail import BalanceAccountDetail
from alipay.aop.api.domain.ExtCardInfo import ExtCardInfo


class AlipayFundAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAccountQueryResponse, self).__init__()
        self._amount_detail = None
        self._available_amount = None
        self._ext_card_info = None
        self._freeze_amount = None
        self._total_amount = None

    @property
    def amount_detail(self):
        return self._amount_detail

    @amount_detail.setter
    def amount_detail(self, value):
        if isinstance(value, BalanceAccountDetail):
            self._amount_detail = value
        else:
            self._amount_detail = BalanceAccountDetail.from_alipay_dict(value)
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def ext_card_info(self):
        return self._ext_card_info

    @ext_card_info.setter
    def ext_card_info(self, value):
        if isinstance(value, ExtCardInfo):
            self._ext_card_info = value
        else:
            self._ext_card_info = ExtCardInfo.from_alipay_dict(value)
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAccountQueryResponse, self).parse_response_content(response_content)
        if 'amount_detail' in response:
            self.amount_detail = response['amount_detail']
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'ext_card_info' in response:
            self.ext_card_info = response['ext_card_info']
        if 'freeze_amount' in response:
            self.freeze_amount = response['freeze_amount']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']

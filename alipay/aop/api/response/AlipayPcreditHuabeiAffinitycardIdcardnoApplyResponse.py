#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiAffinitycardIdcardnoApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiAffinitycardIdcardnoApplyResponse, self).__init__()
        self._alipay_user_id = None
        self._available_amount = None
        self._repay_date = None
        self._total_amount = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def repay_date(self):
        return self._repay_date

    @repay_date.setter
    def repay_date(self, value):
        self._repay_date = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiAffinitycardIdcardnoApplyResponse, self).parse_response_content(response_content)
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'repay_date' in response:
            self.repay_date = response['repay_date']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanCommissionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanCommissionQueryResponse, self).__init__()
        self._activity_commission_amt = None
        self._activity_commission_rank = None
        self._activity_period = None
        self._enterprise_id = None
        self._store_id = None
        self._user_id = None

    @property
    def activity_commission_amt(self):
        return self._activity_commission_amt

    @activity_commission_amt.setter
    def activity_commission_amt(self, value):
        self._activity_commission_amt = value
    @property
    def activity_commission_rank(self):
        return self._activity_commission_rank

    @activity_commission_rank.setter
    def activity_commission_rank(self, value):
        self._activity_commission_rank = value
    @property
    def activity_period(self):
        return self._activity_period

    @activity_period.setter
    def activity_period(self, value):
        self._activity_period = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanCommissionQueryResponse, self).parse_response_content(response_content)
        if 'activity_commission_amt' in response:
            self.activity_commission_amt = response['activity_commission_amt']
        if 'activity_commission_rank' in response:
            self.activity_commission_rank = response['activity_commission_rank']
        if 'activity_period' in response:
            self.activity_period = response['activity_period']
        if 'enterprise_id' in response:
            self.enterprise_id = response['enterprise_id']
        if 'store_id' in response:
            self.store_id = response['store_id']
        if 'user_id' in response:
            self.user_id = response['user_id']

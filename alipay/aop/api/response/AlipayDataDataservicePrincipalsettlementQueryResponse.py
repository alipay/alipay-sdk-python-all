#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SettlementDailyDetail import SettlementDailyDetail


class AlipayDataDataservicePrincipalsettlementQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataservicePrincipalsettlementQueryResponse, self).__init__()
        self._advertiser_pid = None
        self._principal_id = None
        self._principal_pid = None
        self._settlement_amount = None
        self._settlement_date_list = None
        self._settlement_month = None
        self._type = None

    @property
    def advertiser_pid(self):
        return self._advertiser_pid

    @advertiser_pid.setter
    def advertiser_pid(self, value):
        self._advertiser_pid = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_pid(self):
        return self._principal_pid

    @principal_pid.setter
    def principal_pid(self, value):
        self._principal_pid = value
    @property
    def settlement_amount(self):
        return self._settlement_amount

    @settlement_amount.setter
    def settlement_amount(self, value):
        self._settlement_amount = value
    @property
    def settlement_date_list(self):
        return self._settlement_date_list

    @settlement_date_list.setter
    def settlement_date_list(self, value):
        if isinstance(value, list):
            self._settlement_date_list = list()
            for i in value:
                if isinstance(i, SettlementDailyDetail):
                    self._settlement_date_list.append(i)
                else:
                    self._settlement_date_list.append(SettlementDailyDetail.from_alipay_dict(i))
    @property
    def settlement_month(self):
        return self._settlement_month

    @settlement_month.setter
    def settlement_month(self, value):
        self._settlement_month = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataservicePrincipalsettlementQueryResponse, self).parse_response_content(response_content)
        if 'advertiser_pid' in response:
            self.advertiser_pid = response['advertiser_pid']
        if 'principal_id' in response:
            self.principal_id = response['principal_id']
        if 'principal_pid' in response:
            self.principal_pid = response['principal_pid']
        if 'settlement_amount' in response:
            self.settlement_amount = response['settlement_amount']
        if 'settlement_date_list' in response:
            self.settlement_date_list = response['settlement_date_list']
        if 'settlement_month' in response:
            self.settlement_month = response['settlement_month']
        if 'type' in response:
            self.type = response['type']

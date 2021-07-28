#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiMerchantActivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiMerchantActivityQueryResponse, self).__init__()
        self._account_id = None
        self._aggr_id = None
        self._fund_type = None
        self._status = None
        self._subsidy_scope = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def aggr_id(self):
        return self._aggr_id

    @aggr_id.setter
    def aggr_id(self, value):
        self._aggr_id = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def subsidy_scope(self):
        return self._subsidy_scope

    @subsidy_scope.setter
    def subsidy_scope(self, value):
        self._subsidy_scope = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiMerchantActivityQueryResponse, self).parse_response_content(response_content)
        if 'account_id' in response:
            self.account_id = response['account_id']
        if 'aggr_id' in response:
            self.aggr_id = response['aggr_id']
        if 'fund_type' in response:
            self.fund_type = response['fund_type']
        if 'status' in response:
            self.status = response['status']
        if 'subsidy_scope' in response:
            self.subsidy_scope = response['subsidy_scope']

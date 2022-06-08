#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundEnterprisepayGroupQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundEnterprisepayGroupQueryResponse, self).__init__()
        self._account_id = None
        self._fund_group_id = None
        self._fund_identity = None
        self._group_name = None
        self._out_group_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def fund_group_id(self):
        return self._fund_group_id

    @fund_group_id.setter
    def fund_group_id(self, value):
        self._fund_group_id = value
    @property
    def fund_identity(self):
        return self._fund_identity

    @fund_identity.setter
    def fund_identity(self, value):
        self._fund_identity = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def out_group_id(self):
        return self._out_group_id

    @out_group_id.setter
    def out_group_id(self, value):
        self._out_group_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundEnterprisepayGroupQueryResponse, self).parse_response_content(response_content)
        if 'account_id' in response:
            self.account_id = response['account_id']
        if 'fund_group_id' in response:
            self.fund_group_id = response['fund_group_id']
        if 'fund_identity' in response:
            self.fund_identity = response['fund_identity']
        if 'group_name' in response:
            self.group_name = response['group_name']
        if 'out_group_id' in response:
            self.out_group_id = response['out_group_id']

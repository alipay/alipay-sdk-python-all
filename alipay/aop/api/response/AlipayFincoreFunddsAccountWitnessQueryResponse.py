#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFincoreFunddsAccountWitnessQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreFunddsAccountWitnessQueryResponse, self).__init__()
        self._account_no = None
        self._account_status = None
        self._account_type = None
        self._available_balance = None
        self._balance = None
        self._external_entity_id = None
        self._freeze_balance = None
        self._gmt_create = None
        self._gmt_modified = None
        self._user_id = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_status(self):
        return self._account_status

    @account_status.setter
    def account_status(self, value):
        self._account_status = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def available_balance(self):
        return self._available_balance

    @available_balance.setter
    def available_balance(self, value):
        self._available_balance = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def external_entity_id(self):
        return self._external_entity_id

    @external_entity_id.setter
    def external_entity_id(self, value):
        self._external_entity_id = value
    @property
    def freeze_balance(self):
        return self._freeze_balance

    @freeze_balance.setter
    def freeze_balance(self, value):
        self._freeze_balance = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreFunddsAccountWitnessQueryResponse, self).parse_response_content(response_content)
        if 'account_no' in response:
            self.account_no = response['account_no']
        if 'account_status' in response:
            self.account_status = response['account_status']
        if 'account_type' in response:
            self.account_type = response['account_type']
        if 'available_balance' in response:
            self.available_balance = response['available_balance']
        if 'balance' in response:
            self.balance = response['balance']
        if 'external_entity_id' in response:
            self.external_entity_id = response['external_entity_id']
        if 'freeze_balance' in response:
            self.freeze_balance = response['freeze_balance']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'user_id' in response:
            self.user_id = response['user_id']

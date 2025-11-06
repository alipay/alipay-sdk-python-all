#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcFundSignApplyModel(object):

    def __init__(self):
        self._account_type = None
        self._enterprise_id = None
        self._fund_account_type = None
        self._fund_source = None
        self._identity_verify = None
        self._sign_terminal = None
        self._signer_category = None
        self._specified_bank_card_no = None
        self._use_creator_alipay_account = None

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def fund_account_type(self):
        return self._fund_account_type

    @fund_account_type.setter
    def fund_account_type(self, value):
        self._fund_account_type = value
    @property
    def fund_source(self):
        return self._fund_source

    @fund_source.setter
    def fund_source(self, value):
        self._fund_source = value
    @property
    def identity_verify(self):
        return self._identity_verify

    @identity_verify.setter
    def identity_verify(self, value):
        self._identity_verify = value
    @property
    def sign_terminal(self):
        return self._sign_terminal

    @sign_terminal.setter
    def sign_terminal(self, value):
        self._sign_terminal = value
    @property
    def signer_category(self):
        return self._signer_category

    @signer_category.setter
    def signer_category(self, value):
        self._signer_category = value
    @property
    def specified_bank_card_no(self):
        return self._specified_bank_card_no

    @specified_bank_card_no.setter
    def specified_bank_card_no(self, value):
        self._specified_bank_card_no = value
    @property
    def use_creator_alipay_account(self):
        return self._use_creator_alipay_account

    @use_creator_alipay_account.setter
    def use_creator_alipay_account(self, value):
        self._use_creator_alipay_account = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.fund_account_type:
            if hasattr(self.fund_account_type, 'to_alipay_dict'):
                params['fund_account_type'] = self.fund_account_type.to_alipay_dict()
            else:
                params['fund_account_type'] = self.fund_account_type
        if self.fund_source:
            if hasattr(self.fund_source, 'to_alipay_dict'):
                params['fund_source'] = self.fund_source.to_alipay_dict()
            else:
                params['fund_source'] = self.fund_source
        if self.identity_verify:
            if hasattr(self.identity_verify, 'to_alipay_dict'):
                params['identity_verify'] = self.identity_verify.to_alipay_dict()
            else:
                params['identity_verify'] = self.identity_verify
        if self.sign_terminal:
            if hasattr(self.sign_terminal, 'to_alipay_dict'):
                params['sign_terminal'] = self.sign_terminal.to_alipay_dict()
            else:
                params['sign_terminal'] = self.sign_terminal
        if self.signer_category:
            if hasattr(self.signer_category, 'to_alipay_dict'):
                params['signer_category'] = self.signer_category.to_alipay_dict()
            else:
                params['signer_category'] = self.signer_category
        if self.specified_bank_card_no:
            if hasattr(self.specified_bank_card_no, 'to_alipay_dict'):
                params['specified_bank_card_no'] = self.specified_bank_card_no.to_alipay_dict()
            else:
                params['specified_bank_card_no'] = self.specified_bank_card_no
        if self.use_creator_alipay_account:
            if hasattr(self.use_creator_alipay_account, 'to_alipay_dict'):
                params['use_creator_alipay_account'] = self.use_creator_alipay_account.to_alipay_dict()
            else:
                params['use_creator_alipay_account'] = self.use_creator_alipay_account
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcFundSignApplyModel()
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'fund_account_type' in d:
            o.fund_account_type = d['fund_account_type']
        if 'fund_source' in d:
            o.fund_source = d['fund_source']
        if 'identity_verify' in d:
            o.identity_verify = d['identity_verify']
        if 'sign_terminal' in d:
            o.sign_terminal = d['sign_terminal']
        if 'signer_category' in d:
            o.signer_category = d['signer_category']
        if 'specified_bank_card_no' in d:
            o.specified_bank_card_no = d['specified_bank_card_no']
        if 'use_creator_alipay_account' in d:
            o.use_creator_alipay_account = d['use_creator_alipay_account']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeServiceFundWithdrawModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._amount = None
        self._biz_type = None
        self._out_biz_no = None
        self._sub_biz_type = None
        self._withdraw_account_name = None
        self._withdraw_account_no = None
        self._withdraw_bank_branch_code = None
        self._withdraw_bank_inst_id = None
        self._withdraw_card_type = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def withdraw_account_name(self):
        return self._withdraw_account_name

    @withdraw_account_name.setter
    def withdraw_account_name(self, value):
        self._withdraw_account_name = value
    @property
    def withdraw_account_no(self):
        return self._withdraw_account_no

    @withdraw_account_no.setter
    def withdraw_account_no(self, value):
        self._withdraw_account_no = value
    @property
    def withdraw_bank_branch_code(self):
        return self._withdraw_bank_branch_code

    @withdraw_bank_branch_code.setter
    def withdraw_bank_branch_code(self, value):
        self._withdraw_bank_branch_code = value
    @property
    def withdraw_bank_inst_id(self):
        return self._withdraw_bank_inst_id

    @withdraw_bank_inst_id.setter
    def withdraw_bank_inst_id(self, value):
        self._withdraw_bank_inst_id = value
    @property
    def withdraw_card_type(self):
        return self._withdraw_card_type

    @withdraw_card_type.setter
    def withdraw_card_type(self, value):
        self._withdraw_card_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        if self.withdraw_account_name:
            if hasattr(self.withdraw_account_name, 'to_alipay_dict'):
                params['withdraw_account_name'] = self.withdraw_account_name.to_alipay_dict()
            else:
                params['withdraw_account_name'] = self.withdraw_account_name
        if self.withdraw_account_no:
            if hasattr(self.withdraw_account_no, 'to_alipay_dict'):
                params['withdraw_account_no'] = self.withdraw_account_no.to_alipay_dict()
            else:
                params['withdraw_account_no'] = self.withdraw_account_no
        if self.withdraw_bank_branch_code:
            if hasattr(self.withdraw_bank_branch_code, 'to_alipay_dict'):
                params['withdraw_bank_branch_code'] = self.withdraw_bank_branch_code.to_alipay_dict()
            else:
                params['withdraw_bank_branch_code'] = self.withdraw_bank_branch_code
        if self.withdraw_bank_inst_id:
            if hasattr(self.withdraw_bank_inst_id, 'to_alipay_dict'):
                params['withdraw_bank_inst_id'] = self.withdraw_bank_inst_id.to_alipay_dict()
            else:
                params['withdraw_bank_inst_id'] = self.withdraw_bank_inst_id
        if self.withdraw_card_type:
            if hasattr(self.withdraw_card_type, 'to_alipay_dict'):
                params['withdraw_card_type'] = self.withdraw_card_type.to_alipay_dict()
            else:
                params['withdraw_card_type'] = self.withdraw_card_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeServiceFundWithdrawModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'withdraw_account_name' in d:
            o.withdraw_account_name = d['withdraw_account_name']
        if 'withdraw_account_no' in d:
            o.withdraw_account_no = d['withdraw_account_no']
        if 'withdraw_bank_branch_code' in d:
            o.withdraw_bank_branch_code = d['withdraw_bank_branch_code']
        if 'withdraw_bank_inst_id' in d:
            o.withdraw_bank_inst_id = d['withdraw_bank_inst_id']
        if 'withdraw_card_type' in d:
            o.withdraw_card_type = d['withdraw_card_type']
        return o



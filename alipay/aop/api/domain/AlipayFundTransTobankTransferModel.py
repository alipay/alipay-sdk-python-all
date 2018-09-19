#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransTobankTransferModel(object):

    def __init__(self):
        self._amount = None
        self._memo = None
        self._out_biz_no = None
        self._payee_account_name = None
        self._payee_account_type = None
        self._payee_bank_code = None
        self._payee_card_no = None
        self._payee_inst_branch_name = None
        self._payee_inst_city = None
        self._payee_inst_name = None
        self._payee_inst_province = None
        self._payer_real_name = None
        self._remark = None
        self._time_liness = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def payee_account_name(self):
        return self._payee_account_name

    @payee_account_name.setter
    def payee_account_name(self, value):
        self._payee_account_name = value
    @property
    def payee_account_type(self):
        return self._payee_account_type

    @payee_account_type.setter
    def payee_account_type(self, value):
        self._payee_account_type = value
    @property
    def payee_bank_code(self):
        return self._payee_bank_code

    @payee_bank_code.setter
    def payee_bank_code(self, value):
        self._payee_bank_code = value
    @property
    def payee_card_no(self):
        return self._payee_card_no

    @payee_card_no.setter
    def payee_card_no(self, value):
        self._payee_card_no = value
    @property
    def payee_inst_branch_name(self):
        return self._payee_inst_branch_name

    @payee_inst_branch_name.setter
    def payee_inst_branch_name(self, value):
        self._payee_inst_branch_name = value
    @property
    def payee_inst_city(self):
        return self._payee_inst_city

    @payee_inst_city.setter
    def payee_inst_city(self, value):
        self._payee_inst_city = value
    @property
    def payee_inst_name(self):
        return self._payee_inst_name

    @payee_inst_name.setter
    def payee_inst_name(self, value):
        self._payee_inst_name = value
    @property
    def payee_inst_province(self):
        return self._payee_inst_province

    @payee_inst_province.setter
    def payee_inst_province(self, value):
        self._payee_inst_province = value
    @property
    def payer_real_name(self):
        return self._payer_real_name

    @payer_real_name.setter
    def payer_real_name(self, value):
        self._payer_real_name = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def time_liness(self):
        return self._time_liness

    @time_liness.setter
    def time_liness(self, value):
        self._time_liness = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.payee_account_name:
            if hasattr(self.payee_account_name, 'to_alipay_dict'):
                params['payee_account_name'] = self.payee_account_name.to_alipay_dict()
            else:
                params['payee_account_name'] = self.payee_account_name
        if self.payee_account_type:
            if hasattr(self.payee_account_type, 'to_alipay_dict'):
                params['payee_account_type'] = self.payee_account_type.to_alipay_dict()
            else:
                params['payee_account_type'] = self.payee_account_type
        if self.payee_bank_code:
            if hasattr(self.payee_bank_code, 'to_alipay_dict'):
                params['payee_bank_code'] = self.payee_bank_code.to_alipay_dict()
            else:
                params['payee_bank_code'] = self.payee_bank_code
        if self.payee_card_no:
            if hasattr(self.payee_card_no, 'to_alipay_dict'):
                params['payee_card_no'] = self.payee_card_no.to_alipay_dict()
            else:
                params['payee_card_no'] = self.payee_card_no
        if self.payee_inst_branch_name:
            if hasattr(self.payee_inst_branch_name, 'to_alipay_dict'):
                params['payee_inst_branch_name'] = self.payee_inst_branch_name.to_alipay_dict()
            else:
                params['payee_inst_branch_name'] = self.payee_inst_branch_name
        if self.payee_inst_city:
            if hasattr(self.payee_inst_city, 'to_alipay_dict'):
                params['payee_inst_city'] = self.payee_inst_city.to_alipay_dict()
            else:
                params['payee_inst_city'] = self.payee_inst_city
        if self.payee_inst_name:
            if hasattr(self.payee_inst_name, 'to_alipay_dict'):
                params['payee_inst_name'] = self.payee_inst_name.to_alipay_dict()
            else:
                params['payee_inst_name'] = self.payee_inst_name
        if self.payee_inst_province:
            if hasattr(self.payee_inst_province, 'to_alipay_dict'):
                params['payee_inst_province'] = self.payee_inst_province.to_alipay_dict()
            else:
                params['payee_inst_province'] = self.payee_inst_province
        if self.payer_real_name:
            if hasattr(self.payer_real_name, 'to_alipay_dict'):
                params['payer_real_name'] = self.payer_real_name.to_alipay_dict()
            else:
                params['payer_real_name'] = self.payer_real_name
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.time_liness:
            if hasattr(self.time_liness, 'to_alipay_dict'):
                params['time_liness'] = self.time_liness.to_alipay_dict()
            else:
                params['time_liness'] = self.time_liness
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransTobankTransferModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payee_account_name' in d:
            o.payee_account_name = d['payee_account_name']
        if 'payee_account_type' in d:
            o.payee_account_type = d['payee_account_type']
        if 'payee_bank_code' in d:
            o.payee_bank_code = d['payee_bank_code']
        if 'payee_card_no' in d:
            o.payee_card_no = d['payee_card_no']
        if 'payee_inst_branch_name' in d:
            o.payee_inst_branch_name = d['payee_inst_branch_name']
        if 'payee_inst_city' in d:
            o.payee_inst_city = d['payee_inst_city']
        if 'payee_inst_name' in d:
            o.payee_inst_name = d['payee_inst_name']
        if 'payee_inst_province' in d:
            o.payee_inst_province = d['payee_inst_province']
        if 'payer_real_name' in d:
            o.payer_real_name = d['payer_real_name']
        if 'remark' in d:
            o.remark = d['remark']
        if 'time_liness' in d:
            o.time_liness = d['time_liness']
        return o



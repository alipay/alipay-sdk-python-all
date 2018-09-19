#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransToaccountTransferModel(object):

    def __init__(self):
        self._amount = None
        self._ext_param = None
        self._out_biz_no = None
        self._payee_account = None
        self._payee_real_name = None
        self._payee_type = None
        self._payer_real_name = None
        self._payer_show_name = None
        self._remark = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        self._payee_account = value
    @property
    def payee_real_name(self):
        return self._payee_real_name

    @payee_real_name.setter
    def payee_real_name(self, value):
        self._payee_real_name = value
    @property
    def payee_type(self):
        return self._payee_type

    @payee_type.setter
    def payee_type(self, value):
        self._payee_type = value
    @property
    def payer_real_name(self):
        return self._payer_real_name

    @payer_real_name.setter
    def payer_real_name(self, value):
        self._payer_real_name = value
    @property
    def payer_show_name(self):
        return self._payer_show_name

    @payer_show_name.setter
    def payer_show_name(self, value):
        self._payer_show_name = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.payee_account:
            if hasattr(self.payee_account, 'to_alipay_dict'):
                params['payee_account'] = self.payee_account.to_alipay_dict()
            else:
                params['payee_account'] = self.payee_account
        if self.payee_real_name:
            if hasattr(self.payee_real_name, 'to_alipay_dict'):
                params['payee_real_name'] = self.payee_real_name.to_alipay_dict()
            else:
                params['payee_real_name'] = self.payee_real_name
        if self.payee_type:
            if hasattr(self.payee_type, 'to_alipay_dict'):
                params['payee_type'] = self.payee_type.to_alipay_dict()
            else:
                params['payee_type'] = self.payee_type
        if self.payer_real_name:
            if hasattr(self.payer_real_name, 'to_alipay_dict'):
                params['payer_real_name'] = self.payer_real_name.to_alipay_dict()
            else:
                params['payer_real_name'] = self.payer_real_name
        if self.payer_show_name:
            if hasattr(self.payer_show_name, 'to_alipay_dict'):
                params['payer_show_name'] = self.payer_show_name.to_alipay_dict()
            else:
                params['payer_show_name'] = self.payer_show_name
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransToaccountTransferModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payee_account' in d:
            o.payee_account = d['payee_account']
        if 'payee_real_name' in d:
            o.payee_real_name = d['payee_real_name']
        if 'payee_type' in d:
            o.payee_type = d['payee_type']
        if 'payer_real_name' in d:
            o.payer_real_name = d['payer_real_name']
        if 'payer_show_name' in d:
            o.payer_show_name = d['payer_show_name']
        if 'remark' in d:
            o.remark = d['remark']
        return o



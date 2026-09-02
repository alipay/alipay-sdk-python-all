#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceBiztransferSubmitModel(object):

    def __init__(self):
        self._company_account_id = None
        self._out_biz_transfer_id = None
        self._payee_account = None
        self._payee_account_type = None
        self._payee_name = None
        self._recycling_order_id = None
        self._tax_no = None
        self._transfer_biz_amount = None
        self._transfer_biz_type = None

    @property
    def company_account_id(self):
        return self._company_account_id

    @company_account_id.setter
    def company_account_id(self, value):
        self._company_account_id = value
    @property
    def out_biz_transfer_id(self):
        return self._out_biz_transfer_id

    @out_biz_transfer_id.setter
    def out_biz_transfer_id(self, value):
        self._out_biz_transfer_id = value
    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        self._payee_account = value
    @property
    def payee_account_type(self):
        return self._payee_account_type

    @payee_account_type.setter
    def payee_account_type(self, value):
        self._payee_account_type = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def recycling_order_id(self):
        return self._recycling_order_id

    @recycling_order_id.setter
    def recycling_order_id(self, value):
        self._recycling_order_id = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def transfer_biz_amount(self):
        return self._transfer_biz_amount

    @transfer_biz_amount.setter
    def transfer_biz_amount(self, value):
        self._transfer_biz_amount = value
    @property
    def transfer_biz_type(self):
        return self._transfer_biz_type

    @transfer_biz_type.setter
    def transfer_biz_type(self, value):
        self._transfer_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_account_id:
            if hasattr(self.company_account_id, 'to_alipay_dict'):
                params['company_account_id'] = self.company_account_id.to_alipay_dict()
            else:
                params['company_account_id'] = self.company_account_id
        if self.out_biz_transfer_id:
            if hasattr(self.out_biz_transfer_id, 'to_alipay_dict'):
                params['out_biz_transfer_id'] = self.out_biz_transfer_id.to_alipay_dict()
            else:
                params['out_biz_transfer_id'] = self.out_biz_transfer_id
        if self.payee_account:
            if hasattr(self.payee_account, 'to_alipay_dict'):
                params['payee_account'] = self.payee_account.to_alipay_dict()
            else:
                params['payee_account'] = self.payee_account
        if self.payee_account_type:
            if hasattr(self.payee_account_type, 'to_alipay_dict'):
                params['payee_account_type'] = self.payee_account_type.to_alipay_dict()
            else:
                params['payee_account_type'] = self.payee_account_type
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        if self.recycling_order_id:
            if hasattr(self.recycling_order_id, 'to_alipay_dict'):
                params['recycling_order_id'] = self.recycling_order_id.to_alipay_dict()
            else:
                params['recycling_order_id'] = self.recycling_order_id
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        if self.transfer_biz_amount:
            if hasattr(self.transfer_biz_amount, 'to_alipay_dict'):
                params['transfer_biz_amount'] = self.transfer_biz_amount.to_alipay_dict()
            else:
                params['transfer_biz_amount'] = self.transfer_biz_amount
        if self.transfer_biz_type:
            if hasattr(self.transfer_biz_type, 'to_alipay_dict'):
                params['transfer_biz_type'] = self.transfer_biz_type.to_alipay_dict()
            else:
                params['transfer_biz_type'] = self.transfer_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceBiztransferSubmitModel()
        if 'company_account_id' in d:
            o.company_account_id = d['company_account_id']
        if 'out_biz_transfer_id' in d:
            o.out_biz_transfer_id = d['out_biz_transfer_id']
        if 'payee_account' in d:
            o.payee_account = d['payee_account']
        if 'payee_account_type' in d:
            o.payee_account_type = d['payee_account_type']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'recycling_order_id' in d:
            o.recycling_order_id = d['recycling_order_id']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        if 'transfer_biz_amount' in d:
            o.transfer_biz_amount = d['transfer_biz_amount']
        if 'transfer_biz_type' in d:
            o.transfer_biz_type = d['transfer_biz_type']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XingheLendassistCarfinauctionAuctionsucNotifyModel(object):

    def __init__(self):
        self._apply_no = None
        self._deadline = None
        self._deal_price = None
        self._deal_time = None
        self._foregift_price = None
        self._institution_account_name = None
        self._institution_bank_account = None
        self._institution_bank_code = None
        self._institution_bank_name = None
        self._out_order_no = None
        self._payment_remark = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        self._deadline = value
    @property
    def deal_price(self):
        return self._deal_price

    @deal_price.setter
    def deal_price(self, value):
        self._deal_price = value
    @property
    def deal_time(self):
        return self._deal_time

    @deal_time.setter
    def deal_time(self, value):
        self._deal_time = value
    @property
    def foregift_price(self):
        return self._foregift_price

    @foregift_price.setter
    def foregift_price(self, value):
        self._foregift_price = value
    @property
    def institution_account_name(self):
        return self._institution_account_name

    @institution_account_name.setter
    def institution_account_name(self, value):
        self._institution_account_name = value
    @property
    def institution_bank_account(self):
        return self._institution_bank_account

    @institution_bank_account.setter
    def institution_bank_account(self, value):
        self._institution_bank_account = value
    @property
    def institution_bank_code(self):
        return self._institution_bank_code

    @institution_bank_code.setter
    def institution_bank_code(self, value):
        self._institution_bank_code = value
    @property
    def institution_bank_name(self):
        return self._institution_bank_name

    @institution_bank_name.setter
    def institution_bank_name(self, value):
        self._institution_bank_name = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def payment_remark(self):
        return self._payment_remark

    @payment_remark.setter
    def payment_remark(self, value):
        self._payment_remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.deadline:
            if hasattr(self.deadline, 'to_alipay_dict'):
                params['deadline'] = self.deadline.to_alipay_dict()
            else:
                params['deadline'] = self.deadline
        if self.deal_price:
            if hasattr(self.deal_price, 'to_alipay_dict'):
                params['deal_price'] = self.deal_price.to_alipay_dict()
            else:
                params['deal_price'] = self.deal_price
        if self.deal_time:
            if hasattr(self.deal_time, 'to_alipay_dict'):
                params['deal_time'] = self.deal_time.to_alipay_dict()
            else:
                params['deal_time'] = self.deal_time
        if self.foregift_price:
            if hasattr(self.foregift_price, 'to_alipay_dict'):
                params['foregift_price'] = self.foregift_price.to_alipay_dict()
            else:
                params['foregift_price'] = self.foregift_price
        if self.institution_account_name:
            if hasattr(self.institution_account_name, 'to_alipay_dict'):
                params['institution_account_name'] = self.institution_account_name.to_alipay_dict()
            else:
                params['institution_account_name'] = self.institution_account_name
        if self.institution_bank_account:
            if hasattr(self.institution_bank_account, 'to_alipay_dict'):
                params['institution_bank_account'] = self.institution_bank_account.to_alipay_dict()
            else:
                params['institution_bank_account'] = self.institution_bank_account
        if self.institution_bank_code:
            if hasattr(self.institution_bank_code, 'to_alipay_dict'):
                params['institution_bank_code'] = self.institution_bank_code.to_alipay_dict()
            else:
                params['institution_bank_code'] = self.institution_bank_code
        if self.institution_bank_name:
            if hasattr(self.institution_bank_name, 'to_alipay_dict'):
                params['institution_bank_name'] = self.institution_bank_name.to_alipay_dict()
            else:
                params['institution_bank_name'] = self.institution_bank_name
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.payment_remark:
            if hasattr(self.payment_remark, 'to_alipay_dict'):
                params['payment_remark'] = self.payment_remark.to_alipay_dict()
            else:
                params['payment_remark'] = self.payment_remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinauctionAuctionsucNotifyModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'deadline' in d:
            o.deadline = d['deadline']
        if 'deal_price' in d:
            o.deal_price = d['deal_price']
        if 'deal_time' in d:
            o.deal_time = d['deal_time']
        if 'foregift_price' in d:
            o.foregift_price = d['foregift_price']
        if 'institution_account_name' in d:
            o.institution_account_name = d['institution_account_name']
        if 'institution_bank_account' in d:
            o.institution_bank_account = d['institution_bank_account']
        if 'institution_bank_code' in d:
            o.institution_bank_code = d['institution_bank_code']
        if 'institution_bank_name' in d:
            o.institution_bank_name = d['institution_bank_name']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'payment_remark' in d:
            o.payment_remark = d['payment_remark']
        return o



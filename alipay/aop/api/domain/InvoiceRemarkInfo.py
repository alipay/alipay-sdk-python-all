#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceRemarkInfo(object):

    def __init__(self):
        self._remark = None
        self._show_buyer_address_phone = None
        self._show_buyer_bank_account = None
        self._show_seller_address_phone = None
        self._show_seller_bank_account = None

    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def show_buyer_address_phone(self):
        return self._show_buyer_address_phone

    @show_buyer_address_phone.setter
    def show_buyer_address_phone(self, value):
        self._show_buyer_address_phone = value
    @property
    def show_buyer_bank_account(self):
        return self._show_buyer_bank_account

    @show_buyer_bank_account.setter
    def show_buyer_bank_account(self, value):
        self._show_buyer_bank_account = value
    @property
    def show_seller_address_phone(self):
        return self._show_seller_address_phone

    @show_seller_address_phone.setter
    def show_seller_address_phone(self, value):
        self._show_seller_address_phone = value
    @property
    def show_seller_bank_account(self):
        return self._show_seller_bank_account

    @show_seller_bank_account.setter
    def show_seller_bank_account(self, value):
        self._show_seller_bank_account = value


    def to_alipay_dict(self):
        params = dict()
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.show_buyer_address_phone:
            if hasattr(self.show_buyer_address_phone, 'to_alipay_dict'):
                params['show_buyer_address_phone'] = self.show_buyer_address_phone.to_alipay_dict()
            else:
                params['show_buyer_address_phone'] = self.show_buyer_address_phone
        if self.show_buyer_bank_account:
            if hasattr(self.show_buyer_bank_account, 'to_alipay_dict'):
                params['show_buyer_bank_account'] = self.show_buyer_bank_account.to_alipay_dict()
            else:
                params['show_buyer_bank_account'] = self.show_buyer_bank_account
        if self.show_seller_address_phone:
            if hasattr(self.show_seller_address_phone, 'to_alipay_dict'):
                params['show_seller_address_phone'] = self.show_seller_address_phone.to_alipay_dict()
            else:
                params['show_seller_address_phone'] = self.show_seller_address_phone
        if self.show_seller_bank_account:
            if hasattr(self.show_seller_bank_account, 'to_alipay_dict'):
                params['show_seller_bank_account'] = self.show_seller_bank_account.to_alipay_dict()
            else:
                params['show_seller_bank_account'] = self.show_seller_bank_account
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceRemarkInfo()
        if 'remark' in d:
            o.remark = d['remark']
        if 'show_buyer_address_phone' in d:
            o.show_buyer_address_phone = d['show_buyer_address_phone']
        if 'show_buyer_bank_account' in d:
            o.show_buyer_bank_account = d['show_buyer_bank_account']
        if 'show_seller_address_phone' in d:
            o.show_seller_address_phone = d['show_seller_address_phone']
        if 'show_seller_bank_account' in d:
            o.show_seller_bank_account = d['show_seller_bank_account']
        return o



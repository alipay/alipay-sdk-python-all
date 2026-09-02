#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceCompanysupplierModifyModel(object):

    def __init__(self):
        self._bank_card_no = None
        self._bank_code = None
        self._has_bank_card = None
        self._supplier_id = None
        self._supplier_phone = None
        self._tax_no = None

    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def has_bank_card(self):
        return self._has_bank_card

    @has_bank_card.setter
    def has_bank_card(self, value):
        self._has_bank_card = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def supplier_phone(self):
        return self._supplier_phone

    @supplier_phone.setter
    def supplier_phone(self, value):
        self._supplier_phone = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.has_bank_card:
            if hasattr(self.has_bank_card, 'to_alipay_dict'):
                params['has_bank_card'] = self.has_bank_card.to_alipay_dict()
            else:
                params['has_bank_card'] = self.has_bank_card
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.supplier_phone:
            if hasattr(self.supplier_phone, 'to_alipay_dict'):
                params['supplier_phone'] = self.supplier_phone.to_alipay_dict()
            else:
                params['supplier_phone'] = self.supplier_phone
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceCompanysupplierModifyModel()
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'has_bank_card' in d:
            o.has_bank_card = d['has_bank_card']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'supplier_phone' in d:
            o.supplier_phone = d['supplier_phone']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o



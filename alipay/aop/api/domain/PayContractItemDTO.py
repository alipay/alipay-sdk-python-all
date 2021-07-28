#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayContractItemDTO(object):

    def __init__(self):
        self._description = None
        self._item_no = None
        self._item_type = None
        self._need_invoice = None
        self._pay_apply_date = None
        self._pay_ref_type = None
        self._pay_term = None
        self._pay_term_type = None
        self._payment_amount = None
        self._phase = None
        self._terms = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def item_no(self):
        return self._item_no

    @item_no.setter
    def item_no(self, value):
        self._item_no = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def need_invoice(self):
        return self._need_invoice

    @need_invoice.setter
    def need_invoice(self, value):
        self._need_invoice = value
    @property
    def pay_apply_date(self):
        return self._pay_apply_date

    @pay_apply_date.setter
    def pay_apply_date(self, value):
        self._pay_apply_date = value
    @property
    def pay_ref_type(self):
        return self._pay_ref_type

    @pay_ref_type.setter
    def pay_ref_type(self, value):
        self._pay_ref_type = value
    @property
    def pay_term(self):
        return self._pay_term

    @pay_term.setter
    def pay_term(self, value):
        self._pay_term = value
    @property
    def pay_term_type(self):
        return self._pay_term_type

    @pay_term_type.setter
    def pay_term_type(self, value):
        self._pay_term_type = value
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, value):
        self._phase = value
    @property
    def terms(self):
        return self._terms

    @terms.setter
    def terms(self, value):
        self._terms = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.item_no:
            if hasattr(self.item_no, 'to_alipay_dict'):
                params['item_no'] = self.item_no.to_alipay_dict()
            else:
                params['item_no'] = self.item_no
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.need_invoice:
            if hasattr(self.need_invoice, 'to_alipay_dict'):
                params['need_invoice'] = self.need_invoice.to_alipay_dict()
            else:
                params['need_invoice'] = self.need_invoice
        if self.pay_apply_date:
            if hasattr(self.pay_apply_date, 'to_alipay_dict'):
                params['pay_apply_date'] = self.pay_apply_date.to_alipay_dict()
            else:
                params['pay_apply_date'] = self.pay_apply_date
        if self.pay_ref_type:
            if hasattr(self.pay_ref_type, 'to_alipay_dict'):
                params['pay_ref_type'] = self.pay_ref_type.to_alipay_dict()
            else:
                params['pay_ref_type'] = self.pay_ref_type
        if self.pay_term:
            if hasattr(self.pay_term, 'to_alipay_dict'):
                params['pay_term'] = self.pay_term.to_alipay_dict()
            else:
                params['pay_term'] = self.pay_term
        if self.pay_term_type:
            if hasattr(self.pay_term_type, 'to_alipay_dict'):
                params['pay_term_type'] = self.pay_term_type.to_alipay_dict()
            else:
                params['pay_term_type'] = self.pay_term_type
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.phase:
            if hasattr(self.phase, 'to_alipay_dict'):
                params['phase'] = self.phase.to_alipay_dict()
            else:
                params['phase'] = self.phase
        if self.terms:
            if hasattr(self.terms, 'to_alipay_dict'):
                params['terms'] = self.terms.to_alipay_dict()
            else:
                params['terms'] = self.terms
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayContractItemDTO()
        if 'description' in d:
            o.description = d['description']
        if 'item_no' in d:
            o.item_no = d['item_no']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'need_invoice' in d:
            o.need_invoice = d['need_invoice']
        if 'pay_apply_date' in d:
            o.pay_apply_date = d['pay_apply_date']
        if 'pay_ref_type' in d:
            o.pay_ref_type = d['pay_ref_type']
        if 'pay_term' in d:
            o.pay_term = d['pay_term']
        if 'pay_term_type' in d:
            o.pay_term_type = d['pay_term_type']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'phase' in d:
            o.phase = d['phase']
        if 'terms' in d:
            o.terms = d['terms']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiPaymentTermsItemDTO(object):

    def __init__(self):
        self._id = None
        self._need_invoice = None
        self._pay_base = None
        self._pay_pre_type = None
        self._pay_ref_type = None
        self._pay_term = None
        self._pay_term_type = None
        self._payment_amount = None
        self._payment_item_type = None
        self._payment_percent = None
        self._payment_terms_id = None
        self._phase = None
        self._terms = None
        self._terms_cn = None
        self._terms_en = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def need_invoice(self):
        return self._need_invoice

    @need_invoice.setter
    def need_invoice(self, value):
        self._need_invoice = value
    @property
    def pay_base(self):
        return self._pay_base

    @pay_base.setter
    def pay_base(self, value):
        self._pay_base = value
    @property
    def pay_pre_type(self):
        return self._pay_pre_type

    @pay_pre_type.setter
    def pay_pre_type(self, value):
        self._pay_pre_type = value
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
    def payment_item_type(self):
        return self._payment_item_type

    @payment_item_type.setter
    def payment_item_type(self, value):
        self._payment_item_type = value
    @property
    def payment_percent(self):
        return self._payment_percent

    @payment_percent.setter
    def payment_percent(self, value):
        self._payment_percent = value
    @property
    def payment_terms_id(self):
        return self._payment_terms_id

    @payment_terms_id.setter
    def payment_terms_id(self, value):
        self._payment_terms_id = value
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
    @property
    def terms_cn(self):
        return self._terms_cn

    @terms_cn.setter
    def terms_cn(self, value):
        self._terms_cn = value
    @property
    def terms_en(self):
        return self._terms_en

    @terms_en.setter
    def terms_en(self, value):
        self._terms_en = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.need_invoice:
            if hasattr(self.need_invoice, 'to_alipay_dict'):
                params['need_invoice'] = self.need_invoice.to_alipay_dict()
            else:
                params['need_invoice'] = self.need_invoice
        if self.pay_base:
            if hasattr(self.pay_base, 'to_alipay_dict'):
                params['pay_base'] = self.pay_base.to_alipay_dict()
            else:
                params['pay_base'] = self.pay_base
        if self.pay_pre_type:
            if hasattr(self.pay_pre_type, 'to_alipay_dict'):
                params['pay_pre_type'] = self.pay_pre_type.to_alipay_dict()
            else:
                params['pay_pre_type'] = self.pay_pre_type
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
        if self.payment_item_type:
            if hasattr(self.payment_item_type, 'to_alipay_dict'):
                params['payment_item_type'] = self.payment_item_type.to_alipay_dict()
            else:
                params['payment_item_type'] = self.payment_item_type
        if self.payment_percent:
            if hasattr(self.payment_percent, 'to_alipay_dict'):
                params['payment_percent'] = self.payment_percent.to_alipay_dict()
            else:
                params['payment_percent'] = self.payment_percent
        if self.payment_terms_id:
            if hasattr(self.payment_terms_id, 'to_alipay_dict'):
                params['payment_terms_id'] = self.payment_terms_id.to_alipay_dict()
            else:
                params['payment_terms_id'] = self.payment_terms_id
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
        if self.terms_cn:
            if hasattr(self.terms_cn, 'to_alipay_dict'):
                params['terms_cn'] = self.terms_cn.to_alipay_dict()
            else:
                params['terms_cn'] = self.terms_cn
        if self.terms_en:
            if hasattr(self.terms_en, 'to_alipay_dict'):
                params['terms_en'] = self.terms_en.to_alipay_dict()
            else:
                params['terms_en'] = self.terms_en
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiPaymentTermsItemDTO()
        if 'id' in d:
            o.id = d['id']
        if 'need_invoice' in d:
            o.need_invoice = d['need_invoice']
        if 'pay_base' in d:
            o.pay_base = d['pay_base']
        if 'pay_pre_type' in d:
            o.pay_pre_type = d['pay_pre_type']
        if 'pay_ref_type' in d:
            o.pay_ref_type = d['pay_ref_type']
        if 'pay_term' in d:
            o.pay_term = d['pay_term']
        if 'pay_term_type' in d:
            o.pay_term_type = d['pay_term_type']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'payment_item_type' in d:
            o.payment_item_type = d['payment_item_type']
        if 'payment_percent' in d:
            o.payment_percent = d['payment_percent']
        if 'payment_terms_id' in d:
            o.payment_terms_id = d['payment_terms_id']
        if 'phase' in d:
            o.phase = d['phase']
        if 'terms' in d:
            o.terms = d['terms']
        if 'terms_cn' in d:
            o.terms_cn = d['terms_cn']
        if 'terms_en' in d:
            o.terms_en = d['terms_en']
        return o



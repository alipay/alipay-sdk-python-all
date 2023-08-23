#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentPlanItemDTO(object):

    def __init__(self):
        self._ext = None
        self._item_digest_cn = None
        self._item_digest_en = None
        self._item_type = None
        self._need_invoice = None
        self._pay_apply_date = None
        self._pay_ref_type = None
        self._pay_term = None
        self._pay_term_type = None
        self._payment_amount = None
        self._payment_percent = None
        self._payment_plan_item_id = None
        self._phase = None
        self._terms = None

    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
    @property
    def item_digest_cn(self):
        return self._item_digest_cn

    @item_digest_cn.setter
    def item_digest_cn(self, value):
        self._item_digest_cn = value
    @property
    def item_digest_en(self):
        return self._item_digest_en

    @item_digest_en.setter
    def item_digest_en(self, value):
        self._item_digest_en = value
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
    def payment_percent(self):
        return self._payment_percent

    @payment_percent.setter
    def payment_percent(self, value):
        self._payment_percent = value
    @property
    def payment_plan_item_id(self):
        return self._payment_plan_item_id

    @payment_plan_item_id.setter
    def payment_plan_item_id(self, value):
        self._payment_plan_item_id = value
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
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.item_digest_cn:
            if hasattr(self.item_digest_cn, 'to_alipay_dict'):
                params['item_digest_cn'] = self.item_digest_cn.to_alipay_dict()
            else:
                params['item_digest_cn'] = self.item_digest_cn
        if self.item_digest_en:
            if hasattr(self.item_digest_en, 'to_alipay_dict'):
                params['item_digest_en'] = self.item_digest_en.to_alipay_dict()
            else:
                params['item_digest_en'] = self.item_digest_en
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
        if self.payment_percent:
            if hasattr(self.payment_percent, 'to_alipay_dict'):
                params['payment_percent'] = self.payment_percent.to_alipay_dict()
            else:
                params['payment_percent'] = self.payment_percent
        if self.payment_plan_item_id:
            if hasattr(self.payment_plan_item_id, 'to_alipay_dict'):
                params['payment_plan_item_id'] = self.payment_plan_item_id.to_alipay_dict()
            else:
                params['payment_plan_item_id'] = self.payment_plan_item_id
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
        o = PaymentPlanItemDTO()
        if 'ext' in d:
            o.ext = d['ext']
        if 'item_digest_cn' in d:
            o.item_digest_cn = d['item_digest_cn']
        if 'item_digest_en' in d:
            o.item_digest_en = d['item_digest_en']
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
        if 'payment_percent' in d:
            o.payment_percent = d['payment_percent']
        if 'payment_plan_item_id' in d:
            o.payment_plan_item_id = d['payment_plan_item_id']
        if 'phase' in d:
            o.phase = d['phase']
        if 'terms' in d:
            o.terms = d['terms']
        return o



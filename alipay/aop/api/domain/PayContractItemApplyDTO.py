#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class PayContractItemApplyDTO(object):

    def __init__(self):
        self._invoice_received_amount = None
        self._issued_amount = None
        self._item_no = None
        self._item_type = None
        self._need_invoice = None
        self._paid_amount = None
        self._pay_ref_type = None
        self._pay_term = None
        self._pay_term_type = None
        self._payable_amount = None
        self._payment_amount = None
        self._payment_type = None
        self._phase = None
        self._status = None
        self._terms = None

    @property
    def invoice_received_amount(self):
        return self._invoice_received_amount

    @invoice_received_amount.setter
    def invoice_received_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invoice_received_amount = value
        else:
            self._invoice_received_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def issued_amount(self):
        return self._issued_amount

    @issued_amount.setter
    def issued_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._issued_amount = value
        else:
            self._issued_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
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
    def paid_amount(self):
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._paid_amount = value
        else:
            self._paid_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
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
    def payable_amount(self):
        return self._payable_amount

    @payable_amount.setter
    def payable_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._payable_amount = value
        else:
            self._payable_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, value):
        self._phase = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def terms(self):
        return self._terms

    @terms.setter
    def terms(self, value):
        self._terms = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_received_amount:
            if hasattr(self.invoice_received_amount, 'to_alipay_dict'):
                params['invoice_received_amount'] = self.invoice_received_amount.to_alipay_dict()
            else:
                params['invoice_received_amount'] = self.invoice_received_amount
        if self.issued_amount:
            if hasattr(self.issued_amount, 'to_alipay_dict'):
                params['issued_amount'] = self.issued_amount.to_alipay_dict()
            else:
                params['issued_amount'] = self.issued_amount
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
        if self.paid_amount:
            if hasattr(self.paid_amount, 'to_alipay_dict'):
                params['paid_amount'] = self.paid_amount.to_alipay_dict()
            else:
                params['paid_amount'] = self.paid_amount
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
        if self.payable_amount:
            if hasattr(self.payable_amount, 'to_alipay_dict'):
                params['payable_amount'] = self.payable_amount.to_alipay_dict()
            else:
                params['payable_amount'] = self.payable_amount
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.phase:
            if hasattr(self.phase, 'to_alipay_dict'):
                params['phase'] = self.phase.to_alipay_dict()
            else:
                params['phase'] = self.phase
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = PayContractItemApplyDTO()
        if 'invoice_received_amount' in d:
            o.invoice_received_amount = d['invoice_received_amount']
        if 'issued_amount' in d:
            o.issued_amount = d['issued_amount']
        if 'item_no' in d:
            o.item_no = d['item_no']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'need_invoice' in d:
            o.need_invoice = d['need_invoice']
        if 'paid_amount' in d:
            o.paid_amount = d['paid_amount']
        if 'pay_ref_type' in d:
            o.pay_ref_type = d['pay_ref_type']
        if 'pay_term' in d:
            o.pay_term = d['pay_term']
        if 'pay_term_type' in d:
            o.pay_term_type = d['pay_term_type']
        if 'payable_amount' in d:
            o.payable_amount = d['payable_amount']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'phase' in d:
            o.phase = d['phase']
        if 'status' in d:
            o.status = d['status']
        if 'terms' in d:
            o.terms = d['terms']
        return o



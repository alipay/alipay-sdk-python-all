#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbTicketUseDetail(object):

    def __init__(self):
        self._buyer_pay_amount = None
        self._discount_amount = None
        self._invoice_amount = None
        self._koubei_subsidy_amount = None
        self._receipt_amount = None
        self._ticket_code = None
        self._ticket_trans_id = None

    @property
    def buyer_pay_amount(self):
        return self._buyer_pay_amount

    @buyer_pay_amount.setter
    def buyer_pay_amount(self, value):
        self._buyer_pay_amount = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def koubei_subsidy_amount(self):
        return self._koubei_subsidy_amount

    @koubei_subsidy_amount.setter
    def koubei_subsidy_amount(self, value):
        self._koubei_subsidy_amount = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def ticket_code(self):
        return self._ticket_code

    @ticket_code.setter
    def ticket_code(self, value):
        self._ticket_code = value
    @property
    def ticket_trans_id(self):
        return self._ticket_trans_id

    @ticket_trans_id.setter
    def ticket_trans_id(self, value):
        self._ticket_trans_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_pay_amount:
            if hasattr(self.buyer_pay_amount, 'to_alipay_dict'):
                params['buyer_pay_amount'] = self.buyer_pay_amount.to_alipay_dict()
            else:
                params['buyer_pay_amount'] = self.buyer_pay_amount
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
        if self.koubei_subsidy_amount:
            if hasattr(self.koubei_subsidy_amount, 'to_alipay_dict'):
                params['koubei_subsidy_amount'] = self.koubei_subsidy_amount.to_alipay_dict()
            else:
                params['koubei_subsidy_amount'] = self.koubei_subsidy_amount
        if self.receipt_amount:
            if hasattr(self.receipt_amount, 'to_alipay_dict'):
                params['receipt_amount'] = self.receipt_amount.to_alipay_dict()
            else:
                params['receipt_amount'] = self.receipt_amount
        if self.ticket_code:
            if hasattr(self.ticket_code, 'to_alipay_dict'):
                params['ticket_code'] = self.ticket_code.to_alipay_dict()
            else:
                params['ticket_code'] = self.ticket_code
        if self.ticket_trans_id:
            if hasattr(self.ticket_trans_id, 'to_alipay_dict'):
                params['ticket_trans_id'] = self.ticket_trans_id.to_alipay_dict()
            else:
                params['ticket_trans_id'] = self.ticket_trans_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbTicketUseDetail()
        if 'buyer_pay_amount' in d:
            o.buyer_pay_amount = d['buyer_pay_amount']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'koubei_subsidy_amount' in d:
            o.koubei_subsidy_amount = d['koubei_subsidy_amount']
        if 'receipt_amount' in d:
            o.receipt_amount = d['receipt_amount']
        if 'ticket_code' in d:
            o.ticket_code = d['ticket_code']
        if 'ticket_trans_id' in d:
            o.ticket_trans_id = d['ticket_trans_id']
        return o



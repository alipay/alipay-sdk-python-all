#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPayafteruseCreditbizorderCreateModel(object):

    def __init__(self):
        self._amount_type = None
        self._body = None
        self._cancel_back_link = None
        self._category_id = None
        self._commercial_sub_mode = None
        self._credit_commercial_mode = None
        self._extend_params = None
        self._order_amount = None
        self._out_agreement_no = None
        self._out_order_no = None
        self._payment_total_times = None
        self._product_code = None
        self._return_back_link = None
        self._stage_period_type = None
        self._subject = None
        self._zm_service_id = None

    @property
    def amount_type(self):
        return self._amount_type

    @amount_type.setter
    def amount_type(self, value):
        self._amount_type = value
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def cancel_back_link(self):
        return self._cancel_back_link

    @cancel_back_link.setter
    def cancel_back_link(self, value):
        self._cancel_back_link = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def commercial_sub_mode(self):
        return self._commercial_sub_mode

    @commercial_sub_mode.setter
    def commercial_sub_mode(self, value):
        self._commercial_sub_mode = value
    @property
    def credit_commercial_mode(self):
        return self._credit_commercial_mode

    @credit_commercial_mode.setter
    def credit_commercial_mode(self, value):
        self._credit_commercial_mode = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def payment_total_times(self):
        return self._payment_total_times

    @payment_total_times.setter
    def payment_total_times(self, value):
        self._payment_total_times = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def return_back_link(self):
        return self._return_back_link

    @return_back_link.setter
    def return_back_link(self, value):
        self._return_back_link = value
    @property
    def stage_period_type(self):
        return self._stage_period_type

    @stage_period_type.setter
    def stage_period_type(self, value):
        self._stage_period_type = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def zm_service_id(self):
        return self._zm_service_id

    @zm_service_id.setter
    def zm_service_id(self, value):
        self._zm_service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_type:
            if hasattr(self.amount_type, 'to_alipay_dict'):
                params['amount_type'] = self.amount_type.to_alipay_dict()
            else:
                params['amount_type'] = self.amount_type
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.cancel_back_link:
            if hasattr(self.cancel_back_link, 'to_alipay_dict'):
                params['cancel_back_link'] = self.cancel_back_link.to_alipay_dict()
            else:
                params['cancel_back_link'] = self.cancel_back_link
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.commercial_sub_mode:
            if hasattr(self.commercial_sub_mode, 'to_alipay_dict'):
                params['commercial_sub_mode'] = self.commercial_sub_mode.to_alipay_dict()
            else:
                params['commercial_sub_mode'] = self.commercial_sub_mode
        if self.credit_commercial_mode:
            if hasattr(self.credit_commercial_mode, 'to_alipay_dict'):
                params['credit_commercial_mode'] = self.credit_commercial_mode.to_alipay_dict()
            else:
                params['credit_commercial_mode'] = self.credit_commercial_mode
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.out_agreement_no:
            if hasattr(self.out_agreement_no, 'to_alipay_dict'):
                params['out_agreement_no'] = self.out_agreement_no.to_alipay_dict()
            else:
                params['out_agreement_no'] = self.out_agreement_no
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.payment_total_times:
            if hasattr(self.payment_total_times, 'to_alipay_dict'):
                params['payment_total_times'] = self.payment_total_times.to_alipay_dict()
            else:
                params['payment_total_times'] = self.payment_total_times
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.return_back_link:
            if hasattr(self.return_back_link, 'to_alipay_dict'):
                params['return_back_link'] = self.return_back_link.to_alipay_dict()
            else:
                params['return_back_link'] = self.return_back_link
        if self.stage_period_type:
            if hasattr(self.stage_period_type, 'to_alipay_dict'):
                params['stage_period_type'] = self.stage_period_type.to_alipay_dict()
            else:
                params['stage_period_type'] = self.stage_period_type
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.zm_service_id:
            if hasattr(self.zm_service_id, 'to_alipay_dict'):
                params['zm_service_id'] = self.zm_service_id.to_alipay_dict()
            else:
                params['zm_service_id'] = self.zm_service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPayafteruseCreditbizorderCreateModel()
        if 'amount_type' in d:
            o.amount_type = d['amount_type']
        if 'body' in d:
            o.body = d['body']
        if 'cancel_back_link' in d:
            o.cancel_back_link = d['cancel_back_link']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'commercial_sub_mode' in d:
            o.commercial_sub_mode = d['commercial_sub_mode']
        if 'credit_commercial_mode' in d:
            o.credit_commercial_mode = d['credit_commercial_mode']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'out_agreement_no' in d:
            o.out_agreement_no = d['out_agreement_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'payment_total_times' in d:
            o.payment_total_times = d['payment_total_times']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'return_back_link' in d:
            o.return_back_link = d['return_back_link']
        if 'stage_period_type' in d:
            o.stage_period_type = d['stage_period_type']
        if 'subject' in d:
            o.subject = d['subject']
        if 'zm_service_id' in d:
            o.zm_service_id = d['zm_service_id']
        return o



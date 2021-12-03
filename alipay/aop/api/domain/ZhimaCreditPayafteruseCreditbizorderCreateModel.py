#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPayafteruseCreditbizorderCreateModel(object):

    def __init__(self):
        self._body = None
        self._cancel_back_link = None
        self._category_id = None
        self._extend_params = None
        self._order_amount = None
        self._out_agreement_no = None
        self._out_order_no = None
        self._product_code = None
        self._return_back_link = None
        self._subject = None
        self._zm_service_id = None

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
        if 'body' in d:
            o.body = d['body']
        if 'cancel_back_link' in d:
            o.cancel_back_link = d['cancel_back_link']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'out_agreement_no' in d:
            o.out_agreement_no = d['out_agreement_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'return_back_link' in d:
            o.return_back_link = d['return_back_link']
        if 'subject' in d:
            o.subject = d['subject']
        if 'zm_service_id' in d:
            o.zm_service_id = d['zm_service_id']
        return o



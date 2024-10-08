#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsurancePayRefundModel(object):

    def __init__(self):
        self._apply_no = None
        self._biz_type = None
        self._claim_order_no = None
        self._open_id = None
        self._out_pay_order_no = None
        self._source = None
        self._title = None
        self._total_amount = None
        self._user_id = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def claim_order_no(self):
        return self._claim_order_no

    @claim_order_no.setter
    def claim_order_no(self, value):
        self._claim_order_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_pay_order_no(self):
        return self._out_pay_order_no

    @out_pay_order_no.setter
    def out_pay_order_no(self, value):
        self._out_pay_order_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.claim_order_no:
            if hasattr(self.claim_order_no, 'to_alipay_dict'):
                params['claim_order_no'] = self.claim_order_no.to_alipay_dict()
            else:
                params['claim_order_no'] = self.claim_order_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_pay_order_no:
            if hasattr(self.out_pay_order_no, 'to_alipay_dict'):
                params['out_pay_order_no'] = self.out_pay_order_no.to_alipay_dict()
            else:
                params['out_pay_order_no'] = self.out_pay_order_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsurancePayRefundModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'claim_order_no' in d:
            o.claim_order_no = d['claim_order_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_pay_order_no' in d:
            o.out_pay_order_no = d['out_pay_order_no']
        if 'source' in d:
            o.source = d['source']
        if 'title' in d:
            o.title = d['title']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



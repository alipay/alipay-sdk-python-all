#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransBatchCreatesinglebatchModel(object):

    def __init__(self):
        self._batch_memo = None
        self._biz_type = None
        self._create_user_id = None
        self._ext_param = None
        self._pay_amount_single = None
        self._pay_amount_total = None
        self._real_items_total = None
        self._show_items_total = None

    @property
    def batch_memo(self):
        return self._batch_memo

    @batch_memo.setter
    def batch_memo(self, value):
        self._batch_memo = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def create_user_id(self):
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, value):
        self._create_user_id = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def pay_amount_single(self):
        return self._pay_amount_single

    @pay_amount_single.setter
    def pay_amount_single(self, value):
        self._pay_amount_single = value
    @property
    def pay_amount_total(self):
        return self._pay_amount_total

    @pay_amount_total.setter
    def pay_amount_total(self, value):
        self._pay_amount_total = value
    @property
    def real_items_total(self):
        return self._real_items_total

    @real_items_total.setter
    def real_items_total(self, value):
        self._real_items_total = value
    @property
    def show_items_total(self):
        return self._show_items_total

    @show_items_total.setter
    def show_items_total(self, value):
        self._show_items_total = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_memo:
            if hasattr(self.batch_memo, 'to_alipay_dict'):
                params['batch_memo'] = self.batch_memo.to_alipay_dict()
            else:
                params['batch_memo'] = self.batch_memo
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.create_user_id:
            if hasattr(self.create_user_id, 'to_alipay_dict'):
                params['create_user_id'] = self.create_user_id.to_alipay_dict()
            else:
                params['create_user_id'] = self.create_user_id
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.pay_amount_single:
            if hasattr(self.pay_amount_single, 'to_alipay_dict'):
                params['pay_amount_single'] = self.pay_amount_single.to_alipay_dict()
            else:
                params['pay_amount_single'] = self.pay_amount_single
        if self.pay_amount_total:
            if hasattr(self.pay_amount_total, 'to_alipay_dict'):
                params['pay_amount_total'] = self.pay_amount_total.to_alipay_dict()
            else:
                params['pay_amount_total'] = self.pay_amount_total
        if self.real_items_total:
            if hasattr(self.real_items_total, 'to_alipay_dict'):
                params['real_items_total'] = self.real_items_total.to_alipay_dict()
            else:
                params['real_items_total'] = self.real_items_total
        if self.show_items_total:
            if hasattr(self.show_items_total, 'to_alipay_dict'):
                params['show_items_total'] = self.show_items_total.to_alipay_dict()
            else:
                params['show_items_total'] = self.show_items_total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransBatchCreatesinglebatchModel()
        if 'batch_memo' in d:
            o.batch_memo = d['batch_memo']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'create_user_id' in d:
            o.create_user_id = d['create_user_id']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'pay_amount_single' in d:
            o.pay_amount_single = d['pay_amount_single']
        if 'pay_amount_total' in d:
            o.pay_amount_total = d['pay_amount_total']
        if 'real_items_total' in d:
            o.real_items_total = d['real_items_total']
        if 'show_items_total' in d:
            o.show_items_total = d['show_items_total']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditOrderRepaymentApplyModel(object):

    def __init__(self):
        self._action_type = None
        self._category = None
        self._order_info = None
        self._out_order_no = None
        self._repay_amount = None
        self._repay_proof = None
        self._user_id = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def order_info(self):
        return self._order_info

    @order_info.setter
    def order_info(self, value):
        self._order_info = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def repay_amount(self):
        return self._repay_amount

    @repay_amount.setter
    def repay_amount(self, value):
        self._repay_amount = value
    @property
    def repay_proof(self):
        return self._repay_proof

    @repay_proof.setter
    def repay_proof(self, value):
        self._repay_proof = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.order_info:
            if hasattr(self.order_info, 'to_alipay_dict'):
                params['order_info'] = self.order_info.to_alipay_dict()
            else:
                params['order_info'] = self.order_info
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.repay_amount:
            if hasattr(self.repay_amount, 'to_alipay_dict'):
                params['repay_amount'] = self.repay_amount.to_alipay_dict()
            else:
                params['repay_amount'] = self.repay_amount
        if self.repay_proof:
            if hasattr(self.repay_proof, 'to_alipay_dict'):
                params['repay_proof'] = self.repay_proof.to_alipay_dict()
            else:
                params['repay_proof'] = self.repay_proof
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
        o = ZhimaCreditOrderRepaymentApplyModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'category' in d:
            o.category = d['category']
        if 'order_info' in d:
            o.order_info = d['order_info']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'repay_amount' in d:
            o.repay_amount = d['repay_amount']
        if 'repay_proof' in d:
            o.repay_proof = d['repay_proof']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



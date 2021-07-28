#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanBeikeaccountInterestfreeModifyModel(object):

    def __init__(self):
        self._operation_amount = None
        self._operation_type = None
        self._outer_biz_no = None
        self._scenes = None
        self._user_id = None

    @property
    def operation_amount(self):
        return self._operation_amount

    @operation_amount.setter
    def operation_amount(self, value):
        self._operation_amount = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def outer_biz_no(self):
        return self._outer_biz_no

    @outer_biz_no.setter
    def outer_biz_no(self, value):
        self._outer_biz_no = value
    @property
    def scenes(self):
        return self._scenes

    @scenes.setter
    def scenes(self, value):
        self._scenes = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.operation_amount:
            if hasattr(self.operation_amount, 'to_alipay_dict'):
                params['operation_amount'] = self.operation_amount.to_alipay_dict()
            else:
                params['operation_amount'] = self.operation_amount
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.outer_biz_no:
            if hasattr(self.outer_biz_no, 'to_alipay_dict'):
                params['outer_biz_no'] = self.outer_biz_no.to_alipay_dict()
            else:
                params['outer_biz_no'] = self.outer_biz_no
        if self.scenes:
            if hasattr(self.scenes, 'to_alipay_dict'):
                params['scenes'] = self.scenes.to_alipay_dict()
            else:
                params['scenes'] = self.scenes
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
        o = AlipayPcreditLoanBeikeaccountInterestfreeModifyModel()
        if 'operation_amount' in d:
            o.operation_amount = d['operation_amount']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'outer_biz_no' in d:
            o.outer_biz_no = d['outer_biz_no']
        if 'scenes' in d:
            o.scenes = d['scenes']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenWanxintestwxQueryModel(object):

    def __init__(self):
        self._age = None
        self._op = None
        self._open_id = None
        self._test = None
        self._ty = None
        self._user_id = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def op(self):
        return self._op

    @op.setter
    def op(self, value):
        self._op = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        self._test = value
    @property
    def ty(self):
        return self._ty

    @ty.setter
    def ty(self, value):
        self._ty = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.op:
            if hasattr(self.op, 'to_alipay_dict'):
                params['op'] = self.op.to_alipay_dict()
            else:
                params['op'] = self.op
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.test:
            if hasattr(self.test, 'to_alipay_dict'):
                params['test'] = self.test.to_alipay_dict()
            else:
                params['test'] = self.test
        if self.ty:
            if hasattr(self.ty, 'to_alipay_dict'):
                params['ty'] = self.ty.to_alipay_dict()
            else:
                params['ty'] = self.ty
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
        o = AlipayOpenWanxintestwxQueryModel()
        if 'age' in d:
            o.age = d['age']
        if 'op' in d:
            o.op = d['op']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'test' in d:
            o.test = d['test']
        if 'ty' in d:
            o.ty = d['ty']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



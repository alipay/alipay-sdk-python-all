#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenWanxintestaaaQueryModel(object):

    def __init__(self):
        self._age = None
        self._agee = None
        self._demo = None
        self._test = None
        self._ty = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def agee(self):
        return self._agee

    @agee.setter
    def agee(self, value):
        self._agee = value
    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, value):
        self._demo = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.agee:
            if hasattr(self.agee, 'to_alipay_dict'):
                params['agee'] = self.agee.to_alipay_dict()
            else:
                params['agee'] = self.agee
        if self.demo:
            if hasattr(self.demo, 'to_alipay_dict'):
                params['demo'] = self.demo.to_alipay_dict()
            else:
                params['demo'] = self.demo
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenWanxintestaaaQueryModel()
        if 'age' in d:
            o.age = d['age']
        if 'agee' in d:
            o.agee = d['agee']
        if 'demo' in d:
            o.demo = d['demo']
        if 'test' in d:
            o.test = d['test']
        if 'ty' in d:
            o.ty = d['ty']
        return o



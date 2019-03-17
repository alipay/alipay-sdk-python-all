#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GavintestNewLeveaOne import GavintestNewLeveaOne


class AlipayOpenDesCreateModel(object):

    def __init__(self):
        self._des = None
        self._test = None

    @property
    def des(self):
        return self._des

    @des.setter
    def des(self, value):
        if isinstance(value, list):
            self._des = list()
            for i in value:
                if isinstance(i, GavintestNewLeveaOne):
                    self._des.append(i)
                else:
                    self._des.append(GavintestNewLeveaOne.from_alipay_dict(i))
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        if isinstance(value, list):
            self._test = list()
            for i in value:
                self._test.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.des:
            if isinstance(self.des, list):
                for i in range(0, len(self.des)):
                    element = self.des[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.des[i] = element.to_alipay_dict()
            if hasattr(self.des, 'to_alipay_dict'):
                params['des'] = self.des.to_alipay_dict()
            else:
                params['des'] = self.des
        if self.test:
            if isinstance(self.test, list):
                for i in range(0, len(self.test)):
                    element = self.test[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test[i] = element.to_alipay_dict()
            if hasattr(self.test, 'to_alipay_dict'):
                params['test'] = self.test.to_alipay_dict()
            else:
                params['test'] = self.test
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenDesCreateModel()
        if 'des' in d:
            o.des = d['des']
        if 'test' in d:
            o.test = d['test']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationOpenbizmockTestparameterQueryModel(object):

    def __init__(self):
        self._a = None
        self._b = None
        self._c = None
        self._date = None
        self._e = None
        self._f = None
        self._number = None
        self._price = None
        self._ss_list = None

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value
    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def e(self):
        return self._e

    @e.setter
    def e(self, value):
        self._e = value
    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, value):
        self._f = value
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def ss_list(self):
        return self._ss_list

    @ss_list.setter
    def ss_list(self, value):
        if isinstance(value, list):
            self._ss_list = list()
            for i in value:
                self._ss_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.a:
            if hasattr(self.a, 'to_alipay_dict'):
                params['a'] = self.a.to_alipay_dict()
            else:
                params['a'] = self.a
        if self.b:
            if hasattr(self.b, 'to_alipay_dict'):
                params['b'] = self.b.to_alipay_dict()
            else:
                params['b'] = self.b
        if self.c:
            if hasattr(self.c, 'to_alipay_dict'):
                params['c'] = self.c.to_alipay_dict()
            else:
                params['c'] = self.c
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.e:
            if hasattr(self.e, 'to_alipay_dict'):
                params['e'] = self.e.to_alipay_dict()
            else:
                params['e'] = self.e
        if self.f:
            if hasattr(self.f, 'to_alipay_dict'):
                params['f'] = self.f.to_alipay_dict()
            else:
                params['f'] = self.f
        if self.number:
            if hasattr(self.number, 'to_alipay_dict'):
                params['number'] = self.number.to_alipay_dict()
            else:
                params['number'] = self.number
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.ss_list:
            if isinstance(self.ss_list, list):
                for i in range(0, len(self.ss_list)):
                    element = self.ss_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ss_list[i] = element.to_alipay_dict()
            if hasattr(self.ss_list, 'to_alipay_dict'):
                params['ss_list'] = self.ss_list.to_alipay_dict()
            else:
                params['ss_list'] = self.ss_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockTestparameterQueryModel()
        if 'a' in d:
            o.a = d['a']
        if 'b' in d:
            o.b = d['b']
        if 'c' in d:
            o.c = d['c']
        if 'date' in d:
            o.date = d['date']
        if 'e' in d:
            o.e = d['e']
        if 'f' in d:
            o.f = d['f']
        if 'number' in d:
            o.number = d['number']
        if 'price' in d:
            o.price = d['price']
        if 'ss_list' in d:
            o.ss_list = d['ss_list']
        return o



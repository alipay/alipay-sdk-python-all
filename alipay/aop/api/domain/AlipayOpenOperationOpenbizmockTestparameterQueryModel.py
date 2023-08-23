#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenidComplex import OpenidComplex
from alipay.aop.api.domain.OpenidComplex import OpenidComplex


class AlipayOpenOperationOpenbizmockTestparameterQueryModel(object):

    def __init__(self):
        self._a = None
        self._appid_one = None
        self._appid_out_one = None
        self._appid_out_two = None
        self._appid_two = None
        self._b = None
        self._c = None
        self._date = None
        self._e = None
        self._f = None
        self._number = None
        self._one_uid = None
        self._one_uid_openid = None
        self._price = None
        self._ss_list = None
        self._test = None
        self._test_test = None
        self._two_uid = None
        self._two_uid_openid = None
        self._uid_one = None
        self._uid_two = None
        self._uidone_openid = None
        self._uidtwo_openid = None

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
    @property
    def appid_one(self):
        return self._appid_one

    @appid_one.setter
    def appid_one(self, value):
        self._appid_one = value
    @property
    def appid_out_one(self):
        return self._appid_out_one

    @appid_out_one.setter
    def appid_out_one(self, value):
        self._appid_out_one = value
    @property
    def appid_out_two(self):
        return self._appid_out_two

    @appid_out_two.setter
    def appid_out_two(self, value):
        self._appid_out_two = value
    @property
    def appid_two(self):
        return self._appid_two

    @appid_two.setter
    def appid_two(self, value):
        self._appid_two = value
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
    def one_uid(self):
        return self._one_uid

    @one_uid.setter
    def one_uid(self, value):
        self._one_uid = value
    @property
    def one_uid_openid(self):
        return self._one_uid_openid

    @one_uid_openid.setter
    def one_uid_openid(self, value):
        self._one_uid_openid = value
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
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        if isinstance(value, OpenidComplex):
            self._test = value
        else:
            self._test = OpenidComplex.from_alipay_dict(value)
    @property
    def test_test(self):
        return self._test_test

    @test_test.setter
    def test_test(self, value):
        if isinstance(value, OpenidComplex):
            self._test_test = value
        else:
            self._test_test = OpenidComplex.from_alipay_dict(value)
    @property
    def two_uid(self):
        return self._two_uid

    @two_uid.setter
    def two_uid(self, value):
        self._two_uid = value
    @property
    def two_uid_openid(self):
        return self._two_uid_openid

    @two_uid_openid.setter
    def two_uid_openid(self, value):
        self._two_uid_openid = value
    @property
    def uid_one(self):
        return self._uid_one

    @uid_one.setter
    def uid_one(self, value):
        self._uid_one = value
    @property
    def uid_two(self):
        return self._uid_two

    @uid_two.setter
    def uid_two(self, value):
        self._uid_two = value
    @property
    def uidone_openid(self):
        return self._uidone_openid

    @uidone_openid.setter
    def uidone_openid(self, value):
        self._uidone_openid = value
    @property
    def uidtwo_openid(self):
        return self._uidtwo_openid

    @uidtwo_openid.setter
    def uidtwo_openid(self, value):
        self._uidtwo_openid = value


    def to_alipay_dict(self):
        params = dict()
        if self.a:
            if hasattr(self.a, 'to_alipay_dict'):
                params['a'] = self.a.to_alipay_dict()
            else:
                params['a'] = self.a
        if self.appid_one:
            if hasattr(self.appid_one, 'to_alipay_dict'):
                params['appid_one'] = self.appid_one.to_alipay_dict()
            else:
                params['appid_one'] = self.appid_one
        if self.appid_out_one:
            if hasattr(self.appid_out_one, 'to_alipay_dict'):
                params['appid_out_one'] = self.appid_out_one.to_alipay_dict()
            else:
                params['appid_out_one'] = self.appid_out_one
        if self.appid_out_two:
            if hasattr(self.appid_out_two, 'to_alipay_dict'):
                params['appid_out_two'] = self.appid_out_two.to_alipay_dict()
            else:
                params['appid_out_two'] = self.appid_out_two
        if self.appid_two:
            if hasattr(self.appid_two, 'to_alipay_dict'):
                params['appid_two'] = self.appid_two.to_alipay_dict()
            else:
                params['appid_two'] = self.appid_two
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
        if self.one_uid:
            if hasattr(self.one_uid, 'to_alipay_dict'):
                params['one_uid'] = self.one_uid.to_alipay_dict()
            else:
                params['one_uid'] = self.one_uid
        if self.one_uid_openid:
            if hasattr(self.one_uid_openid, 'to_alipay_dict'):
                params['one_uid_openid'] = self.one_uid_openid.to_alipay_dict()
            else:
                params['one_uid_openid'] = self.one_uid_openid
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
        if self.test:
            if hasattr(self.test, 'to_alipay_dict'):
                params['test'] = self.test.to_alipay_dict()
            else:
                params['test'] = self.test
        if self.test_test:
            if hasattr(self.test_test, 'to_alipay_dict'):
                params['test_test'] = self.test_test.to_alipay_dict()
            else:
                params['test_test'] = self.test_test
        if self.two_uid:
            if hasattr(self.two_uid, 'to_alipay_dict'):
                params['two_uid'] = self.two_uid.to_alipay_dict()
            else:
                params['two_uid'] = self.two_uid
        if self.two_uid_openid:
            if hasattr(self.two_uid_openid, 'to_alipay_dict'):
                params['two_uid_openid'] = self.two_uid_openid.to_alipay_dict()
            else:
                params['two_uid_openid'] = self.two_uid_openid
        if self.uid_one:
            if hasattr(self.uid_one, 'to_alipay_dict'):
                params['uid_one'] = self.uid_one.to_alipay_dict()
            else:
                params['uid_one'] = self.uid_one
        if self.uid_two:
            if hasattr(self.uid_two, 'to_alipay_dict'):
                params['uid_two'] = self.uid_two.to_alipay_dict()
            else:
                params['uid_two'] = self.uid_two
        if self.uidone_openid:
            if hasattr(self.uidone_openid, 'to_alipay_dict'):
                params['uidone_openid'] = self.uidone_openid.to_alipay_dict()
            else:
                params['uidone_openid'] = self.uidone_openid
        if self.uidtwo_openid:
            if hasattr(self.uidtwo_openid, 'to_alipay_dict'):
                params['uidtwo_openid'] = self.uidtwo_openid.to_alipay_dict()
            else:
                params['uidtwo_openid'] = self.uidtwo_openid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockTestparameterQueryModel()
        if 'a' in d:
            o.a = d['a']
        if 'appid_one' in d:
            o.appid_one = d['appid_one']
        if 'appid_out_one' in d:
            o.appid_out_one = d['appid_out_one']
        if 'appid_out_two' in d:
            o.appid_out_two = d['appid_out_two']
        if 'appid_two' in d:
            o.appid_two = d['appid_two']
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
        if 'one_uid' in d:
            o.one_uid = d['one_uid']
        if 'one_uid_openid' in d:
            o.one_uid_openid = d['one_uid_openid']
        if 'price' in d:
            o.price = d['price']
        if 'ss_list' in d:
            o.ss_list = d['ss_list']
        if 'test' in d:
            o.test = d['test']
        if 'test_test' in d:
            o.test_test = d['test_test']
        if 'two_uid' in d:
            o.two_uid = d['two_uid']
        if 'two_uid_openid' in d:
            o.two_uid_openid = d['two_uid_openid']
        if 'uid_one' in d:
            o.uid_one = d['uid_one']
        if 'uid_two' in d:
            o.uid_two = d['uid_two']
        if 'uidone_openid' in d:
            o.uidone_openid = d['uidone_openid']
        if 'uidtwo_openid' in d:
            o.uidtwo_openid = d['uidtwo_openid']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayGongyiAddressTest import AlipayGongyiAddressTest
from alipay.aop.api.domain.AlipayGongyiAddressTest import AlipayGongyiAddressTest


class AlipayGongyiUserInfoTest(object):

    def __init__(self):
        self._address = None
        self._age = None
        self._birthday = None
        self._citys = None
        self._code = None
        self._name = None
        self._school_list = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, AlipayGongyiAddressTest):
            self._address = value
        else:
            self._address = AlipayGongyiAddressTest.from_alipay_dict(value)
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def citys(self):
        return self._citys

    @citys.setter
    def citys(self, value):
        if isinstance(value, list):
            self._citys = list()
            for i in value:
                self._citys.append(i)
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def school_list(self):
        return self._school_list

    @school_list.setter
    def school_list(self, value):
        if isinstance(value, list):
            self._school_list = list()
            for i in value:
                if isinstance(i, AlipayGongyiAddressTest):
                    self._school_list.append(i)
                else:
                    self._school_list.append(AlipayGongyiAddressTest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.birthday:
            if hasattr(self.birthday, 'to_alipay_dict'):
                params['birthday'] = self.birthday.to_alipay_dict()
            else:
                params['birthday'] = self.birthday
        if self.citys:
            if isinstance(self.citys, list):
                for i in range(0, len(self.citys)):
                    element = self.citys[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.citys[i] = element.to_alipay_dict()
            if hasattr(self.citys, 'to_alipay_dict'):
                params['citys'] = self.citys.to_alipay_dict()
            else:
                params['citys'] = self.citys
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.school_list:
            if isinstance(self.school_list, list):
                for i in range(0, len(self.school_list)):
                    element = self.school_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.school_list[i] = element.to_alipay_dict()
            if hasattr(self.school_list, 'to_alipay_dict'):
                params['school_list'] = self.school_list.to_alipay_dict()
            else:
                params['school_list'] = self.school_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayGongyiUserInfoTest()
        if 'address' in d:
            o.address = d['address']
        if 'age' in d:
            o.age = d['age']
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'citys' in d:
            o.citys = d['citys']
        if 'code' in d:
            o.code = d['code']
        if 'name' in d:
            o.name = d['name']
        if 'school_list' in d:
            o.school_list = d['school_list']
        return o



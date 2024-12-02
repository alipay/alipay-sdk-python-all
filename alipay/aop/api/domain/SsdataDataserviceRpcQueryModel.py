#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceRpcQueryModel(object):

    def __init__(self):
        self._age = None
        self._name = None
        self._user = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, list):
            self._user = list()
            for i in value:
                self._user.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.user:
            if isinstance(self.user, list):
                for i in range(0, len(self.user)):
                    element = self.user[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user[i] = element.to_alipay_dict()
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceRpcQueryModel()
        if 'age' in d:
            o.age = d['age']
        if 'name' in d:
            o.name = d['name']
        if 'user' in d:
            o.user = d['user']
        return o



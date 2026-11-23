#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserName(object):

    def __init__(self):
        self._first_name = None
        self._full_name = None
        self._last_name = None
        self._middle_name = None

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        self._middle_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.first_name:
            if hasattr(self.first_name, 'to_alipay_dict'):
                params['first_name'] = self.first_name.to_alipay_dict()
            else:
                params['first_name'] = self.first_name
        if self.full_name:
            if hasattr(self.full_name, 'to_alipay_dict'):
                params['full_name'] = self.full_name.to_alipay_dict()
            else:
                params['full_name'] = self.full_name
        if self.last_name:
            if hasattr(self.last_name, 'to_alipay_dict'):
                params['last_name'] = self.last_name.to_alipay_dict()
            else:
                params['last_name'] = self.last_name
        if self.middle_name:
            if hasattr(self.middle_name, 'to_alipay_dict'):
                params['middle_name'] = self.middle_name.to_alipay_dict()
            else:
                params['middle_name'] = self.middle_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserName()
        if 'first_name' in d:
            o.first_name = d['first_name']
        if 'full_name' in d:
            o.full_name = d['full_name']
        if 'last_name' in d:
            o.last_name = d['last_name']
        if 'middle_name' in d:
            o.middle_name = d['middle_name']
        return o



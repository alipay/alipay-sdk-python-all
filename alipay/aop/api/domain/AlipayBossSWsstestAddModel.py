#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ManjiangTestComplexOneData import ManjiangTestComplexOneData
from alipay.aop.api.domain.ParamValidateTest import ParamValidateTest


class AlipayBossSWsstestAddModel(object):

    def __init__(self):
        self._address = None
        self._open_id = None
        self._sss = None
        self._sssdsds = None
        self._test_2 = None
        self._type = None
        self._user_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, ManjiangTestComplexOneData):
            self._address = value
        else:
            self._address = ManjiangTestComplexOneData.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def sss(self):
        return self._sss

    @sss.setter
    def sss(self, value):
        self._sss = value
    @property
    def sssdsds(self):
        return self._sssdsds

    @sssdsds.setter
    def sssdsds(self, value):
        self._sssdsds = value
    @property
    def test_2(self):
        return self._test_2

    @test_2.setter
    def test_2(self, value):
        if isinstance(value, ParamValidateTest):
            self._test_2 = value
        else:
            self._test_2 = ParamValidateTest.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.sss:
            if hasattr(self.sss, 'to_alipay_dict'):
                params['sss'] = self.sss.to_alipay_dict()
            else:
                params['sss'] = self.sss
        if self.sssdsds:
            if hasattr(self.sssdsds, 'to_alipay_dict'):
                params['sssdsds'] = self.sssdsds.to_alipay_dict()
            else:
                params['sssdsds'] = self.sssdsds
        if self.test_2:
            if hasattr(self.test_2, 'to_alipay_dict'):
                params['test_2'] = self.test_2.to_alipay_dict()
            else:
                params['test_2'] = self.test_2
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = AlipayBossSWsstestAddModel()
        if 'address' in d:
            o.address = d['address']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'sss' in d:
            o.sss = d['sss']
        if 'sssdsds' in d:
            o.sssdsds = d['sssdsds']
        if 'test_2' in d:
            o.test_2 = d['test_2']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



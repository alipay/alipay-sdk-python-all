#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyPublicForUploadTestComplexInfo import RainyPublicForUploadTestComplexInfo


class AlipayDataDataexchangeTreeapiuploadtestRainytestQueryModel(object):

    def __init__(self):
        self._choose = None
        self._choose_one_1 = None
        self._choose_one_2 = None
        self._demo = None
        self._open_id = None
        self._user_id = None

    @property
    def choose(self):
        return self._choose

    @choose.setter
    def choose(self, value):
        self._choose = value
    @property
    def choose_one_1(self):
        return self._choose_one_1

    @choose_one_1.setter
    def choose_one_1(self, value):
        self._choose_one_1 = value
    @property
    def choose_one_2(self):
        return self._choose_one_2

    @choose_one_2.setter
    def choose_one_2(self, value):
        self._choose_one_2 = value
    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, value):
        if isinstance(value, list):
            self._demo = list()
            for i in value:
                if isinstance(i, RainyPublicForUploadTestComplexInfo):
                    self._demo.append(i)
                else:
                    self._demo.append(RainyPublicForUploadTestComplexInfo.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.choose:
            if hasattr(self.choose, 'to_alipay_dict'):
                params['choose'] = self.choose.to_alipay_dict()
            else:
                params['choose'] = self.choose
        if self.choose_one_1:
            if hasattr(self.choose_one_1, 'to_alipay_dict'):
                params['choose_one_1'] = self.choose_one_1.to_alipay_dict()
            else:
                params['choose_one_1'] = self.choose_one_1
        if self.choose_one_2:
            if hasattr(self.choose_one_2, 'to_alipay_dict'):
                params['choose_one_2'] = self.choose_one_2.to_alipay_dict()
            else:
                params['choose_one_2'] = self.choose_one_2
        if self.demo:
            if isinstance(self.demo, list):
                for i in range(0, len(self.demo)):
                    element = self.demo[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.demo[i] = element.to_alipay_dict()
            if hasattr(self.demo, 'to_alipay_dict'):
                params['demo'] = self.demo.to_alipay_dict()
            else:
                params['demo'] = self.demo
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = AlipayDataDataexchangeTreeapiuploadtestRainytestQueryModel()
        if 'choose' in d:
            o.choose = d['choose']
        if 'choose_one_1' in d:
            o.choose_one_1 = d['choose_one_1']
        if 'choose_one_2' in d:
            o.choose_one_2 = d['choose_one_2']
        if 'demo' in d:
            o.demo = d['demo']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



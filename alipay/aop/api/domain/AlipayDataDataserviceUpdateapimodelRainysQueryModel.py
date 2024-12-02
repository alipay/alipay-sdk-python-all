#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceUpdateapimodelRainysQueryModel(object):

    def __init__(self):
        self._array_tc_1 = None
        self._rainy_test = None

    @property
    def array_tc_1(self):
        return self._array_tc_1

    @array_tc_1.setter
    def array_tc_1(self, value):
        if isinstance(value, list):
            self._array_tc_1 = list()
            for i in value:
                self._array_tc_1.append(i)
    @property
    def rainy_test(self):
        return self._rainy_test

    @rainy_test.setter
    def rainy_test(self, value):
        self._rainy_test = value


    def to_alipay_dict(self):
        params = dict()
        if self.array_tc_1:
            if isinstance(self.array_tc_1, list):
                for i in range(0, len(self.array_tc_1)):
                    element = self.array_tc_1[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.array_tc_1[i] = element.to_alipay_dict()
            if hasattr(self.array_tc_1, 'to_alipay_dict'):
                params['array_tc_1'] = self.array_tc_1.to_alipay_dict()
            else:
                params['array_tc_1'] = self.array_tc_1
        if self.rainy_test:
            if hasattr(self.rainy_test, 'to_alipay_dict'):
                params['rainy_test'] = self.rainy_test.to_alipay_dict()
            else:
                params['rainy_test'] = self.rainy_test
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceUpdateapimodelRainysQueryModel()
        if 'array_tc_1' in d:
            o.array_tc_1 = d['array_tc_1']
        if 'rainy_test' in d:
            o.rainy_test = d['rainy_test']
        return o



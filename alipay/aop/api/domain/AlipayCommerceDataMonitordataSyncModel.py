#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Datas import Datas


class AlipayCommerceDataMonitordataSyncModel(object):

    def __init__(self):
        self._datas = None
        self._interface_version = None
        self._product_code = None

    @property
    def datas(self):
        return self._datas

    @datas.setter
    def datas(self, value):
        if isinstance(value, list):
            self._datas = list()
            for i in value:
                if isinstance(i, Datas):
                    self._datas.append(i)
                else:
                    self._datas.append(Datas.from_alipay_dict(i))
    @property
    def interface_version(self):
        return self._interface_version

    @interface_version.setter
    def interface_version(self, value):
        self._interface_version = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.datas:
            if isinstance(self.datas, list):
                for i in range(0, len(self.datas)):
                    element = self.datas[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.datas[i] = element.to_alipay_dict()
            if hasattr(self.datas, 'to_alipay_dict'):
                params['datas'] = self.datas.to_alipay_dict()
            else:
                params['datas'] = self.datas
        if self.interface_version:
            if hasattr(self.interface_version, 'to_alipay_dict'):
                params['interface_version'] = self.interface_version.to_alipay_dict()
            else:
                params['interface_version'] = self.interface_version
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDataMonitordataSyncModel()
        if 'datas' in d:
            o.datas = d['datas']
        if 'interface_version' in d:
            o.interface_version = d['interface_version']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o



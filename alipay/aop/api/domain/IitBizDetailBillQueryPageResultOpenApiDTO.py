#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IitBizDetailBillDetailOpenApiDTO import IitBizDetailBillDetailOpenApiDTO


class IitBizDetailBillQueryPageResultOpenApiDTO(object):

    def __init__(self):
        self._calc_finish = None
        self._datas = None
        self._total_count = None

    @property
    def calc_finish(self):
        return self._calc_finish

    @calc_finish.setter
    def calc_finish(self, value):
        self._calc_finish = value
    @property
    def datas(self):
        return self._datas

    @datas.setter
    def datas(self, value):
        if isinstance(value, list):
            self._datas = list()
            for i in value:
                if isinstance(i, IitBizDetailBillDetailOpenApiDTO):
                    self._datas.append(i)
                else:
                    self._datas.append(IitBizDetailBillDetailOpenApiDTO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.calc_finish:
            if hasattr(self.calc_finish, 'to_alipay_dict'):
                params['calc_finish'] = self.calc_finish.to_alipay_dict()
            else:
                params['calc_finish'] = self.calc_finish
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
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IitBizDetailBillQueryPageResultOpenApiDTO()
        if 'calc_finish' in d:
            o.calc_finish = d['calc_finish']
        if 'datas' in d:
            o.datas = d['datas']
        if 'total_count' in d:
            o.total_count = d['total_count']
        return o



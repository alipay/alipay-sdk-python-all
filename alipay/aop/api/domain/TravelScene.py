#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TravelMallRequest import TravelMallRequest


class TravelScene(object):

    def __init__(self):
        self._data_list = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, TravelMallRequest):
                    self._data_list.append(i)
                else:
                    self._data_list.append(TravelMallRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.data_list:
            if isinstance(self.data_list, list):
                for i in range(0, len(self.data_list)):
                    element = self.data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data_list[i] = element.to_alipay_dict()
            if hasattr(self.data_list, 'to_alipay_dict'):
                params['data_list'] = self.data_list.to_alipay_dict()
            else:
                params['data_list'] = self.data_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TravelScene()
        if 'data_list' in d:
            o.data_list = d['data_list']
        return o



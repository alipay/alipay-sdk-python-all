#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppRentroomAreaDeleteModel(object):

    def __init__(self):
        self._area_id_list = None
        self._out_area_id_list = None

    @property
    def area_id_list(self):
        return self._area_id_list

    @area_id_list.setter
    def area_id_list(self, value):
        if isinstance(value, list):
            self._area_id_list = list()
            for i in value:
                self._area_id_list.append(i)
    @property
    def out_area_id_list(self):
        return self._out_area_id_list

    @out_area_id_list.setter
    def out_area_id_list(self, value):
        if isinstance(value, list):
            self._out_area_id_list = list()
            for i in value:
                self._out_area_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.area_id_list:
            if isinstance(self.area_id_list, list):
                for i in range(0, len(self.area_id_list)):
                    element = self.area_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.area_id_list[i] = element.to_alipay_dict()
            if hasattr(self.area_id_list, 'to_alipay_dict'):
                params['area_id_list'] = self.area_id_list.to_alipay_dict()
            else:
                params['area_id_list'] = self.area_id_list
        if self.out_area_id_list:
            if isinstance(self.out_area_id_list, list):
                for i in range(0, len(self.out_area_id_list)):
                    element = self.out_area_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_area_id_list[i] = element.to_alipay_dict()
            if hasattr(self.out_area_id_list, 'to_alipay_dict'):
                params['out_area_id_list'] = self.out_area_id_list.to_alipay_dict()
            else:
                params['out_area_id_list'] = self.out_area_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppRentroomAreaDeleteModel()
        if 'area_id_list' in d:
            o.area_id_list = d['area_id_list']
        if 'out_area_id_list' in d:
            o.out_area_id_list = d['out_area_id_list']
        return o



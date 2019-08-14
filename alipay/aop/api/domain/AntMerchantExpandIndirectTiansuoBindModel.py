#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TiansuoIsvBindVO import TiansuoIsvBindVO


class AntMerchantExpandIndirectTiansuoBindModel(object):

    def __init__(self):
        self._tiansuo_isv_bind_list = None

    @property
    def tiansuo_isv_bind_list(self):
        return self._tiansuo_isv_bind_list

    @tiansuo_isv_bind_list.setter
    def tiansuo_isv_bind_list(self, value):
        if isinstance(value, list):
            self._tiansuo_isv_bind_list = list()
            for i in value:
                if isinstance(i, TiansuoIsvBindVO):
                    self._tiansuo_isv_bind_list.append(i)
                else:
                    self._tiansuo_isv_bind_list.append(TiansuoIsvBindVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.tiansuo_isv_bind_list:
            if isinstance(self.tiansuo_isv_bind_list, list):
                for i in range(0, len(self.tiansuo_isv_bind_list)):
                    element = self.tiansuo_isv_bind_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tiansuo_isv_bind_list[i] = element.to_alipay_dict()
            if hasattr(self.tiansuo_isv_bind_list, 'to_alipay_dict'):
                params['tiansuo_isv_bind_list'] = self.tiansuo_isv_bind_list.to_alipay_dict()
            else:
                params['tiansuo_isv_bind_list'] = self.tiansuo_isv_bind_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIndirectTiansuoBindModel()
        if 'tiansuo_isv_bind_list' in d:
            o.tiansuo_isv_bind_list = d['tiansuo_isv_bind_list']
        return o



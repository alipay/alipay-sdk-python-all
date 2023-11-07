#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TgiTagVO(object):

    def __init__(self):
        self._tgi_name_list = None

    @property
    def tgi_name_list(self):
        return self._tgi_name_list

    @tgi_name_list.setter
    def tgi_name_list(self, value):
        if isinstance(value, list):
            self._tgi_name_list = list()
            for i in value:
                self._tgi_name_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.tgi_name_list:
            if isinstance(self.tgi_name_list, list):
                for i in range(0, len(self.tgi_name_list)):
                    element = self.tgi_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tgi_name_list[i] = element.to_alipay_dict()
            if hasattr(self.tgi_name_list, 'to_alipay_dict'):
                params['tgi_name_list'] = self.tgi_name_list.to_alipay_dict()
            else:
                params['tgi_name_list'] = self.tgi_name_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TgiTagVO()
        if 'tgi_name_list' in d:
            o.tgi_name_list = d['tgi_name_list']
        return o



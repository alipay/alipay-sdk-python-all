#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSearchboxBusinessdistrictQueryModel(object):

    def __init__(self):
        self._brand_id = None
        self._relate_appid_list = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def relate_appid_list(self):
        return self._relate_appid_list

    @relate_appid_list.setter
    def relate_appid_list(self, value):
        if isinstance(value, list):
            self._relate_appid_list = list()
            for i in value:
                self._relate_appid_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.relate_appid_list:
            if isinstance(self.relate_appid_list, list):
                for i in range(0, len(self.relate_appid_list)):
                    element = self.relate_appid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.relate_appid_list[i] = element.to_alipay_dict()
            if hasattr(self.relate_appid_list, 'to_alipay_dict'):
                params['relate_appid_list'] = self.relate_appid_list.to_alipay_dict()
            else:
                params['relate_appid_list'] = self.relate_appid_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSearchboxBusinessdistrictQueryModel()
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'relate_appid_list' in d:
            o.relate_appid_list = d['relate_appid_list']
        return o



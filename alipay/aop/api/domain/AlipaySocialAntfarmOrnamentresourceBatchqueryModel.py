#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialAntfarmOrnamentresourceBatchqueryModel(object):

    def __init__(self):
        self._ornament_resource_key_list = None

    @property
    def ornament_resource_key_list(self):
        return self._ornament_resource_key_list

    @ornament_resource_key_list.setter
    def ornament_resource_key_list(self, value):
        if isinstance(value, list):
            self._ornament_resource_key_list = list()
            for i in value:
                self._ornament_resource_key_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.ornament_resource_key_list:
            if isinstance(self.ornament_resource_key_list, list):
                for i in range(0, len(self.ornament_resource_key_list)):
                    element = self.ornament_resource_key_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ornament_resource_key_list[i] = element.to_alipay_dict()
            if hasattr(self.ornament_resource_key_list, 'to_alipay_dict'):
                params['ornament_resource_key_list'] = self.ornament_resource_key_list.to_alipay_dict()
            else:
                params['ornament_resource_key_list'] = self.ornament_resource_key_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialAntfarmOrnamentresourceBatchqueryModel()
        if 'ornament_resource_key_list' in d:
            o.ornament_resource_key_list = d['ornament_resource_key_list']
        return o



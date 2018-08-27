#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiRetailInstanceTransferModel(object):

    def __init__(self):
        self._instance_id_list = None
        self._instance_type = None

    @property
    def instance_id_list(self):
        return self._instance_id_list

    @instance_id_list.setter
    def instance_id_list(self, value):
        if isinstance(value, list):
            self._instance_id_list = list()
            for i in value:
                self._instance_id_list.append(i)
    @property
    def instance_type(self):
        return self._instance_type

    @instance_type.setter
    def instance_type(self, value):
        self._instance_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.instance_id_list:
            if isinstance(self.instance_id_list, list):
                for i in range(0, len(self.instance_id_list)):
                    element = self.instance_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.instance_id_list[i] = element.to_alipay_dict()
            if hasattr(self.instance_id_list, 'to_alipay_dict'):
                params['instance_id_list'] = self.instance_id_list.to_alipay_dict()
            else:
                params['instance_id_list'] = self.instance_id_list
        if self.instance_type:
            if hasattr(self.instance_type, 'to_alipay_dict'):
                params['instance_type'] = self.instance_type.to_alipay_dict()
            else:
                params['instance_type'] = self.instance_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailInstanceTransferModel()
        if 'instance_id_list' in d:
            o.instance_id_list = d['instance_id_list']
        if 'instance_type' in d:
            o.instance_type = d['instance_type']
        return o



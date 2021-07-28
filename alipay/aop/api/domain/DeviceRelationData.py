#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceRelationData(object):

    def __init__(self):
        self._plan_id_list = None
        self._sn = None

    @property
    def plan_id_list(self):
        return self._plan_id_list

    @plan_id_list.setter
    def plan_id_list(self, value):
        if isinstance(value, list):
            self._plan_id_list = list()
            for i in value:
                self._plan_id_list.append(i)
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.plan_id_list:
            if isinstance(self.plan_id_list, list):
                for i in range(0, len(self.plan_id_list)):
                    element = self.plan_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plan_id_list[i] = element.to_alipay_dict()
            if hasattr(self.plan_id_list, 'to_alipay_dict'):
                params['plan_id_list'] = self.plan_id_list.to_alipay_dict()
            else:
                params['plan_id_list'] = self.plan_id_list
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceRelationData()
        if 'plan_id_list' in d:
            o.plan_id_list = d['plan_id_list']
        if 'sn' in d:
            o.sn = d['sn']
        return o



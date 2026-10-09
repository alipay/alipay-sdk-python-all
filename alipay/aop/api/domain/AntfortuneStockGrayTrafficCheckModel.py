#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneStockGrayTrafficCheckModel(object):

    def __init__(self):
        self._applications = None
        self._inst_id = None

    @property
    def applications(self):
        return self._applications

    @applications.setter
    def applications(self, value):
        if isinstance(value, list):
            self._applications = list()
            for i in value:
                self._applications.append(i)
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.applications:
            if isinstance(self.applications, list):
                for i in range(0, len(self.applications)):
                    element = self.applications[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.applications[i] = element.to_alipay_dict()
            if hasattr(self.applications, 'to_alipay_dict'):
                params['applications'] = self.applications.to_alipay_dict()
            else:
                params['applications'] = self.applications
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockGrayTrafficCheckModel()
        if 'applications' in d:
            o.applications = d['applications']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        return o



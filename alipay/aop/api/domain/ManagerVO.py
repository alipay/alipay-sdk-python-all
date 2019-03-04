#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ManagerVO(object):

    def __init__(self):
        self._manager_name = None
        self._manager_position = None

    @property
    def manager_name(self):
        return self._manager_name

    @manager_name.setter
    def manager_name(self, value):
        self._manager_name = value
    @property
    def manager_position(self):
        return self._manager_position

    @manager_position.setter
    def manager_position(self, value):
        self._manager_position = value


    def to_alipay_dict(self):
        params = dict()
        if self.manager_name:
            if hasattr(self.manager_name, 'to_alipay_dict'):
                params['manager_name'] = self.manager_name.to_alipay_dict()
            else:
                params['manager_name'] = self.manager_name
        if self.manager_position:
            if hasattr(self.manager_position, 'to_alipay_dict'):
                params['manager_position'] = self.manager_position.to_alipay_dict()
            else:
                params['manager_position'] = self.manager_position
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ManagerVO()
        if 'manager_name' in d:
            o.manager_name = d['manager_name']
        if 'manager_position' in d:
            o.manager_position = d['manager_position']
        return o



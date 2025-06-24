#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StaffInfoVO import StaffInfoVO


class AlipayCommercePropertyStaffSaveModel(object):

    def __init__(self):
        self._action = None
        self._list = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, list):
            self._list = list()
            for i in value:
                if isinstance(i, StaffInfoVO):
                    self._list.append(i)
                else:
                    self._list.append(StaffInfoVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.list:
            if isinstance(self.list, list):
                for i in range(0, len(self.list)):
                    element = self.list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.list[i] = element.to_alipay_dict()
            if hasattr(self.list, 'to_alipay_dict'):
                params['list'] = self.list.to_alipay_dict()
            else:
                params['list'] = self.list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommercePropertyStaffSaveModel()
        if 'action' in d:
            o.action = d['action']
        if 'list' in d:
            o.list = d['list']
        return o



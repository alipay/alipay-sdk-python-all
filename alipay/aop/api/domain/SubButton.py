#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubButton(object):

    def __init__(self):
        self._action_param = None
        self._action_type = None
        self._icon = None
        self._name = None

    @property
    def action_param(self):
        return self._action_param

    @action_param.setter
    def action_param(self, value):
        self._action_param = value
    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_param:
            if hasattr(self.action_param, 'to_alipay_dict'):
                params['action_param'] = self.action_param.to_alipay_dict()
            else:
                params['action_param'] = self.action_param
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubButton()
        if 'action_param' in d:
            o.action_param = d['action_param']
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'icon' in d:
            o.icon = d['icon']
        if 'name' in d:
            o.name = d['name']
        return o



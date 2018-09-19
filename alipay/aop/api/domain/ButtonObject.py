#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubButton import SubButton


class ButtonObject(object):

    def __init__(self):
        self._action_param = None
        self._action_type = None
        self._icon = None
        self._name = None
        self._sub_button = None

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
    @property
    def sub_button(self):
        return self._sub_button

    @sub_button.setter
    def sub_button(self, value):
        if isinstance(value, list):
            self._sub_button = list()
            for i in value:
                if isinstance(i, SubButton):
                    self._sub_button.append(i)
                else:
                    self._sub_button.append(SubButton.from_alipay_dict(i))


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
        if self.sub_button:
            if isinstance(self.sub_button, list):
                for i in range(0, len(self.sub_button)):
                    element = self.sub_button[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_button[i] = element.to_alipay_dict()
            if hasattr(self.sub_button, 'to_alipay_dict'):
                params['sub_button'] = self.sub_button.to_alipay_dict()
            else:
                params['sub_button'] = self.sub_button
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ButtonObject()
        if 'action_param' in d:
            o.action_param = d['action_param']
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'icon' in d:
            o.icon = d['icon']
        if 'name' in d:
            o.name = d['name']
        if 'sub_button' in d:
            o.sub_button = d['sub_button']
        return o



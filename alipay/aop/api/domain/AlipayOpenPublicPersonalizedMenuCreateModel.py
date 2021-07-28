#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ButtonObject import ButtonObject
from alipay.aop.api.domain.LabelRule import LabelRule


class AlipayOpenPublicPersonalizedMenuCreateModel(object):

    def __init__(self):
        self._button = None
        self._group_id = None
        self._label_rule = None
        self._mobile_client_type = None
        self._type = None

    @property
    def button(self):
        return self._button

    @button.setter
    def button(self, value):
        if isinstance(value, list):
            self._button = list()
            for i in value:
                if isinstance(i, ButtonObject):
                    self._button.append(i)
                else:
                    self._button.append(ButtonObject.from_alipay_dict(i))
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def label_rule(self):
        return self._label_rule

    @label_rule.setter
    def label_rule(self, value):
        if isinstance(value, list):
            self._label_rule = list()
            for i in value:
                if isinstance(i, LabelRule):
                    self._label_rule.append(i)
                else:
                    self._label_rule.append(LabelRule.from_alipay_dict(i))
    @property
    def mobile_client_type(self):
        return self._mobile_client_type

    @mobile_client_type.setter
    def mobile_client_type(self, value):
        self._mobile_client_type = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.button:
            if isinstance(self.button, list):
                for i in range(0, len(self.button)):
                    element = self.button[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.button[i] = element.to_alipay_dict()
            if hasattr(self.button, 'to_alipay_dict'):
                params['button'] = self.button.to_alipay_dict()
            else:
                params['button'] = self.button
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.label_rule:
            if isinstance(self.label_rule, list):
                for i in range(0, len(self.label_rule)):
                    element = self.label_rule[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.label_rule[i] = element.to_alipay_dict()
            if hasattr(self.label_rule, 'to_alipay_dict'):
                params['label_rule'] = self.label_rule.to_alipay_dict()
            else:
                params['label_rule'] = self.label_rule
        if self.mobile_client_type:
            if hasattr(self.mobile_client_type, 'to_alipay_dict'):
                params['mobile_client_type'] = self.mobile_client_type.to_alipay_dict()
            else:
                params['mobile_client_type'] = self.mobile_client_type
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicPersonalizedMenuCreateModel()
        if 'button' in d:
            o.button = d['button']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'label_rule' in d:
            o.label_rule = d['label_rule']
        if 'mobile_client_type' in d:
            o.mobile_client_type = d['mobile_client_type']
        if 'type' in d:
            o.type = d['type']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpLabelContent(object):

    def __init__(self):
        self._label_category = None
        self._label_code = None
        self._label_definition = None
        self._label_emotion = None
        self._label_name = None
        self._label_value = None

    @property
    def label_category(self):
        return self._label_category

    @label_category.setter
    def label_category(self, value):
        self._label_category = value
    @property
    def label_code(self):
        return self._label_code

    @label_code.setter
    def label_code(self, value):
        self._label_code = value
    @property
    def label_definition(self):
        return self._label_definition

    @label_definition.setter
    def label_definition(self, value):
        self._label_definition = value
    @property
    def label_emotion(self):
        return self._label_emotion

    @label_emotion.setter
    def label_emotion(self, value):
        self._label_emotion = value
    @property
    def label_name(self):
        return self._label_name

    @label_name.setter
    def label_name(self, value):
        self._label_name = value
    @property
    def label_value(self):
        return self._label_value

    @label_value.setter
    def label_value(self, value):
        if isinstance(value, list):
            self._label_value = list()
            for i in value:
                self._label_value.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.label_category:
            if hasattr(self.label_category, 'to_alipay_dict'):
                params['label_category'] = self.label_category.to_alipay_dict()
            else:
                params['label_category'] = self.label_category
        if self.label_code:
            if hasattr(self.label_code, 'to_alipay_dict'):
                params['label_code'] = self.label_code.to_alipay_dict()
            else:
                params['label_code'] = self.label_code
        if self.label_definition:
            if hasattr(self.label_definition, 'to_alipay_dict'):
                params['label_definition'] = self.label_definition.to_alipay_dict()
            else:
                params['label_definition'] = self.label_definition
        if self.label_emotion:
            if hasattr(self.label_emotion, 'to_alipay_dict'):
                params['label_emotion'] = self.label_emotion.to_alipay_dict()
            else:
                params['label_emotion'] = self.label_emotion
        if self.label_name:
            if hasattr(self.label_name, 'to_alipay_dict'):
                params['label_name'] = self.label_name.to_alipay_dict()
            else:
                params['label_name'] = self.label_name
        if self.label_value:
            if isinstance(self.label_value, list):
                for i in range(0, len(self.label_value)):
                    element = self.label_value[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.label_value[i] = element.to_alipay_dict()
            if hasattr(self.label_value, 'to_alipay_dict'):
                params['label_value'] = self.label_value.to_alipay_dict()
            else:
                params['label_value'] = self.label_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpLabelContent()
        if 'label_category' in d:
            o.label_category = d['label_category']
        if 'label_code' in d:
            o.label_code = d['label_code']
        if 'label_definition' in d:
            o.label_definition = d['label_definition']
        if 'label_emotion' in d:
            o.label_emotion = d['label_emotion']
        if 'label_name' in d:
            o.label_name = d['label_name']
        if 'label_value' in d:
            o.label_value = d['label_value']
        return o



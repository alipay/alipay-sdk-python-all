#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NewsConcernedLabel import NewsConcernedLabel


class NewsConcerned(object):

    def __init__(self):
        self._has_id = None
        self._id = None
        self._label = None
        self._name = None

    @property
    def has_id(self):
        return self._has_id

    @has_id.setter
    def has_id(self, value):
        self._has_id = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        if isinstance(value, list):
            self._label = list()
            for i in value:
                if isinstance(i, NewsConcernedLabel):
                    self._label.append(i)
                else:
                    self._label.append(NewsConcernedLabel.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.has_id:
            if hasattr(self.has_id, 'to_alipay_dict'):
                params['has_id'] = self.has_id.to_alipay_dict()
            else:
                params['has_id'] = self.has_id
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.label:
            if isinstance(self.label, list):
                for i in range(0, len(self.label)):
                    element = self.label[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.label[i] = element.to_alipay_dict()
            if hasattr(self.label, 'to_alipay_dict'):
                params['label'] = self.label.to_alipay_dict()
            else:
                params['label'] = self.label
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
        o = NewsConcerned()
        if 'has_id' in d:
            o.has_id = d['has_id']
        if 'id' in d:
            o.id = d['id']
        if 'label' in d:
            o.label = d['label']
        if 'name' in d:
            o.name = d['name']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtensionArea import ExtensionArea
from alipay.aop.api.domain.QueryLabelRule import QueryLabelRule


class QueryExtension(object):

    def __init__(self):
        self._areas = None
        self._extension_key = None
        self._label_rules = None
        self._status = None

    @property
    def areas(self):
        return self._areas

    @areas.setter
    def areas(self, value):
        if isinstance(value, list):
            self._areas = list()
            for i in value:
                if isinstance(i, ExtensionArea):
                    self._areas.append(i)
                else:
                    self._areas.append(ExtensionArea.from_alipay_dict(i))
    @property
    def extension_key(self):
        return self._extension_key

    @extension_key.setter
    def extension_key(self, value):
        self._extension_key = value
    @property
    def label_rules(self):
        return self._label_rules

    @label_rules.setter
    def label_rules(self, value):
        if isinstance(value, list):
            self._label_rules = list()
            for i in value:
                if isinstance(i, QueryLabelRule):
                    self._label_rules.append(i)
                else:
                    self._label_rules.append(QueryLabelRule.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.areas:
            if isinstance(self.areas, list):
                for i in range(0, len(self.areas)):
                    element = self.areas[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.areas[i] = element.to_alipay_dict()
            if hasattr(self.areas, 'to_alipay_dict'):
                params['areas'] = self.areas.to_alipay_dict()
            else:
                params['areas'] = self.areas
        if self.extension_key:
            if hasattr(self.extension_key, 'to_alipay_dict'):
                params['extension_key'] = self.extension_key.to_alipay_dict()
            else:
                params['extension_key'] = self.extension_key
        if self.label_rules:
            if isinstance(self.label_rules, list):
                for i in range(0, len(self.label_rules)):
                    element = self.label_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.label_rules[i] = element.to_alipay_dict()
            if hasattr(self.label_rules, 'to_alipay_dict'):
                params['label_rules'] = self.label_rules.to_alipay_dict()
            else:
                params['label_rules'] = self.label_rules
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryExtension()
        if 'areas' in d:
            o.areas = d['areas']
        if 'extension_key' in d:
            o.extension_key = d['extension_key']
        if 'label_rules' in d:
            o.label_rules = d['label_rules']
        if 'status' in d:
            o.status = d['status']
        return o



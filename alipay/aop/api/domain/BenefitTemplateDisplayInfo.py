#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitTemplateDisplayInfo(object):

    def __init__(self):
        self._activity_desc = None
        self._activity_name = None
        self._activity_rule_desc = None

    @property
    def activity_desc(self):
        return self._activity_desc

    @activity_desc.setter
    def activity_desc(self, value):
        self._activity_desc = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_rule_desc(self):
        return self._activity_rule_desc

    @activity_rule_desc.setter
    def activity_rule_desc(self, value):
        self._activity_rule_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_desc:
            if hasattr(self.activity_desc, 'to_alipay_dict'):
                params['activity_desc'] = self.activity_desc.to_alipay_dict()
            else:
                params['activity_desc'] = self.activity_desc
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.activity_rule_desc:
            if hasattr(self.activity_rule_desc, 'to_alipay_dict'):
                params['activity_rule_desc'] = self.activity_rule_desc.to_alipay_dict()
            else:
                params['activity_rule_desc'] = self.activity_rule_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitTemplateDisplayInfo()
        if 'activity_desc' in d:
            o.activity_desc = d['activity_desc']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_rule_desc' in d:
            o.activity_rule_desc = d['activity_rule_desc']
        return o



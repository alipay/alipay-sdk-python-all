#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FengdieSitesCreateModel import FengdieSitesCreateModel


class AlipayMarketingToolFengdieSitesCreateModel(object):

    def __init__(self):
        self._activity = None
        self._operator = None
        self._space_id = None
        self._template_name = None

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, value):
        if isinstance(value, FengdieSitesCreateModel):
            self._activity = value
        else:
            self._activity = FengdieSitesCreateModel.from_alipay_dict(value)
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def space_id(self):
        return self._space_id

    @space_id.setter
    def space_id(self, value):
        self._space_id = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity:
            if hasattr(self.activity, 'to_alipay_dict'):
                params['activity'] = self.activity.to_alipay_dict()
            else:
                params['activity'] = self.activity
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.space_id:
            if hasattr(self.space_id, 'to_alipay_dict'):
                params['space_id'] = self.space_id.to_alipay_dict()
            else:
                params['space_id'] = self.space_id
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingToolFengdieSitesCreateModel()
        if 'activity' in d:
            o.activity = d['activity']
        if 'operator' in d:
            o.operator = d['operator']
        if 'space_id' in d:
            o.space_id = d['space_id']
        if 'template_name' in d:
            o.template_name = d['template_name']
        return o



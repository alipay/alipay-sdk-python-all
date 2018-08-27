#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FengdieActivityCreateData import FengdieActivityCreateData


class AlipayMarketingToolFengdieActivityCreateModel(object):

    def __init__(self):
        self._activity = None
        self._template_id = None

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, value):
        if isinstance(value, FengdieActivityCreateData):
            self._activity = value
        else:
            self._activity = FengdieActivityCreateData.from_alipay_dict(value)
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity:
            if hasattr(self.activity, 'to_alipay_dict'):
                params['activity'] = self.activity.to_alipay_dict()
            else:
                params['activity'] = self.activity
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingToolFengdieActivityCreateModel()
        if 'activity' in d:
            o.activity = d['activity']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o



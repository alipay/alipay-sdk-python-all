#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingToolFengdieEditorGetModel(object):

    def __init__(self):
        self._activity_id = None
        self._operator = None
        self._redirect_url = None
        self._space_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def space_id(self):
        return self._space_id

    @space_id.setter
    def space_id(self, value):
        self._space_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        if self.space_id:
            if hasattr(self.space_id, 'to_alipay_dict'):
                params['space_id'] = self.space_id.to_alipay_dict()
            else:
                params['space_id'] = self.space_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingToolFengdieEditorGetModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'operator' in d:
            o.operator = d['operator']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'space_id' in d:
            o.space_id = d['space_id']
        return o



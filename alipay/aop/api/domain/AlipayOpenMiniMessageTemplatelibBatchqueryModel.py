#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniMessageTemplatelibBatchqueryModel(object):

    def __init__(self):
        self._has_push = None
        self._industry_code = None
        self._industry_scenario = None
        self._page_num = None
        self._page_size = None
        self._scene_rule = None

    @property
    def has_push(self):
        return self._has_push

    @has_push.setter
    def has_push(self, value):
        self._has_push = value
    @property
    def industry_code(self):
        return self._industry_code

    @industry_code.setter
    def industry_code(self, value):
        self._industry_code = value
    @property
    def industry_scenario(self):
        return self._industry_scenario

    @industry_scenario.setter
    def industry_scenario(self, value):
        self._industry_scenario = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def scene_rule(self):
        return self._scene_rule

    @scene_rule.setter
    def scene_rule(self, value):
        self._scene_rule = value


    def to_alipay_dict(self):
        params = dict()
        if self.has_push:
            if hasattr(self.has_push, 'to_alipay_dict'):
                params['has_push'] = self.has_push.to_alipay_dict()
            else:
                params['has_push'] = self.has_push
        if self.industry_code:
            if hasattr(self.industry_code, 'to_alipay_dict'):
                params['industry_code'] = self.industry_code.to_alipay_dict()
            else:
                params['industry_code'] = self.industry_code
        if self.industry_scenario:
            if hasattr(self.industry_scenario, 'to_alipay_dict'):
                params['industry_scenario'] = self.industry_scenario.to_alipay_dict()
            else:
                params['industry_scenario'] = self.industry_scenario
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.scene_rule:
            if hasattr(self.scene_rule, 'to_alipay_dict'):
                params['scene_rule'] = self.scene_rule.to_alipay_dict()
            else:
                params['scene_rule'] = self.scene_rule
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniMessageTemplatelibBatchqueryModel()
        if 'has_push' in d:
            o.has_push = d['has_push']
        if 'industry_code' in d:
            o.industry_code = d['industry_code']
        if 'industry_scenario' in d:
            o.industry_scenario = d['industry_scenario']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'scene_rule' in d:
            o.scene_rule = d['scene_rule']
        return o



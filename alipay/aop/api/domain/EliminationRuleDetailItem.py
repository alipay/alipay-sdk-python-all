#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EliminationRuleDetailItem(object):

    def __init__(self):
        self._biz_id = None
        self._check_metric = None
        self._desc = None
        self._rule_id = None
        self._rule_name = None
        self._rule_qualified = None
        self._stage_name = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def check_metric(self):
        return self._check_metric

    @check_metric.setter
    def check_metric(self, value):
        self._check_metric = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value
    @property
    def rule_qualified(self):
        return self._rule_qualified

    @rule_qualified.setter
    def rule_qualified(self, value):
        self._rule_qualified = value
    @property
    def stage_name(self):
        return self._stage_name

    @stage_name.setter
    def stage_name(self, value):
        self._stage_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.check_metric:
            if hasattr(self.check_metric, 'to_alipay_dict'):
                params['check_metric'] = self.check_metric.to_alipay_dict()
            else:
                params['check_metric'] = self.check_metric
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
        if self.rule_qualified:
            if hasattr(self.rule_qualified, 'to_alipay_dict'):
                params['rule_qualified'] = self.rule_qualified.to_alipay_dict()
            else:
                params['rule_qualified'] = self.rule_qualified
        if self.stage_name:
            if hasattr(self.stage_name, 'to_alipay_dict'):
                params['stage_name'] = self.stage_name.to_alipay_dict()
            else:
                params['stage_name'] = self.stage_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EliminationRuleDetailItem()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'check_metric' in d:
            o.check_metric = d['check_metric']
        if 'desc' in d:
            o.desc = d['desc']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'rule_qualified' in d:
            o.rule_qualified = d['rule_qualified']
        if 'stage_name' in d:
            o.stage_name = d['stage_name']
        return o



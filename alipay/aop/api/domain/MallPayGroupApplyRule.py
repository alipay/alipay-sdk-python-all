#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MallPayGroupApplyRule(object):

    def __init__(self):
        self._biz_rule_id = None
        self._biz_rule_name = None
        self._biz_rule_type = None
        self._status = None

    @property
    def biz_rule_id(self):
        return self._biz_rule_id

    @biz_rule_id.setter
    def biz_rule_id(self, value):
        self._biz_rule_id = value
    @property
    def biz_rule_name(self):
        return self._biz_rule_name

    @biz_rule_name.setter
    def biz_rule_name(self, value):
        self._biz_rule_name = value
    @property
    def biz_rule_type(self):
        return self._biz_rule_type

    @biz_rule_type.setter
    def biz_rule_type(self, value):
        self._biz_rule_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_rule_id:
            if hasattr(self.biz_rule_id, 'to_alipay_dict'):
                params['biz_rule_id'] = self.biz_rule_id.to_alipay_dict()
            else:
                params['biz_rule_id'] = self.biz_rule_id
        if self.biz_rule_name:
            if hasattr(self.biz_rule_name, 'to_alipay_dict'):
                params['biz_rule_name'] = self.biz_rule_name.to_alipay_dict()
            else:
                params['biz_rule_name'] = self.biz_rule_name
        if self.biz_rule_type:
            if hasattr(self.biz_rule_type, 'to_alipay_dict'):
                params['biz_rule_type'] = self.biz_rule_type.to_alipay_dict()
            else:
                params['biz_rule_type'] = self.biz_rule_type
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
        o = MallPayGroupApplyRule()
        if 'biz_rule_id' in d:
            o.biz_rule_id = d['biz_rule_id']
        if 'biz_rule_name' in d:
            o.biz_rule_name = d['biz_rule_name']
        if 'biz_rule_type' in d:
            o.biz_rule_type = d['biz_rule_type']
        if 'status' in d:
            o.status = d['status']
        return o



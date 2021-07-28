#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishGroupDetailSimplifyInfo import KbdishGroupDetailSimplifyInfo


class KbdishGroupSimplifyInfo(object):

    def __init__(self):
        self._activity_info = None
        self._group_detail_list = None
        self._group_rule = None
        self._name = None

    @property
    def activity_info(self):
        return self._activity_info

    @activity_info.setter
    def activity_info(self, value):
        self._activity_info = value
    @property
    def group_detail_list(self):
        return self._group_detail_list

    @group_detail_list.setter
    def group_detail_list(self, value):
        if isinstance(value, list):
            self._group_detail_list = list()
            for i in value:
                if isinstance(i, KbdishGroupDetailSimplifyInfo):
                    self._group_detail_list.append(i)
                else:
                    self._group_detail_list.append(KbdishGroupDetailSimplifyInfo.from_alipay_dict(i))
    @property
    def group_rule(self):
        return self._group_rule

    @group_rule.setter
    def group_rule(self, value):
        self._group_rule = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_info:
            if hasattr(self.activity_info, 'to_alipay_dict'):
                params['activity_info'] = self.activity_info.to_alipay_dict()
            else:
                params['activity_info'] = self.activity_info
        if self.group_detail_list:
            if isinstance(self.group_detail_list, list):
                for i in range(0, len(self.group_detail_list)):
                    element = self.group_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.group_detail_list, 'to_alipay_dict'):
                params['group_detail_list'] = self.group_detail_list.to_alipay_dict()
            else:
                params['group_detail_list'] = self.group_detail_list
        if self.group_rule:
            if hasattr(self.group_rule, 'to_alipay_dict'):
                params['group_rule'] = self.group_rule.to_alipay_dict()
            else:
                params['group_rule'] = self.group_rule
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
        o = KbdishGroupSimplifyInfo()
        if 'activity_info' in d:
            o.activity_info = d['activity_info']
        if 'group_detail_list' in d:
            o.group_detail_list = d['group_detail_list']
        if 'group_rule' in d:
            o.group_rule = d['group_rule']
        if 'name' in d:
            o.name = d['name']
        return o



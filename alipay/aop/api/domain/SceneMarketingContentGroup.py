#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SceneMarketingContent import SceneMarketingContent


class SceneMarketingContentGroup(object):

    def __init__(self):
        self._data_list = None
        self._group_name = None
        self._summary = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, SceneMarketingContent):
                    self._data_list.append(i)
                else:
                    self._data_list.append(SceneMarketingContent.from_alipay_dict(i))
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_list:
            if isinstance(self.data_list, list):
                for i in range(0, len(self.data_list)):
                    element = self.data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data_list[i] = element.to_alipay_dict()
            if hasattr(self.data_list, 'to_alipay_dict'):
                params['data_list'] = self.data_list.to_alipay_dict()
            else:
                params['data_list'] = self.data_list
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneMarketingContentGroup()
        if 'data_list' in d:
            o.data_list = d['data_list']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'summary' in d:
            o.summary = d['summary']
        return o



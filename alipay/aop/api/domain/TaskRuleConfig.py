#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TaskGoodConfig import TaskGoodConfig


class TaskRuleConfig(object):

    def __init__(self):
        self._good_list = None
        self._scene_tag_list = None

    @property
    def good_list(self):
        return self._good_list

    @good_list.setter
    def good_list(self, value):
        if isinstance(value, list):
            self._good_list = list()
            for i in value:
                if isinstance(i, TaskGoodConfig):
                    self._good_list.append(i)
                else:
                    self._good_list.append(TaskGoodConfig.from_alipay_dict(i))
    @property
    def scene_tag_list(self):
        return self._scene_tag_list

    @scene_tag_list.setter
    def scene_tag_list(self, value):
        if isinstance(value, list):
            self._scene_tag_list = list()
            for i in value:
                self._scene_tag_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.good_list:
            if isinstance(self.good_list, list):
                for i in range(0, len(self.good_list)):
                    element = self.good_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.good_list[i] = element.to_alipay_dict()
            if hasattr(self.good_list, 'to_alipay_dict'):
                params['good_list'] = self.good_list.to_alipay_dict()
            else:
                params['good_list'] = self.good_list
        if self.scene_tag_list:
            if isinstance(self.scene_tag_list, list):
                for i in range(0, len(self.scene_tag_list)):
                    element = self.scene_tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_tag_list[i] = element.to_alipay_dict()
            if hasattr(self.scene_tag_list, 'to_alipay_dict'):
                params['scene_tag_list'] = self.scene_tag_list.to_alipay_dict()
            else:
                params['scene_tag_list'] = self.scene_tag_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskRuleConfig()
        if 'good_list' in d:
            o.good_list = d['good_list']
        if 'scene_tag_list' in d:
            o.scene_tag_list = d['scene_tag_list']
        return o



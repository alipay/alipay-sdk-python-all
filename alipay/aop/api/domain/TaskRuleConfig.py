#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskRuleConfig(object):

    def __init__(self):
        self._scene_tag_list = None

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
        if 'scene_tag_list' in d:
            o.scene_tag_list = d['scene_tag_list']
        return o



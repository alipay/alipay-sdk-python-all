#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecruitContentConfig import RecruitContentConfig


class RecruitContentMiniApp(object):

    def __init__(self):
        self._content_configs = None
        self._mini_app_id = None

    @property
    def content_configs(self):
        return self._content_configs

    @content_configs.setter
    def content_configs(self, value):
        if isinstance(value, list):
            self._content_configs = list()
            for i in value:
                if isinstance(i, RecruitContentConfig):
                    self._content_configs.append(i)
                else:
                    self._content_configs.append(RecruitContentConfig.from_alipay_dict(i))
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_configs:
            if isinstance(self.content_configs, list):
                for i in range(0, len(self.content_configs)):
                    element = self.content_configs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_configs[i] = element.to_alipay_dict()
            if hasattr(self.content_configs, 'to_alipay_dict'):
                params['content_configs'] = self.content_configs.to_alipay_dict()
            else:
                params['content_configs'] = self.content_configs
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitContentMiniApp()
        if 'content_configs' in d:
            o.content_configs = d['content_configs']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        return o



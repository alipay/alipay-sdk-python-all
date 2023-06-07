#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecruitContentConfig import RecruitContentConfig


class RecruitContentVoucherActivity(object):

    def __init__(self):
        self._activity_id = None
        self._content_configs = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitContentVoucherActivity()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'content_configs' in d:
            o.content_configs = d['content_configs']
        return o



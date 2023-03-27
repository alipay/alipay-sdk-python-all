#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecruitContentConfig import RecruitContentConfig


class RecruitContentAppItem(object):

    def __init__(self):
        self._content_configs = None
        self._item_id = None
        self._out_item_id = None
        self._related_app_id = None

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
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def related_app_id(self):
        return self._related_app_id

    @related_app_id.setter
    def related_app_id(self, value):
        self._related_app_id = value


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
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.related_app_id:
            if hasattr(self.related_app_id, 'to_alipay_dict'):
                params['related_app_id'] = self.related_app_id.to_alipay_dict()
            else:
                params['related_app_id'] = self.related_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitContentAppItem()
        if 'content_configs' in d:
            o.content_configs = d['content_configs']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'related_app_id' in d:
            o.related_app_id = d['related_app_id']
        return o



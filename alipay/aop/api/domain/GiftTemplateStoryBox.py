#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GiftTemplateMetaInfo import GiftTemplateMetaInfo


class GiftTemplateStoryBox(object):

    def __init__(self):
        self._link_show_memo = None
        self._link_to_merchant = None
        self._memo = None
        self._resources = None

    @property
    def link_show_memo(self):
        return self._link_show_memo

    @link_show_memo.setter
    def link_show_memo(self, value):
        self._link_show_memo = value
    @property
    def link_to_merchant(self):
        return self._link_to_merchant

    @link_to_merchant.setter
    def link_to_merchant(self, value):
        self._link_to_merchant = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, value):
        if isinstance(value, list):
            self._resources = list()
            for i in value:
                if isinstance(i, GiftTemplateMetaInfo):
                    self._resources.append(i)
                else:
                    self._resources.append(GiftTemplateMetaInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.link_show_memo:
            if hasattr(self.link_show_memo, 'to_alipay_dict'):
                params['link_show_memo'] = self.link_show_memo.to_alipay_dict()
            else:
                params['link_show_memo'] = self.link_show_memo
        if self.link_to_merchant:
            if hasattr(self.link_to_merchant, 'to_alipay_dict'):
                params['link_to_merchant'] = self.link_to_merchant.to_alipay_dict()
            else:
                params['link_to_merchant'] = self.link_to_merchant
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.resources:
            if isinstance(self.resources, list):
                for i in range(0, len(self.resources)):
                    element = self.resources[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.resources[i] = element.to_alipay_dict()
            if hasattr(self.resources, 'to_alipay_dict'):
                params['resources'] = self.resources.to_alipay_dict()
            else:
                params['resources'] = self.resources
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GiftTemplateStoryBox()
        if 'link_show_memo' in d:
            o.link_show_memo = d['link_show_memo']
        if 'link_to_merchant' in d:
            o.link_to_merchant = d['link_to_merchant']
        if 'memo' in d:
            o.memo = d['memo']
        if 'resources' in d:
            o.resources = d['resources']
        return o



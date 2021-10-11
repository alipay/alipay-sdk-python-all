#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberCardPayEffectiveItemRule(object):

    def __init__(self):
        self._exclude_item_ids = None
        self._item_ids = None

    @property
    def exclude_item_ids(self):
        return self._exclude_item_ids

    @exclude_item_ids.setter
    def exclude_item_ids(self, value):
        if isinstance(value, list):
            self._exclude_item_ids = list()
            for i in value:
                self._exclude_item_ids.append(i)
    @property
    def item_ids(self):
        return self._item_ids

    @item_ids.setter
    def item_ids(self, value):
        if isinstance(value, list):
            self._item_ids = list()
            for i in value:
                self._item_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.exclude_item_ids:
            if isinstance(self.exclude_item_ids, list):
                for i in range(0, len(self.exclude_item_ids)):
                    element = self.exclude_item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exclude_item_ids[i] = element.to_alipay_dict()
            if hasattr(self.exclude_item_ids, 'to_alipay_dict'):
                params['exclude_item_ids'] = self.exclude_item_ids.to_alipay_dict()
            else:
                params['exclude_item_ids'] = self.exclude_item_ids
        if self.item_ids:
            if isinstance(self.item_ids, list):
                for i in range(0, len(self.item_ids)):
                    element = self.item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_ids[i] = element.to_alipay_dict()
            if hasattr(self.item_ids, 'to_alipay_dict'):
                params['item_ids'] = self.item_ids.to_alipay_dict()
            else:
                params['item_ids'] = self.item_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberCardPayEffectiveItemRule()
        if 'exclude_item_ids' in d:
            o.exclude_item_ids = d['exclude_item_ids']
        if 'item_ids' in d:
            o.item_ids = d['item_ids']
        return o



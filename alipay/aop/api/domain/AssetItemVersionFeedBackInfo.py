#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetItemVersionFeedBackInfo(object):

    def __init__(self):
        self._item_id = None
        self._item_version = None
        self._memo = None
        self._suppliable = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_version(self):
        return self._item_version

    @item_version.setter
    def item_version(self, value):
        self._item_version = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def suppliable(self):
        return self._suppliable

    @suppliable.setter
    def suppliable(self, value):
        self._suppliable = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_version:
            if hasattr(self.item_version, 'to_alipay_dict'):
                params['item_version'] = self.item_version.to_alipay_dict()
            else:
                params['item_version'] = self.item_version
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.suppliable:
            if hasattr(self.suppliable, 'to_alipay_dict'):
                params['suppliable'] = self.suppliable.to_alipay_dict()
            else:
                params['suppliable'] = self.suppliable
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetItemVersionFeedBackInfo()
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_version' in d:
            o.item_version = d['item_version']
        if 'memo' in d:
            o.memo = d['memo']
        if 'suppliable' in d:
            o.suppliable = d['suppliable']
        return o



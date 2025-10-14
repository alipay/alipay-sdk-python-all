#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetApplyOrderCancelInfo(object):

    def __init__(self):
        self._apply_order_id = None
        self._assign_item_ids = None

    @property
    def apply_order_id(self):
        return self._apply_order_id

    @apply_order_id.setter
    def apply_order_id(self, value):
        self._apply_order_id = value
    @property
    def assign_item_ids(self):
        return self._assign_item_ids

    @assign_item_ids.setter
    def assign_item_ids(self, value):
        if isinstance(value, list):
            self._assign_item_ids = list()
            for i in value:
                self._assign_item_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_order_id:
            if hasattr(self.apply_order_id, 'to_alipay_dict'):
                params['apply_order_id'] = self.apply_order_id.to_alipay_dict()
            else:
                params['apply_order_id'] = self.apply_order_id
        if self.assign_item_ids:
            if isinstance(self.assign_item_ids, list):
                for i in range(0, len(self.assign_item_ids)):
                    element = self.assign_item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.assign_item_ids[i] = element.to_alipay_dict()
            if hasattr(self.assign_item_ids, 'to_alipay_dict'):
                params['assign_item_ids'] = self.assign_item_ids.to_alipay_dict()
            else:
                params['assign_item_ids'] = self.assign_item_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetApplyOrderCancelInfo()
        if 'apply_order_id' in d:
            o.apply_order_id = d['apply_order_id']
        if 'assign_item_ids' in d:
            o.assign_item_ids = d['assign_item_ids']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApplyReverseOrderCancelInfo(object):

    def __init__(self):
        self._assign_item_id = None
        self._assign_item_ids = None
        self._reverse_apply_order_id = None

    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        if isinstance(value, list):
            self._assign_item_id = list()
            for i in value:
                self._assign_item_id.append(i)
    @property
    def assign_item_ids(self):
        return self._assign_item_ids

    @assign_item_ids.setter
    def assign_item_ids(self, value):
        if isinstance(value, list):
            self._assign_item_ids = list()
            for i in value:
                self._assign_item_ids.append(i)
    @property
    def reverse_apply_order_id(self):
        return self._reverse_apply_order_id

    @reverse_apply_order_id.setter
    def reverse_apply_order_id(self, value):
        self._reverse_apply_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.assign_item_id:
            if isinstance(self.assign_item_id, list):
                for i in range(0, len(self.assign_item_id)):
                    element = self.assign_item_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.assign_item_id[i] = element.to_alipay_dict()
            if hasattr(self.assign_item_id, 'to_alipay_dict'):
                params['assign_item_id'] = self.assign_item_id.to_alipay_dict()
            else:
                params['assign_item_id'] = self.assign_item_id
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
        if self.reverse_apply_order_id:
            if hasattr(self.reverse_apply_order_id, 'to_alipay_dict'):
                params['reverse_apply_order_id'] = self.reverse_apply_order_id.to_alipay_dict()
            else:
                params['reverse_apply_order_id'] = self.reverse_apply_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApplyReverseOrderCancelInfo()
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'assign_item_ids' in d:
            o.assign_item_ids = d['assign_item_ids']
        if 'reverse_apply_order_id' in d:
            o.reverse_apply_order_id = d['reverse_apply_order_id']
        return o



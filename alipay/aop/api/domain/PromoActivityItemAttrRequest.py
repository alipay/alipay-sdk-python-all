#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoActivityAttrRequest import PromoActivityAttrRequest


class PromoActivityItemAttrRequest(object):

    def __init__(self):
        self._activity_attr_list = None
        self._item_id = None
        self._out_item_id = None

    @property
    def activity_attr_list(self):
        return self._activity_attr_list

    @activity_attr_list.setter
    def activity_attr_list(self, value):
        if isinstance(value, list):
            self._activity_attr_list = list()
            for i in value:
                if isinstance(i, PromoActivityAttrRequest):
                    self._activity_attr_list.append(i)
                else:
                    self._activity_attr_list.append(PromoActivityAttrRequest.from_alipay_dict(i))
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


    def to_alipay_dict(self):
        params = dict()
        if self.activity_attr_list:
            if isinstance(self.activity_attr_list, list):
                for i in range(0, len(self.activity_attr_list)):
                    element = self.activity_attr_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_attr_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_attr_list, 'to_alipay_dict'):
                params['activity_attr_list'] = self.activity_attr_list.to_alipay_dict()
            else:
                params['activity_attr_list'] = self.activity_attr_list
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoActivityItemAttrRequest()
        if 'activity_attr_list' in d:
            o.activity_attr_list = d['activity_attr_list']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        return o



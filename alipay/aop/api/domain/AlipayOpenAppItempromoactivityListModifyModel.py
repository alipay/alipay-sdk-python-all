#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoActivityItemAttrRequest import PromoActivityItemAttrRequest


class AlipayOpenAppItempromoactivityListModifyModel(object):

    def __init__(self):
        self._item_attr_list = None
        self._promotion_type = None

    @property
    def item_attr_list(self):
        return self._item_attr_list

    @item_attr_list.setter
    def item_attr_list(self, value):
        if isinstance(value, list):
            self._item_attr_list = list()
            for i in value:
                if isinstance(i, PromoActivityItemAttrRequest):
                    self._item_attr_list.append(i)
                else:
                    self._item_attr_list.append(PromoActivityItemAttrRequest.from_alipay_dict(i))
    @property
    def promotion_type(self):
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, value):
        self._promotion_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_attr_list:
            if isinstance(self.item_attr_list, list):
                for i in range(0, len(self.item_attr_list)):
                    element = self.item_attr_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_attr_list[i] = element.to_alipay_dict()
            if hasattr(self.item_attr_list, 'to_alipay_dict'):
                params['item_attr_list'] = self.item_attr_list.to_alipay_dict()
            else:
                params['item_attr_list'] = self.item_attr_list
        if self.promotion_type:
            if hasattr(self.promotion_type, 'to_alipay_dict'):
                params['promotion_type'] = self.promotion_type.to_alipay_dict()
            else:
                params['promotion_type'] = self.promotion_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppItempromoactivityListModifyModel()
        if 'item_attr_list' in d:
            o.item_attr_list = d['item_attr_list']
        if 'promotion_type' in d:
            o.promotion_type = d['promotion_type']
        return o



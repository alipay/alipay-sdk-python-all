#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GoodsComponent import GoodsComponent


class ExtitemDetailInfo(object):

    def __init__(self):
        self._extitem_id = None
        self._extitem_name = None
        self._goods_component_list = None

    @property
    def extitem_id(self):
        return self._extitem_id

    @extitem_id.setter
    def extitem_id(self, value):
        self._extitem_id = value
    @property
    def extitem_name(self):
        return self._extitem_name

    @extitem_name.setter
    def extitem_name(self, value):
        self._extitem_name = value
    @property
    def goods_component_list(self):
        return self._goods_component_list

    @goods_component_list.setter
    def goods_component_list(self, value):
        if isinstance(value, list):
            self._goods_component_list = list()
            for i in value:
                if isinstance(i, GoodsComponent):
                    self._goods_component_list.append(i)
                else:
                    self._goods_component_list.append(GoodsComponent.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.extitem_id:
            if hasattr(self.extitem_id, 'to_alipay_dict'):
                params['extitem_id'] = self.extitem_id.to_alipay_dict()
            else:
                params['extitem_id'] = self.extitem_id
        if self.extitem_name:
            if hasattr(self.extitem_name, 'to_alipay_dict'):
                params['extitem_name'] = self.extitem_name.to_alipay_dict()
            else:
                params['extitem_name'] = self.extitem_name
        if self.goods_component_list:
            if isinstance(self.goods_component_list, list):
                for i in range(0, len(self.goods_component_list)):
                    element = self.goods_component_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_component_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_component_list, 'to_alipay_dict'):
                params['goods_component_list'] = self.goods_component_list.to_alipay_dict()
            else:
                params['goods_component_list'] = self.goods_component_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtitemDetailInfo()
        if 'extitem_id' in d:
            o.extitem_id = d['extitem_id']
        if 'extitem_name' in d:
            o.extitem_name = d['extitem_name']
        if 'goods_component_list' in d:
            o.goods_component_list = d['goods_component_list']
        return o



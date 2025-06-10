#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CustomGoodsVO import CustomGoodsVO


class GoodsMsgVO(object):

    def __init__(self):
        self._activity_id = None
        self._custom_goods_list = None
        self._desc = None
        self._goods_item_id = None
        self._goods_item_id_list = None
        self._goods_source = None
        self._multi_goods = None
        self._related_app_id = None
        self._title = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def custom_goods_list(self):
        return self._custom_goods_list

    @custom_goods_list.setter
    def custom_goods_list(self, value):
        if isinstance(value, list):
            self._custom_goods_list = list()
            for i in value:
                if isinstance(i, CustomGoodsVO):
                    self._custom_goods_list.append(i)
                else:
                    self._custom_goods_list.append(CustomGoodsVO.from_alipay_dict(i))
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def goods_item_id(self):
        return self._goods_item_id

    @goods_item_id.setter
    def goods_item_id(self, value):
        self._goods_item_id = value
    @property
    def goods_item_id_list(self):
        return self._goods_item_id_list

    @goods_item_id_list.setter
    def goods_item_id_list(self, value):
        if isinstance(value, list):
            self._goods_item_id_list = list()
            for i in value:
                self._goods_item_id_list.append(i)
    @property
    def goods_source(self):
        return self._goods_source

    @goods_source.setter
    def goods_source(self, value):
        self._goods_source = value
    @property
    def multi_goods(self):
        return self._multi_goods

    @multi_goods.setter
    def multi_goods(self, value):
        self._multi_goods = value
    @property
    def related_app_id(self):
        return self._related_app_id

    @related_app_id.setter
    def related_app_id(self, value):
        self._related_app_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.custom_goods_list:
            if isinstance(self.custom_goods_list, list):
                for i in range(0, len(self.custom_goods_list)):
                    element = self.custom_goods_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.custom_goods_list[i] = element.to_alipay_dict()
            if hasattr(self.custom_goods_list, 'to_alipay_dict'):
                params['custom_goods_list'] = self.custom_goods_list.to_alipay_dict()
            else:
                params['custom_goods_list'] = self.custom_goods_list
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.goods_item_id:
            if hasattr(self.goods_item_id, 'to_alipay_dict'):
                params['goods_item_id'] = self.goods_item_id.to_alipay_dict()
            else:
                params['goods_item_id'] = self.goods_item_id
        if self.goods_item_id_list:
            if isinstance(self.goods_item_id_list, list):
                for i in range(0, len(self.goods_item_id_list)):
                    element = self.goods_item_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_item_id_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_item_id_list, 'to_alipay_dict'):
                params['goods_item_id_list'] = self.goods_item_id_list.to_alipay_dict()
            else:
                params['goods_item_id_list'] = self.goods_item_id_list
        if self.goods_source:
            if hasattr(self.goods_source, 'to_alipay_dict'):
                params['goods_source'] = self.goods_source.to_alipay_dict()
            else:
                params['goods_source'] = self.goods_source
        if self.multi_goods:
            if hasattr(self.multi_goods, 'to_alipay_dict'):
                params['multi_goods'] = self.multi_goods.to_alipay_dict()
            else:
                params['multi_goods'] = self.multi_goods
        if self.related_app_id:
            if hasattr(self.related_app_id, 'to_alipay_dict'):
                params['related_app_id'] = self.related_app_id.to_alipay_dict()
            else:
                params['related_app_id'] = self.related_app_id
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsMsgVO()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'custom_goods_list' in d:
            o.custom_goods_list = d['custom_goods_list']
        if 'desc' in d:
            o.desc = d['desc']
        if 'goods_item_id' in d:
            o.goods_item_id = d['goods_item_id']
        if 'goods_item_id_list' in d:
            o.goods_item_id_list = d['goods_item_id_list']
        if 'goods_source' in d:
            o.goods_source = d['goods_source']
        if 'multi_goods' in d:
            o.multi_goods = d['multi_goods']
        if 'related_app_id' in d:
            o.related_app_id = d['related_app_id']
        if 'title' in d:
            o.title = d['title']
        return o



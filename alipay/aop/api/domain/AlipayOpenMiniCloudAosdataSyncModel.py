#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContentItem import ContentItem
from alipay.aop.api.domain.GenericItem import GenericItem
from alipay.aop.api.domain.GoodItem import GoodItem
from alipay.aop.api.domain.RetailItem import RetailItem
from alipay.aop.api.domain.ShopItemInfo import ShopItemInfo


class AlipayOpenMiniCloudAosdataSyncModel(object):

    def __init__(self):
        self._content_list = None
        self._data_type = None
        self._generic_item_list = None
        self._goods_list = None
        self._project_id = None
        self._retail_item_list = None
        self._shop_list = None

    @property
    def content_list(self):
        return self._content_list

    @content_list.setter
    def content_list(self, value):
        if isinstance(value, list):
            self._content_list = list()
            for i in value:
                if isinstance(i, ContentItem):
                    self._content_list.append(i)
                else:
                    self._content_list.append(ContentItem.from_alipay_dict(i))
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def generic_item_list(self):
        return self._generic_item_list

    @generic_item_list.setter
    def generic_item_list(self, value):
        if isinstance(value, list):
            self._generic_item_list = list()
            for i in value:
                if isinstance(i, GenericItem):
                    self._generic_item_list.append(i)
                else:
                    self._generic_item_list.append(GenericItem.from_alipay_dict(i))
    @property
    def goods_list(self):
        return self._goods_list

    @goods_list.setter
    def goods_list(self, value):
        if isinstance(value, list):
            self._goods_list = list()
            for i in value:
                if isinstance(i, GoodItem):
                    self._goods_list.append(i)
                else:
                    self._goods_list.append(GoodItem.from_alipay_dict(i))
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def retail_item_list(self):
        return self._retail_item_list

    @retail_item_list.setter
    def retail_item_list(self, value):
        if isinstance(value, list):
            self._retail_item_list = list()
            for i in value:
                if isinstance(i, RetailItem):
                    self._retail_item_list.append(i)
                else:
                    self._retail_item_list.append(RetailItem.from_alipay_dict(i))
    @property
    def shop_list(self):
        return self._shop_list

    @shop_list.setter
    def shop_list(self, value):
        if isinstance(value, list):
            self._shop_list = list()
            for i in value:
                if isinstance(i, ShopItemInfo):
                    self._shop_list.append(i)
                else:
                    self._shop_list.append(ShopItemInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.content_list:
            if isinstance(self.content_list, list):
                for i in range(0, len(self.content_list)):
                    element = self.content_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_list[i] = element.to_alipay_dict()
            if hasattr(self.content_list, 'to_alipay_dict'):
                params['content_list'] = self.content_list.to_alipay_dict()
            else:
                params['content_list'] = self.content_list
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.generic_item_list:
            if isinstance(self.generic_item_list, list):
                for i in range(0, len(self.generic_item_list)):
                    element = self.generic_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.generic_item_list[i] = element.to_alipay_dict()
            if hasattr(self.generic_item_list, 'to_alipay_dict'):
                params['generic_item_list'] = self.generic_item_list.to_alipay_dict()
            else:
                params['generic_item_list'] = self.generic_item_list
        if self.goods_list:
            if isinstance(self.goods_list, list):
                for i in range(0, len(self.goods_list)):
                    element = self.goods_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_list, 'to_alipay_dict'):
                params['goods_list'] = self.goods_list.to_alipay_dict()
            else:
                params['goods_list'] = self.goods_list
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.retail_item_list:
            if isinstance(self.retail_item_list, list):
                for i in range(0, len(self.retail_item_list)):
                    element = self.retail_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.retail_item_list[i] = element.to_alipay_dict()
            if hasattr(self.retail_item_list, 'to_alipay_dict'):
                params['retail_item_list'] = self.retail_item_list.to_alipay_dict()
            else:
                params['retail_item_list'] = self.retail_item_list
        if self.shop_list:
            if isinstance(self.shop_list, list):
                for i in range(0, len(self.shop_list)):
                    element = self.shop_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_list, 'to_alipay_dict'):
                params['shop_list'] = self.shop_list.to_alipay_dict()
            else:
                params['shop_list'] = self.shop_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniCloudAosdataSyncModel()
        if 'content_list' in d:
            o.content_list = d['content_list']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'generic_item_list' in d:
            o.generic_item_list = d['generic_item_list']
        if 'goods_list' in d:
            o.goods_list = d['goods_list']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'retail_item_list' in d:
            o.retail_item_list = d['retail_item_list']
        if 'shop_list' in d:
            o.shop_list = d['shop_list']
        return o



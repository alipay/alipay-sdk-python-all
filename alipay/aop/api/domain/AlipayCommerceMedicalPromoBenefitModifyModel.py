#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LinkedMallItemBaseSku import LinkedMallItemBaseSku


class AlipayCommerceMedicalPromoBenefitModifyModel(object):

    def __init__(self):
        self._category_id = None
        self._category_name = None
        self._item_action = None
        self._item_id = None
        self._item_title = None
        self._main_pic_url = None
        self._open_id = None
        self._sku_list = None
        self._user_id = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def item_action(self):
        return self._item_action

    @item_action.setter
    def item_action(self, value):
        self._item_action = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_title(self):
        return self._item_title

    @item_title.setter
    def item_title(self, value):
        self._item_title = value
    @property
    def main_pic_url(self):
        return self._main_pic_url

    @main_pic_url.setter
    def main_pic_url(self, value):
        self._main_pic_url = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, list):
            self._sku_list = list()
            for i in value:
                if isinstance(i, LinkedMallItemBaseSku):
                    self._sku_list.append(i)
                else:
                    self._sku_list.append(LinkedMallItemBaseSku.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.item_action:
            if hasattr(self.item_action, 'to_alipay_dict'):
                params['item_action'] = self.item_action.to_alipay_dict()
            else:
                params['item_action'] = self.item_action
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_title:
            if hasattr(self.item_title, 'to_alipay_dict'):
                params['item_title'] = self.item_title.to_alipay_dict()
            else:
                params['item_title'] = self.item_title
        if self.main_pic_url:
            if hasattr(self.main_pic_url, 'to_alipay_dict'):
                params['main_pic_url'] = self.main_pic_url.to_alipay_dict()
            else:
                params['main_pic_url'] = self.main_pic_url
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.sku_list:
            if isinstance(self.sku_list, list):
                for i in range(0, len(self.sku_list)):
                    element = self.sku_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_list, 'to_alipay_dict'):
                params['sku_list'] = self.sku_list.to_alipay_dict()
            else:
                params['sku_list'] = self.sku_list
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalPromoBenefitModifyModel()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'item_action' in d:
            o.item_action = d['item_action']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_title' in d:
            o.item_title = d['item_title']
        if 'main_pic_url' in d:
            o.main_pic_url = d['main_pic_url']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'sku_list' in d:
            o.sku_list = d['sku_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



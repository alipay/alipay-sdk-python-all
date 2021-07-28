#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemConsultInfo import ItemConsultInfo


class ItemPromoInfo(object):

    def __init__(self):
        self._item_consult_list = None
        self._item_cover_pic = None
        self._item_desc = None
        self._item_detail_pic_list = None
        self._item_name = None

    @property
    def item_consult_list(self):
        return self._item_consult_list

    @item_consult_list.setter
    def item_consult_list(self, value):
        if isinstance(value, list):
            self._item_consult_list = list()
            for i in value:
                if isinstance(i, ItemConsultInfo):
                    self._item_consult_list.append(i)
                else:
                    self._item_consult_list.append(ItemConsultInfo.from_alipay_dict(i))
    @property
    def item_cover_pic(self):
        return self._item_cover_pic

    @item_cover_pic.setter
    def item_cover_pic(self, value):
        self._item_cover_pic = value
    @property
    def item_desc(self):
        return self._item_desc

    @item_desc.setter
    def item_desc(self, value):
        self._item_desc = value
    @property
    def item_detail_pic_list(self):
        return self._item_detail_pic_list

    @item_detail_pic_list.setter
    def item_detail_pic_list(self, value):
        if isinstance(value, list):
            self._item_detail_pic_list = list()
            for i in value:
                self._item_detail_pic_list.append(i)
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_consult_list:
            if isinstance(self.item_consult_list, list):
                for i in range(0, len(self.item_consult_list)):
                    element = self.item_consult_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_consult_list[i] = element.to_alipay_dict()
            if hasattr(self.item_consult_list, 'to_alipay_dict'):
                params['item_consult_list'] = self.item_consult_list.to_alipay_dict()
            else:
                params['item_consult_list'] = self.item_consult_list
        if self.item_cover_pic:
            if hasattr(self.item_cover_pic, 'to_alipay_dict'):
                params['item_cover_pic'] = self.item_cover_pic.to_alipay_dict()
            else:
                params['item_cover_pic'] = self.item_cover_pic
        if self.item_desc:
            if hasattr(self.item_desc, 'to_alipay_dict'):
                params['item_desc'] = self.item_desc.to_alipay_dict()
            else:
                params['item_desc'] = self.item_desc
        if self.item_detail_pic_list:
            if isinstance(self.item_detail_pic_list, list):
                for i in range(0, len(self.item_detail_pic_list)):
                    element = self.item_detail_pic_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_detail_pic_list[i] = element.to_alipay_dict()
            if hasattr(self.item_detail_pic_list, 'to_alipay_dict'):
                params['item_detail_pic_list'] = self.item_detail_pic_list.to_alipay_dict()
            else:
                params['item_detail_pic_list'] = self.item_detail_pic_list
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemPromoInfo()
        if 'item_consult_list' in d:
            o.item_consult_list = d['item_consult_list']
        if 'item_cover_pic' in d:
            o.item_cover_pic = d['item_cover_pic']
        if 'item_desc' in d:
            o.item_desc = d['item_desc']
        if 'item_detail_pic_list' in d:
            o.item_detail_pic_list = d['item_detail_pic_list']
        if 'item_name' in d:
            o.item_name = d['item_name']
        return o



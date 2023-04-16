#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BsSupplyItemInfo(object):

    def __init__(self):
        self._item_cover_pic = None
        self._item_description = None
        self._item_name = None

    @property
    def item_cover_pic(self):
        return self._item_cover_pic

    @item_cover_pic.setter
    def item_cover_pic(self, value):
        self._item_cover_pic = value
    @property
    def item_description(self):
        return self._item_description

    @item_description.setter
    def item_description(self, value):
        self._item_description = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_cover_pic:
            if hasattr(self.item_cover_pic, 'to_alipay_dict'):
                params['item_cover_pic'] = self.item_cover_pic.to_alipay_dict()
            else:
                params['item_cover_pic'] = self.item_cover_pic
        if self.item_description:
            if hasattr(self.item_description, 'to_alipay_dict'):
                params['item_description'] = self.item_description.to_alipay_dict()
            else:
                params['item_description'] = self.item_description
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
        o = BsSupplyItemInfo()
        if 'item_cover_pic' in d:
            o.item_cover_pic = d['item_cover_pic']
        if 'item_description' in d:
            o.item_description = d['item_description']
        if 'item_name' in d:
            o.item_name = d['item_name']
        return o



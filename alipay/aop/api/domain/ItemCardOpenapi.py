#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemCardOpenapi(object):

    def __init__(self):
        self._item_id = None
        self._item_image = None
        self._item_original_price = None
        self._item_safe_price = None
        self._item_tags = None
        self._item_title = None
        self._item_url = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_image(self):
        return self._item_image

    @item_image.setter
    def item_image(self, value):
        self._item_image = value
    @property
    def item_original_price(self):
        return self._item_original_price

    @item_original_price.setter
    def item_original_price(self, value):
        self._item_original_price = value
    @property
    def item_safe_price(self):
        return self._item_safe_price

    @item_safe_price.setter
    def item_safe_price(self, value):
        self._item_safe_price = value
    @property
    def item_tags(self):
        return self._item_tags

    @item_tags.setter
    def item_tags(self, value):
        if isinstance(value, list):
            self._item_tags = list()
            for i in value:
                self._item_tags.append(i)
    @property
    def item_title(self):
        return self._item_title

    @item_title.setter
    def item_title(self, value):
        self._item_title = value
    @property
    def item_url(self):
        return self._item_url

    @item_url.setter
    def item_url(self, value):
        self._item_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_image:
            if hasattr(self.item_image, 'to_alipay_dict'):
                params['item_image'] = self.item_image.to_alipay_dict()
            else:
                params['item_image'] = self.item_image
        if self.item_original_price:
            if hasattr(self.item_original_price, 'to_alipay_dict'):
                params['item_original_price'] = self.item_original_price.to_alipay_dict()
            else:
                params['item_original_price'] = self.item_original_price
        if self.item_safe_price:
            if hasattr(self.item_safe_price, 'to_alipay_dict'):
                params['item_safe_price'] = self.item_safe_price.to_alipay_dict()
            else:
                params['item_safe_price'] = self.item_safe_price
        if self.item_tags:
            if isinstance(self.item_tags, list):
                for i in range(0, len(self.item_tags)):
                    element = self.item_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_tags[i] = element.to_alipay_dict()
            if hasattr(self.item_tags, 'to_alipay_dict'):
                params['item_tags'] = self.item_tags.to_alipay_dict()
            else:
                params['item_tags'] = self.item_tags
        if self.item_title:
            if hasattr(self.item_title, 'to_alipay_dict'):
                params['item_title'] = self.item_title.to_alipay_dict()
            else:
                params['item_title'] = self.item_title
        if self.item_url:
            if hasattr(self.item_url, 'to_alipay_dict'):
                params['item_url'] = self.item_url.to_alipay_dict()
            else:
                params['item_url'] = self.item_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemCardOpenapi()
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_image' in d:
            o.item_image = d['item_image']
        if 'item_original_price' in d:
            o.item_original_price = d['item_original_price']
        if 'item_safe_price' in d:
            o.item_safe_price = d['item_safe_price']
        if 'item_tags' in d:
            o.item_tags = d['item_tags']
        if 'item_title' in d:
            o.item_title = d['item_title']
        if 'item_url' in d:
            o.item_url = d['item_url']
        return o



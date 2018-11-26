#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemResp(object):

    def __init__(self):
        self._category = None
        self._has_recive = None
        self._icon = None
        self._image = None
        self._item_id = None
        self._meaning = None
        self._org_price = None
        self._price = None
        self._shop_id = None
        self._summary = None
        self._tags = None
        self._tips = None
        self._title = None
        self._type = None
        self._url = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def has_recive(self):
        return self._has_recive

    @has_recive.setter
    def has_recive(self, value):
        self._has_recive = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def meaning(self):
        return self._meaning

    @meaning.setter
    def meaning(self, value):
        self._meaning = value
    @property
    def org_price(self):
        return self._org_price

    @org_price.setter
    def org_price(self, value):
        self._org_price = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value
    @property
    def tips(self):
        return self._tips

    @tips.setter
    def tips(self, value):
        self._tips = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.has_recive:
            if hasattr(self.has_recive, 'to_alipay_dict'):
                params['has_recive'] = self.has_recive.to_alipay_dict()
            else:
                params['has_recive'] = self.has_recive
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.meaning:
            if hasattr(self.meaning, 'to_alipay_dict'):
                params['meaning'] = self.meaning.to_alipay_dict()
            else:
                params['meaning'] = self.meaning
        if self.org_price:
            if hasattr(self.org_price, 'to_alipay_dict'):
                params['org_price'] = self.org_price.to_alipay_dict()
            else:
                params['org_price'] = self.org_price
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        if self.tags:
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.tips:
            if hasattr(self.tips, 'to_alipay_dict'):
                params['tips'] = self.tips.to_alipay_dict()
            else:
                params['tips'] = self.tips
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemResp()
        if 'category' in d:
            o.category = d['category']
        if 'has_recive' in d:
            o.has_recive = d['has_recive']
        if 'icon' in d:
            o.icon = d['icon']
        if 'image' in d:
            o.image = d['image']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'meaning' in d:
            o.meaning = d['meaning']
        if 'org_price' in d:
            o.org_price = d['org_price']
        if 'price' in d:
            o.price = d['price']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'summary' in d:
            o.summary = d['summary']
        if 'tags' in d:
            o.tags = d['tags']
        if 'tips' in d:
            o.tips = d['tips']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        if 'url' in d:
            o.url = d['url']
        return o



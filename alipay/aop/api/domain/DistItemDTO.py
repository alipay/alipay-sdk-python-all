#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DistItemDTO(object):

    def __init__(self):
        self._channel_item_id = None
        self._channel_item_pic_url = None
        self._channel_item_price = None
        self._channel_item_title = None
        self._item_cnt = None
        self._item_id = None
        self._out_item_id = None
        self._out_sku_id = None
        self._sku_id = None

    @property
    def channel_item_id(self):
        return self._channel_item_id

    @channel_item_id.setter
    def channel_item_id(self, value):
        self._channel_item_id = value
    @property
    def channel_item_pic_url(self):
        return self._channel_item_pic_url

    @channel_item_pic_url.setter
    def channel_item_pic_url(self, value):
        self._channel_item_pic_url = value
    @property
    def channel_item_price(self):
        return self._channel_item_price

    @channel_item_price.setter
    def channel_item_price(self, value):
        self._channel_item_price = value
    @property
    def channel_item_title(self):
        return self._channel_item_title

    @channel_item_title.setter
    def channel_item_title(self, value):
        self._channel_item_title = value
    @property
    def item_cnt(self):
        return self._item_cnt

    @item_cnt.setter
    def item_cnt(self, value):
        self._item_cnt = value
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
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_item_id:
            if hasattr(self.channel_item_id, 'to_alipay_dict'):
                params['channel_item_id'] = self.channel_item_id.to_alipay_dict()
            else:
                params['channel_item_id'] = self.channel_item_id
        if self.channel_item_pic_url:
            if hasattr(self.channel_item_pic_url, 'to_alipay_dict'):
                params['channel_item_pic_url'] = self.channel_item_pic_url.to_alipay_dict()
            else:
                params['channel_item_pic_url'] = self.channel_item_pic_url
        if self.channel_item_price:
            if hasattr(self.channel_item_price, 'to_alipay_dict'):
                params['channel_item_price'] = self.channel_item_price.to_alipay_dict()
            else:
                params['channel_item_price'] = self.channel_item_price
        if self.channel_item_title:
            if hasattr(self.channel_item_title, 'to_alipay_dict'):
                params['channel_item_title'] = self.channel_item_title.to_alipay_dict()
            else:
                params['channel_item_title'] = self.channel_item_title
        if self.item_cnt:
            if hasattr(self.item_cnt, 'to_alipay_dict'):
                params['item_cnt'] = self.item_cnt.to_alipay_dict()
            else:
                params['item_cnt'] = self.item_cnt
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
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DistItemDTO()
        if 'channel_item_id' in d:
            o.channel_item_id = d['channel_item_id']
        if 'channel_item_pic_url' in d:
            o.channel_item_pic_url = d['channel_item_pic_url']
        if 'channel_item_price' in d:
            o.channel_item_price = d['channel_item_price']
        if 'channel_item_title' in d:
            o.channel_item_title = d['channel_item_title']
        if 'item_cnt' in d:
            o.item_cnt = d['item_cnt']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o



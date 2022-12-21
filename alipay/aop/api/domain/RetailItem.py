#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RetailItem(object):

    def __init__(self):
        self._available_times = None
        self._brand = None
        self._buy_url = None
        self._cate = None
        self._cate_cnt = None
        self._content = None
        self._detail_url = None
        self._goods_id = None
        self._id = None
        self._ip_role_id = None
        self._mini_app_id = None
        self._pic_url_list = None
        self._promo_pic_url_list = None
        self._shop_id = None
        self._status = None
        self._tags = None
        self._title = None

    @property
    def available_times(self):
        return self._available_times

    @available_times.setter
    def available_times(self, value):
        if isinstance(value, list):
            self._available_times = list()
            for i in value:
                self._available_times.append(i)
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def buy_url(self):
        return self._buy_url

    @buy_url.setter
    def buy_url(self, value):
        self._buy_url = value
    @property
    def cate(self):
        return self._cate

    @cate.setter
    def cate(self, value):
        self._cate = value
    @property
    def cate_cnt(self):
        return self._cate_cnt

    @cate_cnt.setter
    def cate_cnt(self, value):
        self._cate_cnt = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def pic_url_list(self):
        return self._pic_url_list

    @pic_url_list.setter
    def pic_url_list(self, value):
        if isinstance(value, list):
            self._pic_url_list = list()
            for i in value:
                self._pic_url_list.append(i)
    @property
    def promo_pic_url_list(self):
        return self._promo_pic_url_list

    @promo_pic_url_list.setter
    def promo_pic_url_list(self, value):
        if isinstance(value, list):
            self._promo_pic_url_list = list()
            for i in value:
                self._promo_pic_url_list.append(i)
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_times:
            if isinstance(self.available_times, list):
                for i in range(0, len(self.available_times)):
                    element = self.available_times[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_times[i] = element.to_alipay_dict()
            if hasattr(self.available_times, 'to_alipay_dict'):
                params['available_times'] = self.available_times.to_alipay_dict()
            else:
                params['available_times'] = self.available_times
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
        if self.buy_url:
            if hasattr(self.buy_url, 'to_alipay_dict'):
                params['buy_url'] = self.buy_url.to_alipay_dict()
            else:
                params['buy_url'] = self.buy_url
        if self.cate:
            if hasattr(self.cate, 'to_alipay_dict'):
                params['cate'] = self.cate.to_alipay_dict()
            else:
                params['cate'] = self.cate
        if self.cate_cnt:
            if hasattr(self.cate_cnt, 'to_alipay_dict'):
                params['cate_cnt'] = self.cate_cnt.to_alipay_dict()
            else:
                params['cate_cnt'] = self.cate_cnt
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.pic_url_list:
            if isinstance(self.pic_url_list, list):
                for i in range(0, len(self.pic_url_list)):
                    element = self.pic_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pic_url_list[i] = element.to_alipay_dict()
            if hasattr(self.pic_url_list, 'to_alipay_dict'):
                params['pic_url_list'] = self.pic_url_list.to_alipay_dict()
            else:
                params['pic_url_list'] = self.pic_url_list
        if self.promo_pic_url_list:
            if isinstance(self.promo_pic_url_list, list):
                for i in range(0, len(self.promo_pic_url_list)):
                    element = self.promo_pic_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_pic_url_list[i] = element.to_alipay_dict()
            if hasattr(self.promo_pic_url_list, 'to_alipay_dict'):
                params['promo_pic_url_list'] = self.promo_pic_url_list.to_alipay_dict()
            else:
                params['promo_pic_url_list'] = self.promo_pic_url_list
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tags:
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
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
        o = RetailItem()
        if 'available_times' in d:
            o.available_times = d['available_times']
        if 'brand' in d:
            o.brand = d['brand']
        if 'buy_url' in d:
            o.buy_url = d['buy_url']
        if 'cate' in d:
            o.cate = d['cate']
        if 'cate_cnt' in d:
            o.cate_cnt = d['cate_cnt']
        if 'content' in d:
            o.content = d['content']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'id' in d:
            o.id = d['id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'pic_url_list' in d:
            o.pic_url_list = d['pic_url_list']
        if 'promo_pic_url_list' in d:
            o.promo_pic_url_list = d['promo_pic_url_list']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        if 'tags' in d:
            o.tags = d['tags']
        if 'title' in d:
            o.title = d['title']
        return o



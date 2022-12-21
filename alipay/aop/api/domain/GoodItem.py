#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodItem(object):

    def __init__(self):
        self._available_city_list = None
        self._brand = None
        self._cate = None
        self._cate_cnt = None
        self._comment_cnt = None
        self._content = None
        self._current_price = None
        self._detail_pic_num = None
        self._detail_url = None
        self._id = None
        self._mini_app_id = None
        self._origin_price = None
        self._pic_url_list = None
        self._promo_pic_url_list = None
        self._pub_time = None
        self._rating = None
        self._row_type = None
        self._shop_id = None
        self._spu_id = None
        self._status = None
        self._stock_num = None
        self._tags = None
        self._title = None

    @property
    def available_city_list(self):
        return self._available_city_list

    @available_city_list.setter
    def available_city_list(self, value):
        if isinstance(value, list):
            self._available_city_list = list()
            for i in value:
                self._available_city_list.append(i)
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
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
    def comment_cnt(self):
        return self._comment_cnt

    @comment_cnt.setter
    def comment_cnt(self, value):
        self._comment_cnt = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def current_price(self):
        return self._current_price

    @current_price.setter
    def current_price(self, value):
        self._current_price = value
    @property
    def detail_pic_num(self):
        return self._detail_pic_num

    @detail_pic_num.setter
    def detail_pic_num(self, value):
        self._detail_pic_num = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def origin_price(self):
        return self._origin_price

    @origin_price.setter
    def origin_price(self, value):
        self._origin_price = value
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
    def pub_time(self):
        return self._pub_time

    @pub_time.setter
    def pub_time(self, value):
        self._pub_time = value
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value
    @property
    def row_type(self):
        return self._row_type

    @row_type.setter
    def row_type(self, value):
        self._row_type = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value
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
        if self.available_city_list:
            if isinstance(self.available_city_list, list):
                for i in range(0, len(self.available_city_list)):
                    element = self.available_city_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_city_list[i] = element.to_alipay_dict()
            if hasattr(self.available_city_list, 'to_alipay_dict'):
                params['available_city_list'] = self.available_city_list.to_alipay_dict()
            else:
                params['available_city_list'] = self.available_city_list
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
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
        if self.comment_cnt:
            if hasattr(self.comment_cnt, 'to_alipay_dict'):
                params['comment_cnt'] = self.comment_cnt.to_alipay_dict()
            else:
                params['comment_cnt'] = self.comment_cnt
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.current_price:
            if hasattr(self.current_price, 'to_alipay_dict'):
                params['current_price'] = self.current_price.to_alipay_dict()
            else:
                params['current_price'] = self.current_price
        if self.detail_pic_num:
            if hasattr(self.detail_pic_num, 'to_alipay_dict'):
                params['detail_pic_num'] = self.detail_pic_num.to_alipay_dict()
            else:
                params['detail_pic_num'] = self.detail_pic_num
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.origin_price:
            if hasattr(self.origin_price, 'to_alipay_dict'):
                params['origin_price'] = self.origin_price.to_alipay_dict()
            else:
                params['origin_price'] = self.origin_price
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
        if self.pub_time:
            if hasattr(self.pub_time, 'to_alipay_dict'):
                params['pub_time'] = self.pub_time.to_alipay_dict()
            else:
                params['pub_time'] = self.pub_time
        if self.rating:
            if hasattr(self.rating, 'to_alipay_dict'):
                params['rating'] = self.rating.to_alipay_dict()
            else:
                params['rating'] = self.rating
        if self.row_type:
            if hasattr(self.row_type, 'to_alipay_dict'):
                params['row_type'] = self.row_type.to_alipay_dict()
            else:
                params['row_type'] = self.row_type
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
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
        o = GoodItem()
        if 'available_city_list' in d:
            o.available_city_list = d['available_city_list']
        if 'brand' in d:
            o.brand = d['brand']
        if 'cate' in d:
            o.cate = d['cate']
        if 'cate_cnt' in d:
            o.cate_cnt = d['cate_cnt']
        if 'comment_cnt' in d:
            o.comment_cnt = d['comment_cnt']
        if 'content' in d:
            o.content = d['content']
        if 'current_price' in d:
            o.current_price = d['current_price']
        if 'detail_pic_num' in d:
            o.detail_pic_num = d['detail_pic_num']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'id' in d:
            o.id = d['id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'origin_price' in d:
            o.origin_price = d['origin_price']
        if 'pic_url_list' in d:
            o.pic_url_list = d['pic_url_list']
        if 'promo_pic_url_list' in d:
            o.promo_pic_url_list = d['promo_pic_url_list']
        if 'pub_time' in d:
            o.pub_time = d['pub_time']
        if 'rating' in d:
            o.rating = d['rating']
        if 'row_type' in d:
            o.row_type = d['row_type']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        if 'status' in d:
            o.status = d['status']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        if 'tags' in d:
            o.tags = d['tags']
        if 'title' in d:
            o.title = d['title']
        return o



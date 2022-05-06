#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApeDataItem(object):

    def __init__(self):
        self._brand = None
        self._cate = None
        self._cate_cnt = None
        self._comment_cnt = None
        self._current_price = None
        self._detail_pic_num = None
        self._free_shipping = None
        self._id = None
        self._origin_price = None
        self._pic_url_list = None
        self._praise_cnt = None
        self._pub_time = None
        self._rating = None
        self._sale_number = None
        self._share_cnt = None
        self._shipping_money = None
        self._shop_id = None
        self._source_id = None
        self._spu_id = None
        self._status = None
        self._tags = None
        self._title = None

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
    def free_shipping(self):
        return self._free_shipping

    @free_shipping.setter
    def free_shipping(self, value):
        self._free_shipping = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
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
    def praise_cnt(self):
        return self._praise_cnt

    @praise_cnt.setter
    def praise_cnt(self, value):
        self._praise_cnt = value
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
    def sale_number(self):
        return self._sale_number

    @sale_number.setter
    def sale_number(self, value):
        self._sale_number = value
    @property
    def share_cnt(self):
        return self._share_cnt

    @share_cnt.setter
    def share_cnt(self, value):
        self._share_cnt = value
    @property
    def shipping_money(self):
        return self._shipping_money

    @shipping_money.setter
    def shipping_money(self, value):
        self._shipping_money = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
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
        if self.free_shipping:
            if hasattr(self.free_shipping, 'to_alipay_dict'):
                params['free_shipping'] = self.free_shipping.to_alipay_dict()
            else:
                params['free_shipping'] = self.free_shipping
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
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
        if self.praise_cnt:
            if hasattr(self.praise_cnt, 'to_alipay_dict'):
                params['praise_cnt'] = self.praise_cnt.to_alipay_dict()
            else:
                params['praise_cnt'] = self.praise_cnt
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
        if self.sale_number:
            if hasattr(self.sale_number, 'to_alipay_dict'):
                params['sale_number'] = self.sale_number.to_alipay_dict()
            else:
                params['sale_number'] = self.sale_number
        if self.share_cnt:
            if hasattr(self.share_cnt, 'to_alipay_dict'):
                params['share_cnt'] = self.share_cnt.to_alipay_dict()
            else:
                params['share_cnt'] = self.share_cnt
        if self.shipping_money:
            if hasattr(self.shipping_money, 'to_alipay_dict'):
                params['shipping_money'] = self.shipping_money.to_alipay_dict()
            else:
                params['shipping_money'] = self.shipping_money
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
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
        o = ApeDataItem()
        if 'brand' in d:
            o.brand = d['brand']
        if 'cate' in d:
            o.cate = d['cate']
        if 'cate_cnt' in d:
            o.cate_cnt = d['cate_cnt']
        if 'comment_cnt' in d:
            o.comment_cnt = d['comment_cnt']
        if 'current_price' in d:
            o.current_price = d['current_price']
        if 'detail_pic_num' in d:
            o.detail_pic_num = d['detail_pic_num']
        if 'free_shipping' in d:
            o.free_shipping = d['free_shipping']
        if 'id' in d:
            o.id = d['id']
        if 'origin_price' in d:
            o.origin_price = d['origin_price']
        if 'pic_url_list' in d:
            o.pic_url_list = d['pic_url_list']
        if 'praise_cnt' in d:
            o.praise_cnt = d['praise_cnt']
        if 'pub_time' in d:
            o.pub_time = d['pub_time']
        if 'rating' in d:
            o.rating = d['rating']
        if 'sale_number' in d:
            o.sale_number = d['sale_number']
        if 'share_cnt' in d:
            o.share_cnt = d['share_cnt']
        if 'shipping_money' in d:
            o.shipping_money = d['shipping_money']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        if 'status' in d:
            o.status = d['status']
        if 'tags' in d:
            o.tags = d['tags']
        if 'title' in d:
            o.title = d['title']
        return o



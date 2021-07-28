#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduTradeExtInfo(object):

    def __init__(self):
        self._course_desc = None
        self._course_img_url = None
        self._course_name = None
        self._course_tag = None
        self._origin_price = None
        self._out_course_id = None
        self._out_shop_id = None
        self._price = None
        self._shop_img_url = None
        self._shop_name = None
        self._shop_url = None

    @property
    def course_desc(self):
        return self._course_desc

    @course_desc.setter
    def course_desc(self, value):
        self._course_desc = value
    @property
    def course_img_url(self):
        return self._course_img_url

    @course_img_url.setter
    def course_img_url(self, value):
        self._course_img_url = value
    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        self._course_name = value
    @property
    def course_tag(self):
        return self._course_tag

    @course_tag.setter
    def course_tag(self, value):
        self._course_tag = value
    @property
    def origin_price(self):
        return self._origin_price

    @origin_price.setter
    def origin_price(self, value):
        self._origin_price = value
    @property
    def out_course_id(self):
        return self._out_course_id

    @out_course_id.setter
    def out_course_id(self, value):
        self._out_course_id = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def shop_img_url(self):
        return self._shop_img_url

    @shop_img_url.setter
    def shop_img_url(self, value):
        self._shop_img_url = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_url(self):
        return self._shop_url

    @shop_url.setter
    def shop_url(self, value):
        self._shop_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.course_desc:
            if hasattr(self.course_desc, 'to_alipay_dict'):
                params['course_desc'] = self.course_desc.to_alipay_dict()
            else:
                params['course_desc'] = self.course_desc
        if self.course_img_url:
            if hasattr(self.course_img_url, 'to_alipay_dict'):
                params['course_img_url'] = self.course_img_url.to_alipay_dict()
            else:
                params['course_img_url'] = self.course_img_url
        if self.course_name:
            if hasattr(self.course_name, 'to_alipay_dict'):
                params['course_name'] = self.course_name.to_alipay_dict()
            else:
                params['course_name'] = self.course_name
        if self.course_tag:
            if hasattr(self.course_tag, 'to_alipay_dict'):
                params['course_tag'] = self.course_tag.to_alipay_dict()
            else:
                params['course_tag'] = self.course_tag
        if self.origin_price:
            if hasattr(self.origin_price, 'to_alipay_dict'):
                params['origin_price'] = self.origin_price.to_alipay_dict()
            else:
                params['origin_price'] = self.origin_price
        if self.out_course_id:
            if hasattr(self.out_course_id, 'to_alipay_dict'):
                params['out_course_id'] = self.out_course_id.to_alipay_dict()
            else:
                params['out_course_id'] = self.out_course_id
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.shop_img_url:
            if hasattr(self.shop_img_url, 'to_alipay_dict'):
                params['shop_img_url'] = self.shop_img_url.to_alipay_dict()
            else:
                params['shop_img_url'] = self.shop_img_url
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_url:
            if hasattr(self.shop_url, 'to_alipay_dict'):
                params['shop_url'] = self.shop_url.to_alipay_dict()
            else:
                params['shop_url'] = self.shop_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduTradeExtInfo()
        if 'course_desc' in d:
            o.course_desc = d['course_desc']
        if 'course_img_url' in d:
            o.course_img_url = d['course_img_url']
        if 'course_name' in d:
            o.course_name = d['course_name']
        if 'course_tag' in d:
            o.course_tag = d['course_tag']
        if 'origin_price' in d:
            o.origin_price = d['origin_price']
        if 'out_course_id' in d:
            o.out_course_id = d['out_course_id']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'price' in d:
            o.price = d['price']
        if 'shop_img_url' in d:
            o.shop_img_url = d['shop_img_url']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_url' in d:
            o.shop_url = d['shop_url']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandShopReviewCreateModel(object):

    def __init__(self):
        self._content_id = None
        self._digital_poi_id = None
        self._open_id = None
        self._pay_time = None
        self._review_create_time = None
        self._review_images = None
        self._review_modify_time = None
        self._review_text = None
        self._review_videos = None
        self._shop_id = None
        self._star_level = None
        self._star_level_total = None
        self._trade_no = None
        self._user_id = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def digital_poi_id(self):
        return self._digital_poi_id

    @digital_poi_id.setter
    def digital_poi_id(self, value):
        self._digital_poi_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def review_create_time(self):
        return self._review_create_time

    @review_create_time.setter
    def review_create_time(self, value):
        self._review_create_time = value
    @property
    def review_images(self):
        return self._review_images

    @review_images.setter
    def review_images(self, value):
        self._review_images = value
    @property
    def review_modify_time(self):
        return self._review_modify_time

    @review_modify_time.setter
    def review_modify_time(self, value):
        self._review_modify_time = value
    @property
    def review_text(self):
        return self._review_text

    @review_text.setter
    def review_text(self, value):
        self._review_text = value
    @property
    def review_videos(self):
        return self._review_videos

    @review_videos.setter
    def review_videos(self, value):
        self._review_videos = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def star_level(self):
        return self._star_level

    @star_level.setter
    def star_level(self, value):
        self._star_level = value
    @property
    def star_level_total(self):
        return self._star_level_total

    @star_level_total.setter
    def star_level_total(self, value):
        self._star_level_total = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.digital_poi_id:
            if hasattr(self.digital_poi_id, 'to_alipay_dict'):
                params['digital_poi_id'] = self.digital_poi_id.to_alipay_dict()
            else:
                params['digital_poi_id'] = self.digital_poi_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.review_create_time:
            if hasattr(self.review_create_time, 'to_alipay_dict'):
                params['review_create_time'] = self.review_create_time.to_alipay_dict()
            else:
                params['review_create_time'] = self.review_create_time
        if self.review_images:
            if hasattr(self.review_images, 'to_alipay_dict'):
                params['review_images'] = self.review_images.to_alipay_dict()
            else:
                params['review_images'] = self.review_images
        if self.review_modify_time:
            if hasattr(self.review_modify_time, 'to_alipay_dict'):
                params['review_modify_time'] = self.review_modify_time.to_alipay_dict()
            else:
                params['review_modify_time'] = self.review_modify_time
        if self.review_text:
            if hasattr(self.review_text, 'to_alipay_dict'):
                params['review_text'] = self.review_text.to_alipay_dict()
            else:
                params['review_text'] = self.review_text
        if self.review_videos:
            if hasattr(self.review_videos, 'to_alipay_dict'):
                params['review_videos'] = self.review_videos.to_alipay_dict()
            else:
                params['review_videos'] = self.review_videos
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.star_level:
            if hasattr(self.star_level, 'to_alipay_dict'):
                params['star_level'] = self.star_level.to_alipay_dict()
            else:
                params['star_level'] = self.star_level
        if self.star_level_total:
            if hasattr(self.star_level_total, 'to_alipay_dict'):
                params['star_level_total'] = self.star_level_total.to_alipay_dict()
            else:
                params['star_level_total'] = self.star_level_total
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
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
        o = AntMerchantExpandShopReviewCreateModel()
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'digital_poi_id' in d:
            o.digital_poi_id = d['digital_poi_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'review_create_time' in d:
            o.review_create_time = d['review_create_time']
        if 'review_images' in d:
            o.review_images = d['review_images']
        if 'review_modify_time' in d:
            o.review_modify_time = d['review_modify_time']
        if 'review_text' in d:
            o.review_text = d['review_text']
        if 'review_videos' in d:
            o.review_videos = d['review_videos']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'star_level' in d:
            o.star_level = d['star_level']
        if 'star_level_total' in d:
            o.star_level_total = d['star_level_total']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



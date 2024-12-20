#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CouponMsgVO(object):

    def __init__(self):
        self._activity_id = None
        self._activity_id_list = None
        self._image_id = None
        self._long_introduce_text = None
        self._multi_coupon = None
        self._short_introduce_text_list = None
        self._title = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_id_list(self):
        return self._activity_id_list

    @activity_id_list.setter
    def activity_id_list(self, value):
        if isinstance(value, list):
            self._activity_id_list = list()
            for i in value:
                self._activity_id_list.append(i)
    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value
    @property
    def long_introduce_text(self):
        return self._long_introduce_text

    @long_introduce_text.setter
    def long_introduce_text(self, value):
        self._long_introduce_text = value
    @property
    def multi_coupon(self):
        return self._multi_coupon

    @multi_coupon.setter
    def multi_coupon(self, value):
        self._multi_coupon = value
    @property
    def short_introduce_text_list(self):
        return self._short_introduce_text_list

    @short_introduce_text_list.setter
    def short_introduce_text_list(self, value):
        if isinstance(value, list):
            self._short_introduce_text_list = list()
            for i in value:
                self._short_introduce_text_list.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_id_list:
            if isinstance(self.activity_id_list, list):
                for i in range(0, len(self.activity_id_list)):
                    element = self.activity_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_id_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_id_list, 'to_alipay_dict'):
                params['activity_id_list'] = self.activity_id_list.to_alipay_dict()
            else:
                params['activity_id_list'] = self.activity_id_list
        if self.image_id:
            if hasattr(self.image_id, 'to_alipay_dict'):
                params['image_id'] = self.image_id.to_alipay_dict()
            else:
                params['image_id'] = self.image_id
        if self.long_introduce_text:
            if hasattr(self.long_introduce_text, 'to_alipay_dict'):
                params['long_introduce_text'] = self.long_introduce_text.to_alipay_dict()
            else:
                params['long_introduce_text'] = self.long_introduce_text
        if self.multi_coupon:
            if hasattr(self.multi_coupon, 'to_alipay_dict'):
                params['multi_coupon'] = self.multi_coupon.to_alipay_dict()
            else:
                params['multi_coupon'] = self.multi_coupon
        if self.short_introduce_text_list:
            if isinstance(self.short_introduce_text_list, list):
                for i in range(0, len(self.short_introduce_text_list)):
                    element = self.short_introduce_text_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.short_introduce_text_list[i] = element.to_alipay_dict()
            if hasattr(self.short_introduce_text_list, 'to_alipay_dict'):
                params['short_introduce_text_list'] = self.short_introduce_text_list.to_alipay_dict()
            else:
                params['short_introduce_text_list'] = self.short_introduce_text_list
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
        o = CouponMsgVO()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_id_list' in d:
            o.activity_id_list = d['activity_id_list']
        if 'image_id' in d:
            o.image_id = d['image_id']
        if 'long_introduce_text' in d:
            o.long_introduce_text = d['long_introduce_text']
        if 'multi_coupon' in d:
            o.multi_coupon = d['multi_coupon']
        if 'short_introduce_text_list' in d:
            o.short_introduce_text_list = d['short_introduce_text_list']
        if 'title' in d:
            o.title = d['title']
        return o



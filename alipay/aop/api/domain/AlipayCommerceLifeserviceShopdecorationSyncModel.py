#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LifeServiceShopBusinessTime import LifeServiceShopBusinessTime
from alipay.aop.api.domain.LifeServiceAttr import LifeServiceAttr


class AlipayCommerceLifeserviceShopdecorationSyncModel(object):

    def __init__(self):
        self._shop_business_time = None
        self._shop_commercial_tags = None
        self._shop_decoration_attrs = None
        self._shop_id = None
        self._shop_logo = None
        self._shop_vibes_images = None

    @property
    def shop_business_time(self):
        return self._shop_business_time

    @shop_business_time.setter
    def shop_business_time(self, value):
        if isinstance(value, list):
            self._shop_business_time = list()
            for i in value:
                if isinstance(i, LifeServiceShopBusinessTime):
                    self._shop_business_time.append(i)
                else:
                    self._shop_business_time.append(LifeServiceShopBusinessTime.from_alipay_dict(i))
    @property
    def shop_commercial_tags(self):
        return self._shop_commercial_tags

    @shop_commercial_tags.setter
    def shop_commercial_tags(self, value):
        if isinstance(value, list):
            self._shop_commercial_tags = list()
            for i in value:
                self._shop_commercial_tags.append(i)
    @property
    def shop_decoration_attrs(self):
        return self._shop_decoration_attrs

    @shop_decoration_attrs.setter
    def shop_decoration_attrs(self, value):
        if isinstance(value, list):
            self._shop_decoration_attrs = list()
            for i in value:
                if isinstance(i, LifeServiceAttr):
                    self._shop_decoration_attrs.append(i)
                else:
                    self._shop_decoration_attrs.append(LifeServiceAttr.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_logo(self):
        return self._shop_logo

    @shop_logo.setter
    def shop_logo(self, value):
        self._shop_logo = value
    @property
    def shop_vibes_images(self):
        return self._shop_vibes_images

    @shop_vibes_images.setter
    def shop_vibes_images(self, value):
        if isinstance(value, list):
            self._shop_vibes_images = list()
            for i in value:
                self._shop_vibes_images.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.shop_business_time:
            if isinstance(self.shop_business_time, list):
                for i in range(0, len(self.shop_business_time)):
                    element = self.shop_business_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_business_time[i] = element.to_alipay_dict()
            if hasattr(self.shop_business_time, 'to_alipay_dict'):
                params['shop_business_time'] = self.shop_business_time.to_alipay_dict()
            else:
                params['shop_business_time'] = self.shop_business_time
        if self.shop_commercial_tags:
            if isinstance(self.shop_commercial_tags, list):
                for i in range(0, len(self.shop_commercial_tags)):
                    element = self.shop_commercial_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_commercial_tags[i] = element.to_alipay_dict()
            if hasattr(self.shop_commercial_tags, 'to_alipay_dict'):
                params['shop_commercial_tags'] = self.shop_commercial_tags.to_alipay_dict()
            else:
                params['shop_commercial_tags'] = self.shop_commercial_tags
        if self.shop_decoration_attrs:
            if isinstance(self.shop_decoration_attrs, list):
                for i in range(0, len(self.shop_decoration_attrs)):
                    element = self.shop_decoration_attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_decoration_attrs[i] = element.to_alipay_dict()
            if hasattr(self.shop_decoration_attrs, 'to_alipay_dict'):
                params['shop_decoration_attrs'] = self.shop_decoration_attrs.to_alipay_dict()
            else:
                params['shop_decoration_attrs'] = self.shop_decoration_attrs
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_logo:
            if hasattr(self.shop_logo, 'to_alipay_dict'):
                params['shop_logo'] = self.shop_logo.to_alipay_dict()
            else:
                params['shop_logo'] = self.shop_logo
        if self.shop_vibes_images:
            if isinstance(self.shop_vibes_images, list):
                for i in range(0, len(self.shop_vibes_images)):
                    element = self.shop_vibes_images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_vibes_images[i] = element.to_alipay_dict()
            if hasattr(self.shop_vibes_images, 'to_alipay_dict'):
                params['shop_vibes_images'] = self.shop_vibes_images.to_alipay_dict()
            else:
                params['shop_vibes_images'] = self.shop_vibes_images
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceShopdecorationSyncModel()
        if 'shop_business_time' in d:
            o.shop_business_time = d['shop_business_time']
        if 'shop_commercial_tags' in d:
            o.shop_commercial_tags = d['shop_commercial_tags']
        if 'shop_decoration_attrs' in d:
            o.shop_decoration_attrs = d['shop_decoration_attrs']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_logo' in d:
            o.shop_logo = d['shop_logo']
        if 'shop_vibes_images' in d:
            o.shop_vibes_images = d['shop_vibes_images']
        return o



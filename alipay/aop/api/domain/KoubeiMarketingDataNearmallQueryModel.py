#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataNearmallQueryModel(object):

    def __init__(self):
        self._app_channel = None
        self._city_id = None
        self._page_no = None
        self._page_size = None
        self._product_id = None
        self._product_version = None
        self._radius = None
        self._user_id = None
        self._x = None
        self._y = None

    @property
    def app_channel(self):
        return self._app_channel

    @app_channel.setter
    def app_channel(self, value):
        self._app_channel = value
    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        self._city_id = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_version(self):
        return self._product_version

    @product_version.setter
    def product_version(self, value):
        self._product_version = value
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_channel:
            if hasattr(self.app_channel, 'to_alipay_dict'):
                params['app_channel'] = self.app_channel.to_alipay_dict()
            else:
                params['app_channel'] = self.app_channel
        if self.city_id:
            if hasattr(self.city_id, 'to_alipay_dict'):
                params['city_id'] = self.city_id.to_alipay_dict()
            else:
                params['city_id'] = self.city_id
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.product_version:
            if hasattr(self.product_version, 'to_alipay_dict'):
                params['product_version'] = self.product_version.to_alipay_dict()
            else:
                params['product_version'] = self.product_version
        if self.radius:
            if hasattr(self.radius, 'to_alipay_dict'):
                params['radius'] = self.radius.to_alipay_dict()
            else:
                params['radius'] = self.radius
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.x:
            if hasattr(self.x, 'to_alipay_dict'):
                params['x'] = self.x.to_alipay_dict()
            else:
                params['x'] = self.x
        if self.y:
            if hasattr(self.y, 'to_alipay_dict'):
                params['y'] = self.y.to_alipay_dict()
            else:
                params['y'] = self.y
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataNearmallQueryModel()
        if 'app_channel' in d:
            o.app_channel = d['app_channel']
        if 'city_id' in d:
            o.city_id = d['city_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_version' in d:
            o.product_version = d['product_version']
        if 'radius' in d:
            o.radius = d['radius']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'x' in d:
            o.x = d['x']
        if 'y' in d:
            o.y = d['y']
        return o



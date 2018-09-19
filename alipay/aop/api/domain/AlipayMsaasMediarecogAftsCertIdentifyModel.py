#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogAftsCertIdentifyModel(object):

    def __init__(self):
        self._ext = None
        self._h = None
        self._plate_number = None
        self._url = None
        self._user_id = None
        self._w = None
        self._x = None
        self._y = None

    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, value):
        self._h = value
    @property
    def plate_number(self):
        return self._plate_number

    @plate_number.setter
    def plate_number(self, value):
        self._plate_number = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, value):
        self._w = value
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
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.h:
            if hasattr(self.h, 'to_alipay_dict'):
                params['h'] = self.h.to_alipay_dict()
            else:
                params['h'] = self.h
        if self.plate_number:
            if hasattr(self.plate_number, 'to_alipay_dict'):
                params['plate_number'] = self.plate_number.to_alipay_dict()
            else:
                params['plate_number'] = self.plate_number
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.w:
            if hasattr(self.w, 'to_alipay_dict'):
                params['w'] = self.w.to_alipay_dict()
            else:
                params['w'] = self.w
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
        o = AlipayMsaasMediarecogAftsCertIdentifyModel()
        if 'ext' in d:
            o.ext = d['ext']
        if 'h' in d:
            o.h = d['h']
        if 'plate_number' in d:
            o.plate_number = d['plate_number']
        if 'url' in d:
            o.url = d['url']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'w' in d:
            o.w = d['w']
        if 'x' in d:
            o.x = d['x']
        if 'y' in d:
            o.y = d['y']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EscrowBusinessInfo(object):

    def __init__(self):
        self._app_type = None
        self._image_id = None
        self._mrch_biz_address = None
        self._place_type = None
        self._place_url = None

    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        self._app_type = value
    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value
    @property
    def mrch_biz_address(self):
        return self._mrch_biz_address

    @mrch_biz_address.setter
    def mrch_biz_address(self, value):
        self._mrch_biz_address = value
    @property
    def place_type(self):
        return self._place_type

    @place_type.setter
    def place_type(self, value):
        self._place_type = value
    @property
    def place_url(self):
        return self._place_url

    @place_url.setter
    def place_url(self, value):
        self._place_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_type:
            if hasattr(self.app_type, 'to_alipay_dict'):
                params['app_type'] = self.app_type.to_alipay_dict()
            else:
                params['app_type'] = self.app_type
        if self.image_id:
            if hasattr(self.image_id, 'to_alipay_dict'):
                params['image_id'] = self.image_id.to_alipay_dict()
            else:
                params['image_id'] = self.image_id
        if self.mrch_biz_address:
            if hasattr(self.mrch_biz_address, 'to_alipay_dict'):
                params['mrch_biz_address'] = self.mrch_biz_address.to_alipay_dict()
            else:
                params['mrch_biz_address'] = self.mrch_biz_address
        if self.place_type:
            if hasattr(self.place_type, 'to_alipay_dict'):
                params['place_type'] = self.place_type.to_alipay_dict()
            else:
                params['place_type'] = self.place_type
        if self.place_url:
            if hasattr(self.place_url, 'to_alipay_dict'):
                params['place_url'] = self.place_url.to_alipay_dict()
            else:
                params['place_url'] = self.place_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EscrowBusinessInfo()
        if 'app_type' in d:
            o.app_type = d['app_type']
        if 'image_id' in d:
            o.image_id = d['image_id']
        if 'mrch_biz_address' in d:
            o.mrch_biz_address = d['mrch_biz_address']
        if 'place_type' in d:
            o.place_type = d['place_type']
        if 'place_url' in d:
            o.place_url = d['place_url']
        return o



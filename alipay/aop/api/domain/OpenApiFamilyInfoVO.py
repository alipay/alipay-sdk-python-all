#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiFamilyInfoVO(object):

    def __init__(self):
        self._family_count = None
        self._family_img = None
        self._family_max_count = None
        self._family_state = None
        self._family_url = None
        self._prize_img = None
        self._prize_name = None
        self._sku_id = None

    @property
    def family_count(self):
        return self._family_count

    @family_count.setter
    def family_count(self, value):
        self._family_count = value
    @property
    def family_img(self):
        return self._family_img

    @family_img.setter
    def family_img(self, value):
        self._family_img = value
    @property
    def family_max_count(self):
        return self._family_max_count

    @family_max_count.setter
    def family_max_count(self, value):
        self._family_max_count = value
    @property
    def family_state(self):
        return self._family_state

    @family_state.setter
    def family_state(self, value):
        self._family_state = value
    @property
    def family_url(self):
        return self._family_url

    @family_url.setter
    def family_url(self, value):
        self._family_url = value
    @property
    def prize_img(self):
        return self._prize_img

    @prize_img.setter
    def prize_img(self, value):
        self._prize_img = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.family_count:
            if hasattr(self.family_count, 'to_alipay_dict'):
                params['family_count'] = self.family_count.to_alipay_dict()
            else:
                params['family_count'] = self.family_count
        if self.family_img:
            if hasattr(self.family_img, 'to_alipay_dict'):
                params['family_img'] = self.family_img.to_alipay_dict()
            else:
                params['family_img'] = self.family_img
        if self.family_max_count:
            if hasattr(self.family_max_count, 'to_alipay_dict'):
                params['family_max_count'] = self.family_max_count.to_alipay_dict()
            else:
                params['family_max_count'] = self.family_max_count
        if self.family_state:
            if hasattr(self.family_state, 'to_alipay_dict'):
                params['family_state'] = self.family_state.to_alipay_dict()
            else:
                params['family_state'] = self.family_state
        if self.family_url:
            if hasattr(self.family_url, 'to_alipay_dict'):
                params['family_url'] = self.family_url.to_alipay_dict()
            else:
                params['family_url'] = self.family_url
        if self.prize_img:
            if hasattr(self.prize_img, 'to_alipay_dict'):
                params['prize_img'] = self.prize_img.to_alipay_dict()
            else:
                params['prize_img'] = self.prize_img
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiFamilyInfoVO()
        if 'family_count' in d:
            o.family_count = d['family_count']
        if 'family_img' in d:
            o.family_img = d['family_img']
        if 'family_max_count' in d:
            o.family_max_count = d['family_max_count']
        if 'family_state' in d:
            o.family_state = d['family_state']
        if 'family_url' in d:
            o.family_url = d['family_url']
        if 'prize_img' in d:
            o.prize_img = d['prize_img']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o



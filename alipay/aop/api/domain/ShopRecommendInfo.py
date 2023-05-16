#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopRecommendInfo(object):

    def __init__(self):
        self._recommend = None
        self._recommend_address = None
        self._recommend_latitude = None
        self._recommend_longtitude = None
        self._recommend_name = None
        self._unconfidence_reason = None

    @property
    def recommend(self):
        return self._recommend

    @recommend.setter
    def recommend(self, value):
        self._recommend = value
    @property
    def recommend_address(self):
        return self._recommend_address

    @recommend_address.setter
    def recommend_address(self, value):
        self._recommend_address = value
    @property
    def recommend_latitude(self):
        return self._recommend_latitude

    @recommend_latitude.setter
    def recommend_latitude(self, value):
        self._recommend_latitude = value
    @property
    def recommend_longtitude(self):
        return self._recommend_longtitude

    @recommend_longtitude.setter
    def recommend_longtitude(self, value):
        self._recommend_longtitude = value
    @property
    def recommend_name(self):
        return self._recommend_name

    @recommend_name.setter
    def recommend_name(self, value):
        self._recommend_name = value
    @property
    def unconfidence_reason(self):
        return self._unconfidence_reason

    @unconfidence_reason.setter
    def unconfidence_reason(self, value):
        self._unconfidence_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.recommend:
            if hasattr(self.recommend, 'to_alipay_dict'):
                params['recommend'] = self.recommend.to_alipay_dict()
            else:
                params['recommend'] = self.recommend
        if self.recommend_address:
            if hasattr(self.recommend_address, 'to_alipay_dict'):
                params['recommend_address'] = self.recommend_address.to_alipay_dict()
            else:
                params['recommend_address'] = self.recommend_address
        if self.recommend_latitude:
            if hasattr(self.recommend_latitude, 'to_alipay_dict'):
                params['recommend_latitude'] = self.recommend_latitude.to_alipay_dict()
            else:
                params['recommend_latitude'] = self.recommend_latitude
        if self.recommend_longtitude:
            if hasattr(self.recommend_longtitude, 'to_alipay_dict'):
                params['recommend_longtitude'] = self.recommend_longtitude.to_alipay_dict()
            else:
                params['recommend_longtitude'] = self.recommend_longtitude
        if self.recommend_name:
            if hasattr(self.recommend_name, 'to_alipay_dict'):
                params['recommend_name'] = self.recommend_name.to_alipay_dict()
            else:
                params['recommend_name'] = self.recommend_name
        if self.unconfidence_reason:
            if hasattr(self.unconfidence_reason, 'to_alipay_dict'):
                params['unconfidence_reason'] = self.unconfidence_reason.to_alipay_dict()
            else:
                params['unconfidence_reason'] = self.unconfidence_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopRecommendInfo()
        if 'recommend' in d:
            o.recommend = d['recommend']
        if 'recommend_address' in d:
            o.recommend_address = d['recommend_address']
        if 'recommend_latitude' in d:
            o.recommend_latitude = d['recommend_latitude']
        if 'recommend_longtitude' in d:
            o.recommend_longtitude = d['recommend_longtitude']
        if 'recommend_name' in d:
            o.recommend_name = d['recommend_name']
        if 'unconfidence_reason' in d:
            o.unconfidence_reason = d['unconfidence_reason']
        return o



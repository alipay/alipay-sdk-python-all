#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IcommunityContentLocationInfo(object):

    def __init__(self):
        self._location_detail = None
        self._location_latitude = None
        self._location_longitude = None
        self._location_name = None

    @property
    def location_detail(self):
        return self._location_detail

    @location_detail.setter
    def location_detail(self, value):
        self._location_detail = value
    @property
    def location_latitude(self):
        return self._location_latitude

    @location_latitude.setter
    def location_latitude(self, value):
        self._location_latitude = value
    @property
    def location_longitude(self):
        return self._location_longitude

    @location_longitude.setter
    def location_longitude(self, value):
        self._location_longitude = value
    @property
    def location_name(self):
        return self._location_name

    @location_name.setter
    def location_name(self, value):
        self._location_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.location_detail:
            if hasattr(self.location_detail, 'to_alipay_dict'):
                params['location_detail'] = self.location_detail.to_alipay_dict()
            else:
                params['location_detail'] = self.location_detail
        if self.location_latitude:
            if hasattr(self.location_latitude, 'to_alipay_dict'):
                params['location_latitude'] = self.location_latitude.to_alipay_dict()
            else:
                params['location_latitude'] = self.location_latitude
        if self.location_longitude:
            if hasattr(self.location_longitude, 'to_alipay_dict'):
                params['location_longitude'] = self.location_longitude.to_alipay_dict()
            else:
                params['location_longitude'] = self.location_longitude
        if self.location_name:
            if hasattr(self.location_name, 'to_alipay_dict'):
                params['location_name'] = self.location_name.to_alipay_dict()
            else:
                params['location_name'] = self.location_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IcommunityContentLocationInfo()
        if 'location_detail' in d:
            o.location_detail = d['location_detail']
        if 'location_latitude' in d:
            o.location_latitude = d['location_latitude']
        if 'location_longitude' in d:
            o.location_longitude = d['location_longitude']
        if 'location_name' in d:
            o.location_name = d['location_name']
        return o



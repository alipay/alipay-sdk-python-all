#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NearbyCrowdDensity(object):

    def __init__(self):
        self._crowd_density = None
        self._geohash = None

    @property
    def crowd_density(self):
        return self._crowd_density

    @crowd_density.setter
    def crowd_density(self, value):
        self._crowd_density = value
    @property
    def geohash(self):
        return self._geohash

    @geohash.setter
    def geohash(self, value):
        self._geohash = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_density:
            if hasattr(self.crowd_density, 'to_alipay_dict'):
                params['crowd_density'] = self.crowd_density.to_alipay_dict()
            else:
                params['crowd_density'] = self.crowd_density
        if self.geohash:
            if hasattr(self.geohash, 'to_alipay_dict'):
                params['geohash'] = self.geohash.to_alipay_dict()
            else:
                params['geohash'] = self.geohash
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NearbyCrowdDensity()
        if 'crowd_density' in d:
            o.crowd_density = d['crowd_density']
        if 'geohash' in d:
            o.geohash = d['geohash']
        return o



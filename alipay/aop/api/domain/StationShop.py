#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StationShop(object):

    def __init__(self):
        self._station_shop_id = None
        self._station_shop_name = None

    @property
    def station_shop_id(self):
        return self._station_shop_id

    @station_shop_id.setter
    def station_shop_id(self, value):
        self._station_shop_id = value
    @property
    def station_shop_name(self):
        return self._station_shop_name

    @station_shop_name.setter
    def station_shop_name(self, value):
        self._station_shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.station_shop_id:
            if hasattr(self.station_shop_id, 'to_alipay_dict'):
                params['station_shop_id'] = self.station_shop_id.to_alipay_dict()
            else:
                params['station_shop_id'] = self.station_shop_id
        if self.station_shop_name:
            if hasattr(self.station_shop_name, 'to_alipay_dict'):
                params['station_shop_name'] = self.station_shop_name.to_alipay_dict()
            else:
                params['station_shop_name'] = self.station_shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StationShop()
        if 'station_shop_id' in d:
            o.station_shop_id = d['station_shop_id']
        if 'station_shop_name' in d:
            o.station_shop_name = d['station_shop_name']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcLocationInfo import EcLocationInfo


class EcTradingAreaInfo(object):

    def __init__(self):
        self._location_info = None
        self._trading_area_id = None
        self._trading_area_name = None

    @property
    def location_info(self):
        return self._location_info

    @location_info.setter
    def location_info(self, value):
        if isinstance(value, EcLocationInfo):
            self._location_info = value
        else:
            self._location_info = EcLocationInfo.from_alipay_dict(value)
    @property
    def trading_area_id(self):
        return self._trading_area_id

    @trading_area_id.setter
    def trading_area_id(self, value):
        self._trading_area_id = value
    @property
    def trading_area_name(self):
        return self._trading_area_name

    @trading_area_name.setter
    def trading_area_name(self, value):
        self._trading_area_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.location_info:
            if hasattr(self.location_info, 'to_alipay_dict'):
                params['location_info'] = self.location_info.to_alipay_dict()
            else:
                params['location_info'] = self.location_info
        if self.trading_area_id:
            if hasattr(self.trading_area_id, 'to_alipay_dict'):
                params['trading_area_id'] = self.trading_area_id.to_alipay_dict()
            else:
                params['trading_area_id'] = self.trading_area_id
        if self.trading_area_name:
            if hasattr(self.trading_area_name, 'to_alipay_dict'):
                params['trading_area_name'] = self.trading_area_name.to_alipay_dict()
            else:
                params['trading_area_name'] = self.trading_area_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcTradingAreaInfo()
        if 'location_info' in d:
            o.location_info = d['location_info']
        if 'trading_area_id' in d:
            o.trading_area_id = d['trading_area_id']
        if 'trading_area_name' in d:
            o.trading_area_name = d['trading_area_name']
        return o



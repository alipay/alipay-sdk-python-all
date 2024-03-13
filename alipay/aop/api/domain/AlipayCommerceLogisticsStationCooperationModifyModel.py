#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsStationCooperationModifyModel(object):

    def __init__(self):
        self._event_type = None
        self._open_id = None
        self._station_brand_id = None
        self._station_shop_id = None
        self._station_user_id = None
        self._user_id = None

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def station_brand_id(self):
        return self._station_brand_id

    @station_brand_id.setter
    def station_brand_id(self, value):
        self._station_brand_id = value
    @property
    def station_shop_id(self):
        return self._station_shop_id

    @station_shop_id.setter
    def station_shop_id(self, value):
        self._station_shop_id = value
    @property
    def station_user_id(self):
        return self._station_user_id

    @station_user_id.setter
    def station_user_id(self, value):
        self._station_user_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.station_brand_id:
            if hasattr(self.station_brand_id, 'to_alipay_dict'):
                params['station_brand_id'] = self.station_brand_id.to_alipay_dict()
            else:
                params['station_brand_id'] = self.station_brand_id
        if self.station_shop_id:
            if hasattr(self.station_shop_id, 'to_alipay_dict'):
                params['station_shop_id'] = self.station_shop_id.to_alipay_dict()
            else:
                params['station_shop_id'] = self.station_shop_id
        if self.station_user_id:
            if hasattr(self.station_user_id, 'to_alipay_dict'):
                params['station_user_id'] = self.station_user_id.to_alipay_dict()
            else:
                params['station_user_id'] = self.station_user_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsStationCooperationModifyModel()
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'station_brand_id' in d:
            o.station_brand_id = d['station_brand_id']
        if 'station_shop_id' in d:
            o.station_shop_id = d['station_shop_id']
        if 'station_user_id' in d:
            o.station_user_id = d['station_user_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



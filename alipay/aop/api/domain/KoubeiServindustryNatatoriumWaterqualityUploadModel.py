#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiServindustryNatatoriumWaterqualityUploadModel(object):

    def __init__(self):
        self._commodity_id = None
        self._current_num = None
        self._currentnum_update_time = None
        self._external_id = None
        self._footpool_cl_qualified = None
        self._footpool_cl_remain = None
        self._footpool_cl_remain_standard = None
        self._limit_num = None
        self._mainpool_cl_qualified = None
        self._mainpool_cl_remain = None
        self._mainpool_cl_remain_standard = None
        self._pool_volume = None
        self._remark = None
        self._request_id = None
        self._shop_id = None
        self._water_change = None
        self._water_change_percent = None
        self._water_change_qualified = None
        self._water_change_standard = None
        self._water_check_time = None
        self._water_ph = None
        self._water_ph_qualified = None
        self._water_ph_standard = None
        self._water_qualified = None
        self._water_temperature = None
        self._water_temperature_qualified = None
        self._water_temperature_standard = None
        self._water_update_time = None

    @property
    def commodity_id(self):
        return self._commodity_id

    @commodity_id.setter
    def commodity_id(self, value):
        self._commodity_id = value
    @property
    def current_num(self):
        return self._current_num

    @current_num.setter
    def current_num(self, value):
        self._current_num = value
    @property
    def currentnum_update_time(self):
        return self._currentnum_update_time

    @currentnum_update_time.setter
    def currentnum_update_time(self, value):
        self._currentnum_update_time = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def footpool_cl_qualified(self):
        return self._footpool_cl_qualified

    @footpool_cl_qualified.setter
    def footpool_cl_qualified(self, value):
        self._footpool_cl_qualified = value
    @property
    def footpool_cl_remain(self):
        return self._footpool_cl_remain

    @footpool_cl_remain.setter
    def footpool_cl_remain(self, value):
        self._footpool_cl_remain = value
    @property
    def footpool_cl_remain_standard(self):
        return self._footpool_cl_remain_standard

    @footpool_cl_remain_standard.setter
    def footpool_cl_remain_standard(self, value):
        self._footpool_cl_remain_standard = value
    @property
    def limit_num(self):
        return self._limit_num

    @limit_num.setter
    def limit_num(self, value):
        self._limit_num = value
    @property
    def mainpool_cl_qualified(self):
        return self._mainpool_cl_qualified

    @mainpool_cl_qualified.setter
    def mainpool_cl_qualified(self, value):
        self._mainpool_cl_qualified = value
    @property
    def mainpool_cl_remain(self):
        return self._mainpool_cl_remain

    @mainpool_cl_remain.setter
    def mainpool_cl_remain(self, value):
        self._mainpool_cl_remain = value
    @property
    def mainpool_cl_remain_standard(self):
        return self._mainpool_cl_remain_standard

    @mainpool_cl_remain_standard.setter
    def mainpool_cl_remain_standard(self, value):
        self._mainpool_cl_remain_standard = value
    @property
    def pool_volume(self):
        return self._pool_volume

    @pool_volume.setter
    def pool_volume(self, value):
        self._pool_volume = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def water_change(self):
        return self._water_change

    @water_change.setter
    def water_change(self, value):
        self._water_change = value
    @property
    def water_change_percent(self):
        return self._water_change_percent

    @water_change_percent.setter
    def water_change_percent(self, value):
        self._water_change_percent = value
    @property
    def water_change_qualified(self):
        return self._water_change_qualified

    @water_change_qualified.setter
    def water_change_qualified(self, value):
        self._water_change_qualified = value
    @property
    def water_change_standard(self):
        return self._water_change_standard

    @water_change_standard.setter
    def water_change_standard(self, value):
        self._water_change_standard = value
    @property
    def water_check_time(self):
        return self._water_check_time

    @water_check_time.setter
    def water_check_time(self, value):
        self._water_check_time = value
    @property
    def water_ph(self):
        return self._water_ph

    @water_ph.setter
    def water_ph(self, value):
        self._water_ph = value
    @property
    def water_ph_qualified(self):
        return self._water_ph_qualified

    @water_ph_qualified.setter
    def water_ph_qualified(self, value):
        self._water_ph_qualified = value
    @property
    def water_ph_standard(self):
        return self._water_ph_standard

    @water_ph_standard.setter
    def water_ph_standard(self, value):
        self._water_ph_standard = value
    @property
    def water_qualified(self):
        return self._water_qualified

    @water_qualified.setter
    def water_qualified(self, value):
        self._water_qualified = value
    @property
    def water_temperature(self):
        return self._water_temperature

    @water_temperature.setter
    def water_temperature(self, value):
        self._water_temperature = value
    @property
    def water_temperature_qualified(self):
        return self._water_temperature_qualified

    @water_temperature_qualified.setter
    def water_temperature_qualified(self, value):
        self._water_temperature_qualified = value
    @property
    def water_temperature_standard(self):
        return self._water_temperature_standard

    @water_temperature_standard.setter
    def water_temperature_standard(self, value):
        self._water_temperature_standard = value
    @property
    def water_update_time(self):
        return self._water_update_time

    @water_update_time.setter
    def water_update_time(self, value):
        self._water_update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_id:
            if hasattr(self.commodity_id, 'to_alipay_dict'):
                params['commodity_id'] = self.commodity_id.to_alipay_dict()
            else:
                params['commodity_id'] = self.commodity_id
        if self.current_num:
            if hasattr(self.current_num, 'to_alipay_dict'):
                params['current_num'] = self.current_num.to_alipay_dict()
            else:
                params['current_num'] = self.current_num
        if self.currentnum_update_time:
            if hasattr(self.currentnum_update_time, 'to_alipay_dict'):
                params['currentnum_update_time'] = self.currentnum_update_time.to_alipay_dict()
            else:
                params['currentnum_update_time'] = self.currentnum_update_time
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.footpool_cl_qualified:
            if hasattr(self.footpool_cl_qualified, 'to_alipay_dict'):
                params['footpool_cl_qualified'] = self.footpool_cl_qualified.to_alipay_dict()
            else:
                params['footpool_cl_qualified'] = self.footpool_cl_qualified
        if self.footpool_cl_remain:
            if hasattr(self.footpool_cl_remain, 'to_alipay_dict'):
                params['footpool_cl_remain'] = self.footpool_cl_remain.to_alipay_dict()
            else:
                params['footpool_cl_remain'] = self.footpool_cl_remain
        if self.footpool_cl_remain_standard:
            if hasattr(self.footpool_cl_remain_standard, 'to_alipay_dict'):
                params['footpool_cl_remain_standard'] = self.footpool_cl_remain_standard.to_alipay_dict()
            else:
                params['footpool_cl_remain_standard'] = self.footpool_cl_remain_standard
        if self.limit_num:
            if hasattr(self.limit_num, 'to_alipay_dict'):
                params['limit_num'] = self.limit_num.to_alipay_dict()
            else:
                params['limit_num'] = self.limit_num
        if self.mainpool_cl_qualified:
            if hasattr(self.mainpool_cl_qualified, 'to_alipay_dict'):
                params['mainpool_cl_qualified'] = self.mainpool_cl_qualified.to_alipay_dict()
            else:
                params['mainpool_cl_qualified'] = self.mainpool_cl_qualified
        if self.mainpool_cl_remain:
            if hasattr(self.mainpool_cl_remain, 'to_alipay_dict'):
                params['mainpool_cl_remain'] = self.mainpool_cl_remain.to_alipay_dict()
            else:
                params['mainpool_cl_remain'] = self.mainpool_cl_remain
        if self.mainpool_cl_remain_standard:
            if hasattr(self.mainpool_cl_remain_standard, 'to_alipay_dict'):
                params['mainpool_cl_remain_standard'] = self.mainpool_cl_remain_standard.to_alipay_dict()
            else:
                params['mainpool_cl_remain_standard'] = self.mainpool_cl_remain_standard
        if self.pool_volume:
            if hasattr(self.pool_volume, 'to_alipay_dict'):
                params['pool_volume'] = self.pool_volume.to_alipay_dict()
            else:
                params['pool_volume'] = self.pool_volume
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.water_change:
            if hasattr(self.water_change, 'to_alipay_dict'):
                params['water_change'] = self.water_change.to_alipay_dict()
            else:
                params['water_change'] = self.water_change
        if self.water_change_percent:
            if hasattr(self.water_change_percent, 'to_alipay_dict'):
                params['water_change_percent'] = self.water_change_percent.to_alipay_dict()
            else:
                params['water_change_percent'] = self.water_change_percent
        if self.water_change_qualified:
            if hasattr(self.water_change_qualified, 'to_alipay_dict'):
                params['water_change_qualified'] = self.water_change_qualified.to_alipay_dict()
            else:
                params['water_change_qualified'] = self.water_change_qualified
        if self.water_change_standard:
            if hasattr(self.water_change_standard, 'to_alipay_dict'):
                params['water_change_standard'] = self.water_change_standard.to_alipay_dict()
            else:
                params['water_change_standard'] = self.water_change_standard
        if self.water_check_time:
            if hasattr(self.water_check_time, 'to_alipay_dict'):
                params['water_check_time'] = self.water_check_time.to_alipay_dict()
            else:
                params['water_check_time'] = self.water_check_time
        if self.water_ph:
            if hasattr(self.water_ph, 'to_alipay_dict'):
                params['water_ph'] = self.water_ph.to_alipay_dict()
            else:
                params['water_ph'] = self.water_ph
        if self.water_ph_qualified:
            if hasattr(self.water_ph_qualified, 'to_alipay_dict'):
                params['water_ph_qualified'] = self.water_ph_qualified.to_alipay_dict()
            else:
                params['water_ph_qualified'] = self.water_ph_qualified
        if self.water_ph_standard:
            if hasattr(self.water_ph_standard, 'to_alipay_dict'):
                params['water_ph_standard'] = self.water_ph_standard.to_alipay_dict()
            else:
                params['water_ph_standard'] = self.water_ph_standard
        if self.water_qualified:
            if hasattr(self.water_qualified, 'to_alipay_dict'):
                params['water_qualified'] = self.water_qualified.to_alipay_dict()
            else:
                params['water_qualified'] = self.water_qualified
        if self.water_temperature:
            if hasattr(self.water_temperature, 'to_alipay_dict'):
                params['water_temperature'] = self.water_temperature.to_alipay_dict()
            else:
                params['water_temperature'] = self.water_temperature
        if self.water_temperature_qualified:
            if hasattr(self.water_temperature_qualified, 'to_alipay_dict'):
                params['water_temperature_qualified'] = self.water_temperature_qualified.to_alipay_dict()
            else:
                params['water_temperature_qualified'] = self.water_temperature_qualified
        if self.water_temperature_standard:
            if hasattr(self.water_temperature_standard, 'to_alipay_dict'):
                params['water_temperature_standard'] = self.water_temperature_standard.to_alipay_dict()
            else:
                params['water_temperature_standard'] = self.water_temperature_standard
        if self.water_update_time:
            if hasattr(self.water_update_time, 'to_alipay_dict'):
                params['water_update_time'] = self.water_update_time.to_alipay_dict()
            else:
                params['water_update_time'] = self.water_update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiServindustryNatatoriumWaterqualityUploadModel()
        if 'commodity_id' in d:
            o.commodity_id = d['commodity_id']
        if 'current_num' in d:
            o.current_num = d['current_num']
        if 'currentnum_update_time' in d:
            o.currentnum_update_time = d['currentnum_update_time']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'footpool_cl_qualified' in d:
            o.footpool_cl_qualified = d['footpool_cl_qualified']
        if 'footpool_cl_remain' in d:
            o.footpool_cl_remain = d['footpool_cl_remain']
        if 'footpool_cl_remain_standard' in d:
            o.footpool_cl_remain_standard = d['footpool_cl_remain_standard']
        if 'limit_num' in d:
            o.limit_num = d['limit_num']
        if 'mainpool_cl_qualified' in d:
            o.mainpool_cl_qualified = d['mainpool_cl_qualified']
        if 'mainpool_cl_remain' in d:
            o.mainpool_cl_remain = d['mainpool_cl_remain']
        if 'mainpool_cl_remain_standard' in d:
            o.mainpool_cl_remain_standard = d['mainpool_cl_remain_standard']
        if 'pool_volume' in d:
            o.pool_volume = d['pool_volume']
        if 'remark' in d:
            o.remark = d['remark']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'water_change' in d:
            o.water_change = d['water_change']
        if 'water_change_percent' in d:
            o.water_change_percent = d['water_change_percent']
        if 'water_change_qualified' in d:
            o.water_change_qualified = d['water_change_qualified']
        if 'water_change_standard' in d:
            o.water_change_standard = d['water_change_standard']
        if 'water_check_time' in d:
            o.water_check_time = d['water_check_time']
        if 'water_ph' in d:
            o.water_ph = d['water_ph']
        if 'water_ph_qualified' in d:
            o.water_ph_qualified = d['water_ph_qualified']
        if 'water_ph_standard' in d:
            o.water_ph_standard = d['water_ph_standard']
        if 'water_qualified' in d:
            o.water_qualified = d['water_qualified']
        if 'water_temperature' in d:
            o.water_temperature = d['water_temperature']
        if 'water_temperature_qualified' in d:
            o.water_temperature_qualified = d['water_temperature_qualified']
        if 'water_temperature_standard' in d:
            o.water_temperature_standard = d['water_temperature_standard']
        if 'water_update_time' in d:
            o.water_update_time = d['water_update_time']
        return o



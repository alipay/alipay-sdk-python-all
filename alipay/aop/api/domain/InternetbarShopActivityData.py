#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InternetbarShopActivityData(object):

    def __init__(self):
        self._active_device_count = None
        self._apply_device_count = None
        self._biz_date = None
        self._daily_active_device_count = None
        self._device_1_day_pv = None
        self._device_30_day_avg_pv = None
        self._device_30_day_uv = None
        self._device_dau = None
        self._last_30_day_active_device_count = None
        self._shop_code = None
        self._shop_id = None
        self._shop_name = None

    @property
    def active_device_count(self):
        return self._active_device_count

    @active_device_count.setter
    def active_device_count(self, value):
        self._active_device_count = value
    @property
    def apply_device_count(self):
        return self._apply_device_count

    @apply_device_count.setter
    def apply_device_count(self, value):
        self._apply_device_count = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def daily_active_device_count(self):
        return self._daily_active_device_count

    @daily_active_device_count.setter
    def daily_active_device_count(self, value):
        self._daily_active_device_count = value
    @property
    def device_1_day_pv(self):
        return self._device_1_day_pv

    @device_1_day_pv.setter
    def device_1_day_pv(self, value):
        self._device_1_day_pv = value
    @property
    def device_30_day_avg_pv(self):
        return self._device_30_day_avg_pv

    @device_30_day_avg_pv.setter
    def device_30_day_avg_pv(self, value):
        self._device_30_day_avg_pv = value
    @property
    def device_30_day_uv(self):
        return self._device_30_day_uv

    @device_30_day_uv.setter
    def device_30_day_uv(self, value):
        self._device_30_day_uv = value
    @property
    def device_dau(self):
        return self._device_dau

    @device_dau.setter
    def device_dau(self, value):
        self._device_dau = value
    @property
    def last_30_day_active_device_count(self):
        return self._last_30_day_active_device_count

    @last_30_day_active_device_count.setter
    def last_30_day_active_device_count(self, value):
        self._last_30_day_active_device_count = value
    @property
    def shop_code(self):
        return self._shop_code

    @shop_code.setter
    def shop_code(self, value):
        self._shop_code = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_device_count:
            if hasattr(self.active_device_count, 'to_alipay_dict'):
                params['active_device_count'] = self.active_device_count.to_alipay_dict()
            else:
                params['active_device_count'] = self.active_device_count
        if self.apply_device_count:
            if hasattr(self.apply_device_count, 'to_alipay_dict'):
                params['apply_device_count'] = self.apply_device_count.to_alipay_dict()
            else:
                params['apply_device_count'] = self.apply_device_count
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.daily_active_device_count:
            if hasattr(self.daily_active_device_count, 'to_alipay_dict'):
                params['daily_active_device_count'] = self.daily_active_device_count.to_alipay_dict()
            else:
                params['daily_active_device_count'] = self.daily_active_device_count
        if self.device_1_day_pv:
            if hasattr(self.device_1_day_pv, 'to_alipay_dict'):
                params['device_1_day_pv'] = self.device_1_day_pv.to_alipay_dict()
            else:
                params['device_1_day_pv'] = self.device_1_day_pv
        if self.device_30_day_avg_pv:
            if hasattr(self.device_30_day_avg_pv, 'to_alipay_dict'):
                params['device_30_day_avg_pv'] = self.device_30_day_avg_pv.to_alipay_dict()
            else:
                params['device_30_day_avg_pv'] = self.device_30_day_avg_pv
        if self.device_30_day_uv:
            if hasattr(self.device_30_day_uv, 'to_alipay_dict'):
                params['device_30_day_uv'] = self.device_30_day_uv.to_alipay_dict()
            else:
                params['device_30_day_uv'] = self.device_30_day_uv
        if self.device_dau:
            if hasattr(self.device_dau, 'to_alipay_dict'):
                params['device_dau'] = self.device_dau.to_alipay_dict()
            else:
                params['device_dau'] = self.device_dau
        if self.last_30_day_active_device_count:
            if hasattr(self.last_30_day_active_device_count, 'to_alipay_dict'):
                params['last_30_day_active_device_count'] = self.last_30_day_active_device_count.to_alipay_dict()
            else:
                params['last_30_day_active_device_count'] = self.last_30_day_active_device_count
        if self.shop_code:
            if hasattr(self.shop_code, 'to_alipay_dict'):
                params['shop_code'] = self.shop_code.to_alipay_dict()
            else:
                params['shop_code'] = self.shop_code
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InternetbarShopActivityData()
        if 'active_device_count' in d:
            o.active_device_count = d['active_device_count']
        if 'apply_device_count' in d:
            o.apply_device_count = d['apply_device_count']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'daily_active_device_count' in d:
            o.daily_active_device_count = d['daily_active_device_count']
        if 'device_1_day_pv' in d:
            o.device_1_day_pv = d['device_1_day_pv']
        if 'device_30_day_avg_pv' in d:
            o.device_30_day_avg_pv = d['device_30_day_avg_pv']
        if 'device_30_day_uv' in d:
            o.device_30_day_uv = d['device_30_day_uv']
        if 'device_dau' in d:
            o.device_dau = d['device_dau']
        if 'last_30_day_active_device_count' in d:
            o.last_30_day_active_device_count = d['last_30_day_active_device_count']
        if 'shop_code' in d:
            o.shop_code = d['shop_code']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        return o



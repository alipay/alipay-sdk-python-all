#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BroadcastReportItem(object):

    def __init__(self):
        self._biz_active_time = None
        self._biz_touch_active_time = None
        self._coop_mode = None
        self._device_sn = None
        self._first_marketing_broadcast = None
        self._is_have_jl_coil = None
        self._isv_pid = None
        self._last_bind_merchant_id = None
        self._monthly_marketing_count = None
        self._monthly_touch_tx_count_above_2 = None
        self._monthly_tx_count_above_2 = None
        self._supplier_id = None
        self._tag_id = None
        self._work_date_range = None

    @property
    def biz_active_time(self):
        return self._biz_active_time

    @biz_active_time.setter
    def biz_active_time(self, value):
        self._biz_active_time = value
    @property
    def biz_touch_active_time(self):
        return self._biz_touch_active_time

    @biz_touch_active_time.setter
    def biz_touch_active_time(self, value):
        self._biz_touch_active_time = value
    @property
    def coop_mode(self):
        return self._coop_mode

    @coop_mode.setter
    def coop_mode(self, value):
        self._coop_mode = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def first_marketing_broadcast(self):
        return self._first_marketing_broadcast

    @first_marketing_broadcast.setter
    def first_marketing_broadcast(self, value):
        self._first_marketing_broadcast = value
    @property
    def is_have_jl_coil(self):
        return self._is_have_jl_coil

    @is_have_jl_coil.setter
    def is_have_jl_coil(self, value):
        self._is_have_jl_coil = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def last_bind_merchant_id(self):
        return self._last_bind_merchant_id

    @last_bind_merchant_id.setter
    def last_bind_merchant_id(self, value):
        self._last_bind_merchant_id = value
    @property
    def monthly_marketing_count(self):
        return self._monthly_marketing_count

    @monthly_marketing_count.setter
    def monthly_marketing_count(self, value):
        self._monthly_marketing_count = value
    @property
    def monthly_touch_tx_count_above_2(self):
        return self._monthly_touch_tx_count_above_2

    @monthly_touch_tx_count_above_2.setter
    def monthly_touch_tx_count_above_2(self, value):
        self._monthly_touch_tx_count_above_2 = value
    @property
    def monthly_tx_count_above_2(self):
        return self._monthly_tx_count_above_2

    @monthly_tx_count_above_2.setter
    def monthly_tx_count_above_2(self, value):
        self._monthly_tx_count_above_2 = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value
    @property
    def work_date_range(self):
        return self._work_date_range

    @work_date_range.setter
    def work_date_range(self, value):
        self._work_date_range = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_active_time:
            if hasattr(self.biz_active_time, 'to_alipay_dict'):
                params['biz_active_time'] = self.biz_active_time.to_alipay_dict()
            else:
                params['biz_active_time'] = self.biz_active_time
        if self.biz_touch_active_time:
            if hasattr(self.biz_touch_active_time, 'to_alipay_dict'):
                params['biz_touch_active_time'] = self.biz_touch_active_time.to_alipay_dict()
            else:
                params['biz_touch_active_time'] = self.biz_touch_active_time
        if self.coop_mode:
            if hasattr(self.coop_mode, 'to_alipay_dict'):
                params['coop_mode'] = self.coop_mode.to_alipay_dict()
            else:
                params['coop_mode'] = self.coop_mode
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.first_marketing_broadcast:
            if hasattr(self.first_marketing_broadcast, 'to_alipay_dict'):
                params['first_marketing_broadcast'] = self.first_marketing_broadcast.to_alipay_dict()
            else:
                params['first_marketing_broadcast'] = self.first_marketing_broadcast
        if self.is_have_jl_coil:
            if hasattr(self.is_have_jl_coil, 'to_alipay_dict'):
                params['is_have_jl_coil'] = self.is_have_jl_coil.to_alipay_dict()
            else:
                params['is_have_jl_coil'] = self.is_have_jl_coil
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.last_bind_merchant_id:
            if hasattr(self.last_bind_merchant_id, 'to_alipay_dict'):
                params['last_bind_merchant_id'] = self.last_bind_merchant_id.to_alipay_dict()
            else:
                params['last_bind_merchant_id'] = self.last_bind_merchant_id
        if self.monthly_marketing_count:
            if hasattr(self.monthly_marketing_count, 'to_alipay_dict'):
                params['monthly_marketing_count'] = self.monthly_marketing_count.to_alipay_dict()
            else:
                params['monthly_marketing_count'] = self.monthly_marketing_count
        if self.monthly_touch_tx_count_above_2:
            if hasattr(self.monthly_touch_tx_count_above_2, 'to_alipay_dict'):
                params['monthly_touch_tx_count_above_2'] = self.monthly_touch_tx_count_above_2.to_alipay_dict()
            else:
                params['monthly_touch_tx_count_above_2'] = self.monthly_touch_tx_count_above_2
        if self.monthly_tx_count_above_2:
            if hasattr(self.monthly_tx_count_above_2, 'to_alipay_dict'):
                params['monthly_tx_count_above_2'] = self.monthly_tx_count_above_2.to_alipay_dict()
            else:
                params['monthly_tx_count_above_2'] = self.monthly_tx_count_above_2
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        if self.work_date_range:
            if hasattr(self.work_date_range, 'to_alipay_dict'):
                params['work_date_range'] = self.work_date_range.to_alipay_dict()
            else:
                params['work_date_range'] = self.work_date_range
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BroadcastReportItem()
        if 'biz_active_time' in d:
            o.biz_active_time = d['biz_active_time']
        if 'biz_touch_active_time' in d:
            o.biz_touch_active_time = d['biz_touch_active_time']
        if 'coop_mode' in d:
            o.coop_mode = d['coop_mode']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'first_marketing_broadcast' in d:
            o.first_marketing_broadcast = d['first_marketing_broadcast']
        if 'is_have_jl_coil' in d:
            o.is_have_jl_coil = d['is_have_jl_coil']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'last_bind_merchant_id' in d:
            o.last_bind_merchant_id = d['last_bind_merchant_id']
        if 'monthly_marketing_count' in d:
            o.monthly_marketing_count = d['monthly_marketing_count']
        if 'monthly_touch_tx_count_above_2' in d:
            o.monthly_touch_tx_count_above_2 = d['monthly_touch_tx_count_above_2']
        if 'monthly_tx_count_above_2' in d:
            o.monthly_tx_count_above_2 = d['monthly_tx_count_above_2']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        if 'work_date_range' in d:
            o.work_date_range = d['work_date_range']
        return o



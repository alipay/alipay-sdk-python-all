#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpeakerActivityItem(object):

    def __init__(self):
        self._biz_touch_active_time = None
        self._coop_mode = None
        self._device_sn = None
        self._first_bind_time = None
        self._last_bind_merchant_id = None
        self._supplier_id = None
        self._tag_id = None

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
    def first_bind_time(self):
        return self._first_bind_time

    @first_bind_time.setter
    def first_bind_time(self, value):
        self._first_bind_time = value
    @property
    def last_bind_merchant_id(self):
        return self._last_bind_merchant_id

    @last_bind_merchant_id.setter
    def last_bind_merchant_id(self, value):
        self._last_bind_merchant_id = value
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


    def to_alipay_dict(self):
        params = dict()
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
        if self.first_bind_time:
            if hasattr(self.first_bind_time, 'to_alipay_dict'):
                params['first_bind_time'] = self.first_bind_time.to_alipay_dict()
            else:
                params['first_bind_time'] = self.first_bind_time
        if self.last_bind_merchant_id:
            if hasattr(self.last_bind_merchant_id, 'to_alipay_dict'):
                params['last_bind_merchant_id'] = self.last_bind_merchant_id.to_alipay_dict()
            else:
                params['last_bind_merchant_id'] = self.last_bind_merchant_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpeakerActivityItem()
        if 'biz_touch_active_time' in d:
            o.biz_touch_active_time = d['biz_touch_active_time']
        if 'coop_mode' in d:
            o.coop_mode = d['coop_mode']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'first_bind_time' in d:
            o.first_bind_time = d['first_bind_time']
        if 'last_bind_merchant_id' in d:
            o.last_bind_merchant_id = d['last_bind_merchant_id']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        return o



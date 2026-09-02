#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderIndflowActionMaintainModel(object):

    def __init__(self):
        self._action_time = None
        self._action_type = None
        self._ad_pos_id = None
        self._mobile_phone = None
        self._supply_id = None

    @property
    def action_time(self):
        return self._action_time

    @action_time.setter
    def action_time(self, value):
        self._action_time = value
    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def ad_pos_id(self):
        return self._ad_pos_id

    @ad_pos_id.setter
    def ad_pos_id(self, value):
        self._ad_pos_id = value
    @property
    def mobile_phone(self):
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        self._mobile_phone = value
    @property
    def supply_id(self):
        return self._supply_id

    @supply_id.setter
    def supply_id(self, value):
        self._supply_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_time:
            if hasattr(self.action_time, 'to_alipay_dict'):
                params['action_time'] = self.action_time.to_alipay_dict()
            else:
                params['action_time'] = self.action_time
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.ad_pos_id:
            if hasattr(self.ad_pos_id, 'to_alipay_dict'):
                params['ad_pos_id'] = self.ad_pos_id.to_alipay_dict()
            else:
                params['ad_pos_id'] = self.ad_pos_id
        if self.mobile_phone:
            if hasattr(self.mobile_phone, 'to_alipay_dict'):
                params['mobile_phone'] = self.mobile_phone.to_alipay_dict()
            else:
                params['mobile_phone'] = self.mobile_phone
        if self.supply_id:
            if hasattr(self.supply_id, 'to_alipay_dict'):
                params['supply_id'] = self.supply_id.to_alipay_dict()
            else:
                params['supply_id'] = self.supply_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderIndflowActionMaintainModel()
        if 'action_time' in d:
            o.action_time = d['action_time']
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'ad_pos_id' in d:
            o.ad_pos_id = d['ad_pos_id']
        if 'mobile_phone' in d:
            o.mobile_phone = d['mobile_phone']
        if 'supply_id' in d:
            o.supply_id = d['supply_id']
        return o



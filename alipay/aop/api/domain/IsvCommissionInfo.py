#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommissionFirstRoleInfo import CommissionFirstRoleInfo
from alipay.aop.api.domain.ItemModeCommissionInfo import ItemModeCommissionInfo


class IsvCommissionInfo(object):

    def __init__(self):
        self._commission_first_role_list = None
        self._commission_invalid_time = None
        self._commission_mode = None
        self._commission_scene = None
        self._commission_valid_time = None
        self._isv_rate = None
        self._item_mode_commission_list = None
        self._long_term = None
        self._merchant_app_id = None

    @property
    def commission_first_role_list(self):
        return self._commission_first_role_list

    @commission_first_role_list.setter
    def commission_first_role_list(self, value):
        if isinstance(value, list):
            self._commission_first_role_list = list()
            for i in value:
                if isinstance(i, CommissionFirstRoleInfo):
                    self._commission_first_role_list.append(i)
                else:
                    self._commission_first_role_list.append(CommissionFirstRoleInfo.from_alipay_dict(i))
    @property
    def commission_invalid_time(self):
        return self._commission_invalid_time

    @commission_invalid_time.setter
    def commission_invalid_time(self, value):
        self._commission_invalid_time = value
    @property
    def commission_mode(self):
        return self._commission_mode

    @commission_mode.setter
    def commission_mode(self, value):
        self._commission_mode = value
    @property
    def commission_scene(self):
        return self._commission_scene

    @commission_scene.setter
    def commission_scene(self, value):
        self._commission_scene = value
    @property
    def commission_valid_time(self):
        return self._commission_valid_time

    @commission_valid_time.setter
    def commission_valid_time(self, value):
        self._commission_valid_time = value
    @property
    def isv_rate(self):
        return self._isv_rate

    @isv_rate.setter
    def isv_rate(self, value):
        self._isv_rate = value
    @property
    def item_mode_commission_list(self):
        return self._item_mode_commission_list

    @item_mode_commission_list.setter
    def item_mode_commission_list(self, value):
        if isinstance(value, list):
            self._item_mode_commission_list = list()
            for i in value:
                if isinstance(i, ItemModeCommissionInfo):
                    self._item_mode_commission_list.append(i)
                else:
                    self._item_mode_commission_list.append(ItemModeCommissionInfo.from_alipay_dict(i))
    @property
    def long_term(self):
        return self._long_term

    @long_term.setter
    def long_term(self, value):
        self._long_term = value
    @property
    def merchant_app_id(self):
        return self._merchant_app_id

    @merchant_app_id.setter
    def merchant_app_id(self, value):
        self._merchant_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.commission_first_role_list:
            if isinstance(self.commission_first_role_list, list):
                for i in range(0, len(self.commission_first_role_list)):
                    element = self.commission_first_role_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.commission_first_role_list[i] = element.to_alipay_dict()
            if hasattr(self.commission_first_role_list, 'to_alipay_dict'):
                params['commission_first_role_list'] = self.commission_first_role_list.to_alipay_dict()
            else:
                params['commission_first_role_list'] = self.commission_first_role_list
        if self.commission_invalid_time:
            if hasattr(self.commission_invalid_time, 'to_alipay_dict'):
                params['commission_invalid_time'] = self.commission_invalid_time.to_alipay_dict()
            else:
                params['commission_invalid_time'] = self.commission_invalid_time
        if self.commission_mode:
            if hasattr(self.commission_mode, 'to_alipay_dict'):
                params['commission_mode'] = self.commission_mode.to_alipay_dict()
            else:
                params['commission_mode'] = self.commission_mode
        if self.commission_scene:
            if hasattr(self.commission_scene, 'to_alipay_dict'):
                params['commission_scene'] = self.commission_scene.to_alipay_dict()
            else:
                params['commission_scene'] = self.commission_scene
        if self.commission_valid_time:
            if hasattr(self.commission_valid_time, 'to_alipay_dict'):
                params['commission_valid_time'] = self.commission_valid_time.to_alipay_dict()
            else:
                params['commission_valid_time'] = self.commission_valid_time
        if self.isv_rate:
            if hasattr(self.isv_rate, 'to_alipay_dict'):
                params['isv_rate'] = self.isv_rate.to_alipay_dict()
            else:
                params['isv_rate'] = self.isv_rate
        if self.item_mode_commission_list:
            if isinstance(self.item_mode_commission_list, list):
                for i in range(0, len(self.item_mode_commission_list)):
                    element = self.item_mode_commission_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_mode_commission_list[i] = element.to_alipay_dict()
            if hasattr(self.item_mode_commission_list, 'to_alipay_dict'):
                params['item_mode_commission_list'] = self.item_mode_commission_list.to_alipay_dict()
            else:
                params['item_mode_commission_list'] = self.item_mode_commission_list
        if self.long_term:
            if hasattr(self.long_term, 'to_alipay_dict'):
                params['long_term'] = self.long_term.to_alipay_dict()
            else:
                params['long_term'] = self.long_term
        if self.merchant_app_id:
            if hasattr(self.merchant_app_id, 'to_alipay_dict'):
                params['merchant_app_id'] = self.merchant_app_id.to_alipay_dict()
            else:
                params['merchant_app_id'] = self.merchant_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IsvCommissionInfo()
        if 'commission_first_role_list' in d:
            o.commission_first_role_list = d['commission_first_role_list']
        if 'commission_invalid_time' in d:
            o.commission_invalid_time = d['commission_invalid_time']
        if 'commission_mode' in d:
            o.commission_mode = d['commission_mode']
        if 'commission_scene' in d:
            o.commission_scene = d['commission_scene']
        if 'commission_valid_time' in d:
            o.commission_valid_time = d['commission_valid_time']
        if 'isv_rate' in d:
            o.isv_rate = d['isv_rate']
        if 'item_mode_commission_list' in d:
            o.item_mode_commission_list = d['item_mode_commission_list']
        if 'long_term' in d:
            o.long_term = d['long_term']
        if 'merchant_app_id' in d:
            o.merchant_app_id = d['merchant_app_id']
        return o



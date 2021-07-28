#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NormalBusinessTimeRule import NormalBusinessTimeRule
from alipay.aop.api.domain.SpecialBusinessTimeRule import SpecialBusinessTimeRule
from alipay.aop.api.domain.PreOrderConfigInfo import PreOrderConfigInfo


class ShopOrderConfigInfo(object):

    def __init__(self):
        self._ext_infos = None
        self._order_entry_status = None
        self._order_normal_business_time = None
        self._order_special_business_time = None
        self._order_status = None
        self._pre_order_config = None
        self._shop_id = None
        self._store_id = None

    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def order_entry_status(self):
        return self._order_entry_status

    @order_entry_status.setter
    def order_entry_status(self, value):
        self._order_entry_status = value
    @property
    def order_normal_business_time(self):
        return self._order_normal_business_time

    @order_normal_business_time.setter
    def order_normal_business_time(self, value):
        if isinstance(value, list):
            self._order_normal_business_time = list()
            for i in value:
                if isinstance(i, NormalBusinessTimeRule):
                    self._order_normal_business_time.append(i)
                else:
                    self._order_normal_business_time.append(NormalBusinessTimeRule.from_alipay_dict(i))
    @property
    def order_special_business_time(self):
        return self._order_special_business_time

    @order_special_business_time.setter
    def order_special_business_time(self, value):
        if isinstance(value, list):
            self._order_special_business_time = list()
            for i in value:
                if isinstance(i, SpecialBusinessTimeRule):
                    self._order_special_business_time.append(i)
                else:
                    self._order_special_business_time.append(SpecialBusinessTimeRule.from_alipay_dict(i))
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def pre_order_config(self):
        return self._pre_order_config

    @pre_order_config.setter
    def pre_order_config(self, value):
        if isinstance(value, PreOrderConfigInfo):
            self._pre_order_config = value
        else:
            self._pre_order_config = PreOrderConfigInfo.from_alipay_dict(value)
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.order_entry_status:
            if hasattr(self.order_entry_status, 'to_alipay_dict'):
                params['order_entry_status'] = self.order_entry_status.to_alipay_dict()
            else:
                params['order_entry_status'] = self.order_entry_status
        if self.order_normal_business_time:
            if isinstance(self.order_normal_business_time, list):
                for i in range(0, len(self.order_normal_business_time)):
                    element = self.order_normal_business_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_normal_business_time[i] = element.to_alipay_dict()
            if hasattr(self.order_normal_business_time, 'to_alipay_dict'):
                params['order_normal_business_time'] = self.order_normal_business_time.to_alipay_dict()
            else:
                params['order_normal_business_time'] = self.order_normal_business_time
        if self.order_special_business_time:
            if isinstance(self.order_special_business_time, list):
                for i in range(0, len(self.order_special_business_time)):
                    element = self.order_special_business_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_special_business_time[i] = element.to_alipay_dict()
            if hasattr(self.order_special_business_time, 'to_alipay_dict'):
                params['order_special_business_time'] = self.order_special_business_time.to_alipay_dict()
            else:
                params['order_special_business_time'] = self.order_special_business_time
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.pre_order_config:
            if hasattr(self.pre_order_config, 'to_alipay_dict'):
                params['pre_order_config'] = self.pre_order_config.to_alipay_dict()
            else:
                params['pre_order_config'] = self.pre_order_config
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopOrderConfigInfo()
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'order_entry_status' in d:
            o.order_entry_status = d['order_entry_status']
        if 'order_normal_business_time' in d:
            o.order_normal_business_time = d['order_normal_business_time']
        if 'order_special_business_time' in d:
            o.order_special_business_time = d['order_special_business_time']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'pre_order_config' in d:
            o.pre_order_config = d['pre_order_config']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o



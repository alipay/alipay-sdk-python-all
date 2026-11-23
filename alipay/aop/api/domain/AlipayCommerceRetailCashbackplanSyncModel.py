#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRetailCashbackplanSyncModel(object):

    def __init__(self):
        self._base_info = None
        self._delivery_plan_id = None
        self._fund_config = None
        self._operate_type = None
        self._out_biz_id = None

    @property
    def base_info(self):
        return self._base_info

    @base_info.setter
    def base_info(self, value):
        self._base_info = value
    @property
    def delivery_plan_id(self):
        return self._delivery_plan_id

    @delivery_plan_id.setter
    def delivery_plan_id(self, value):
        self._delivery_plan_id = value
    @property
    def fund_config(self):
        return self._fund_config

    @fund_config.setter
    def fund_config(self, value):
        self._fund_config = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_info:
            if hasattr(self.base_info, 'to_alipay_dict'):
                params['base_info'] = self.base_info.to_alipay_dict()
            else:
                params['base_info'] = self.base_info
        if self.delivery_plan_id:
            if hasattr(self.delivery_plan_id, 'to_alipay_dict'):
                params['delivery_plan_id'] = self.delivery_plan_id.to_alipay_dict()
            else:
                params['delivery_plan_id'] = self.delivery_plan_id
        if self.fund_config:
            if hasattr(self.fund_config, 'to_alipay_dict'):
                params['fund_config'] = self.fund_config.to_alipay_dict()
            else:
                params['fund_config'] = self.fund_config
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRetailCashbackplanSyncModel()
        if 'base_info' in d:
            o.base_info = d['base_info']
        if 'delivery_plan_id' in d:
            o.delivery_plan_id = d['delivery_plan_id']
        if 'fund_config' in d:
            o.fund_config = d['fund_config']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        return o



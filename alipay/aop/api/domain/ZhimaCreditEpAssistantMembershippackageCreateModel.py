#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpAssistantProductConfig import EpAssistantProductConfig


class ZhimaCreditEpAssistantMembershippackageCreateModel(object):

    def __init__(self):
        self._begin_effect_time = None
        self._company_id = None
        self._company_name = None
        self._has_activity = None
        self._order_no = None
        self._out_biz_no = None
        self._product_code = None
        self._product_config = None
        self._product_sku = None

    @property
    def begin_effect_time(self):
        return self._begin_effect_time

    @begin_effect_time.setter
    def begin_effect_time(self, value):
        self._begin_effect_time = value
    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def has_activity(self):
        return self._has_activity

    @has_activity.setter
    def has_activity(self, value):
        self._has_activity = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_config(self):
        return self._product_config

    @product_config.setter
    def product_config(self, value):
        if isinstance(value, EpAssistantProductConfig):
            self._product_config = value
        else:
            self._product_config = EpAssistantProductConfig.from_alipay_dict(value)
    @property
    def product_sku(self):
        return self._product_sku

    @product_sku.setter
    def product_sku(self, value):
        self._product_sku = value


    def to_alipay_dict(self):
        params = dict()
        if self.begin_effect_time:
            if hasattr(self.begin_effect_time, 'to_alipay_dict'):
                params['begin_effect_time'] = self.begin_effect_time.to_alipay_dict()
            else:
                params['begin_effect_time'] = self.begin_effect_time
        if self.company_id:
            if hasattr(self.company_id, 'to_alipay_dict'):
                params['company_id'] = self.company_id.to_alipay_dict()
            else:
                params['company_id'] = self.company_id
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.has_activity:
            if hasattr(self.has_activity, 'to_alipay_dict'):
                params['has_activity'] = self.has_activity.to_alipay_dict()
            else:
                params['has_activity'] = self.has_activity
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_config:
            if hasattr(self.product_config, 'to_alipay_dict'):
                params['product_config'] = self.product_config.to_alipay_dict()
            else:
                params['product_config'] = self.product_config
        if self.product_sku:
            if hasattr(self.product_sku, 'to_alipay_dict'):
                params['product_sku'] = self.product_sku.to_alipay_dict()
            else:
                params['product_sku'] = self.product_sku
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAssistantMembershippackageCreateModel()
        if 'begin_effect_time' in d:
            o.begin_effect_time = d['begin_effect_time']
        if 'company_id' in d:
            o.company_id = d['company_id']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'has_activity' in d:
            o.has_activity = d['has_activity']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_config' in d:
            o.product_config = d['product_config']
        if 'product_sku' in d:
            o.product_sku = d['product_sku']
        return o



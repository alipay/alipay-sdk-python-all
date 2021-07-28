#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInstserviceOrderCreateModel(object):

    def __init__(self):
        self._bill_key = None
        self._biz_type = None
        self._extend = None
        self._flow_id = None
        self._flow_time = None
        self._inst = None
        self._operation = None
        self._partner_name = None
        self._product_id = None
        self._sub_biz_type = None
        self._user_id = None

    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def extend(self):
        return self._extend

    @extend.setter
    def extend(self, value):
        self._extend = value
    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def flow_time(self):
        return self._flow_time

    @flow_time.setter
    def flow_time(self, value):
        self._flow_time = value
    @property
    def inst(self):
        return self._inst

    @inst.setter
    def inst(self, value):
        self._inst = value
    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value
    @property
    def partner_name(self):
        return self._partner_name

    @partner_name.setter
    def partner_name(self, value):
        self._partner_name = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = self.bill_key.to_alipay_dict()
            else:
                params['bill_key'] = self.bill_key
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.extend:
            if hasattr(self.extend, 'to_alipay_dict'):
                params['extend'] = self.extend.to_alipay_dict()
            else:
                params['extend'] = self.extend
        if self.flow_id:
            if hasattr(self.flow_id, 'to_alipay_dict'):
                params['flow_id'] = self.flow_id.to_alipay_dict()
            else:
                params['flow_id'] = self.flow_id
        if self.flow_time:
            if hasattr(self.flow_time, 'to_alipay_dict'):
                params['flow_time'] = self.flow_time.to_alipay_dict()
            else:
                params['flow_time'] = self.flow_time
        if self.inst:
            if hasattr(self.inst, 'to_alipay_dict'):
                params['inst'] = self.inst.to_alipay_dict()
            else:
                params['inst'] = self.inst
        if self.operation:
            if hasattr(self.operation, 'to_alipay_dict'):
                params['operation'] = self.operation.to_alipay_dict()
            else:
                params['operation'] = self.operation
        if self.partner_name:
            if hasattr(self.partner_name, 'to_alipay_dict'):
                params['partner_name'] = self.partner_name.to_alipay_dict()
            else:
                params['partner_name'] = self.partner_name
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
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
        o = AlipayEbppInstserviceOrderCreateModel()
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'extend' in d:
            o.extend = d['extend']
        if 'flow_id' in d:
            o.flow_id = d['flow_id']
        if 'flow_time' in d:
            o.flow_time = d['flow_time']
        if 'inst' in d:
            o.inst = d['inst']
        if 'operation' in d:
            o.operation = d['operation']
        if 'partner_name' in d:
            o.partner_name = d['partner_name']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



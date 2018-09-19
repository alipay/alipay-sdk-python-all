#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryOrderProcessVO(object):

    def __init__(self):
        self._gmt_create = None
        self._gmt_modified = None
        self._operate_info = None
        self._operate_time = None
        self._operator_code = None
        self._operator_name = None
        self._order_code = None
        self._order_id = None
        self._order_type = None
        self._process_status = None
        self._remark = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def operate_info(self):
        return self._operate_info

    @operate_info.setter
    def operate_info(self, value):
        self._operate_info = value
    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
    @property
    def operator_code(self):
        return self._operator_code

    @operator_code.setter
    def operator_code(self, value):
        self._operator_code = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def order_code(self):
        return self._order_code

    @order_code.setter
    def order_code(self, value):
        self._order_code = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def process_status(self):
        return self._process_status

    @process_status.setter
    def process_status(self, value):
        self._process_status = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.operate_info:
            if hasattr(self.operate_info, 'to_alipay_dict'):
                params['operate_info'] = self.operate_info.to_alipay_dict()
            else:
                params['operate_info'] = self.operate_info
        if self.operate_time:
            if hasattr(self.operate_time, 'to_alipay_dict'):
                params['operate_time'] = self.operate_time.to_alipay_dict()
            else:
                params['operate_time'] = self.operate_time
        if self.operator_code:
            if hasattr(self.operator_code, 'to_alipay_dict'):
                params['operator_code'] = self.operator_code.to_alipay_dict()
            else:
                params['operator_code'] = self.operator_code
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
        if self.order_code:
            if hasattr(self.order_code, 'to_alipay_dict'):
                params['order_code'] = self.order_code.to_alipay_dict()
            else:
                params['order_code'] = self.order_code
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.process_status:
            if hasattr(self.process_status, 'to_alipay_dict'):
                params['process_status'] = self.process_status.to_alipay_dict()
            else:
                params['process_status'] = self.process_status
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryOrderProcessVO()
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'operate_info' in d:
            o.operate_info = d['operate_info']
        if 'operate_time' in d:
            o.operate_time = d['operate_time']
        if 'operator_code' in d:
            o.operator_code = d['operator_code']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'order_code' in d:
            o.order_code = d['order_code']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'process_status' in d:
            o.process_status = d['process_status']
        if 'remark' in d:
            o.remark = d['remark']
        return o



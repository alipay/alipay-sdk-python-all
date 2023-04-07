#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BelongMerchantInfo import BelongMerchantInfo


class ActivityBaseInfo(object):

    def __init__(self):
        self._activity_id = None
        self._activity_name = None
        self._activity_operation_status = None
        self._activity_product_type = None
        self._activity_status = None
        self._belong_merchant_info = None
        self._code_mode = None
        self._out_activity_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_operation_status(self):
        return self._activity_operation_status

    @activity_operation_status.setter
    def activity_operation_status(self, value):
        self._activity_operation_status = value
    @property
    def activity_product_type(self):
        return self._activity_product_type

    @activity_product_type.setter
    def activity_product_type(self, value):
        self._activity_product_type = value
    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def belong_merchant_info(self):
        return self._belong_merchant_info

    @belong_merchant_info.setter
    def belong_merchant_info(self, value):
        if isinstance(value, BelongMerchantInfo):
            self._belong_merchant_info = value
        else:
            self._belong_merchant_info = BelongMerchantInfo.from_alipay_dict(value)
    @property
    def code_mode(self):
        return self._code_mode

    @code_mode.setter
    def code_mode(self, value):
        self._code_mode = value
    @property
    def out_activity_id(self):
        return self._out_activity_id

    @out_activity_id.setter
    def out_activity_id(self, value):
        self._out_activity_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.activity_operation_status:
            if hasattr(self.activity_operation_status, 'to_alipay_dict'):
                params['activity_operation_status'] = self.activity_operation_status.to_alipay_dict()
            else:
                params['activity_operation_status'] = self.activity_operation_status
        if self.activity_product_type:
            if hasattr(self.activity_product_type, 'to_alipay_dict'):
                params['activity_product_type'] = self.activity_product_type.to_alipay_dict()
            else:
                params['activity_product_type'] = self.activity_product_type
        if self.activity_status:
            if hasattr(self.activity_status, 'to_alipay_dict'):
                params['activity_status'] = self.activity_status.to_alipay_dict()
            else:
                params['activity_status'] = self.activity_status
        if self.belong_merchant_info:
            if hasattr(self.belong_merchant_info, 'to_alipay_dict'):
                params['belong_merchant_info'] = self.belong_merchant_info.to_alipay_dict()
            else:
                params['belong_merchant_info'] = self.belong_merchant_info
        if self.code_mode:
            if hasattr(self.code_mode, 'to_alipay_dict'):
                params['code_mode'] = self.code_mode.to_alipay_dict()
            else:
                params['code_mode'] = self.code_mode
        if self.out_activity_id:
            if hasattr(self.out_activity_id, 'to_alipay_dict'):
                params['out_activity_id'] = self.out_activity_id.to_alipay_dict()
            else:
                params['out_activity_id'] = self.out_activity_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityBaseInfo()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_operation_status' in d:
            o.activity_operation_status = d['activity_operation_status']
        if 'activity_product_type' in d:
            o.activity_product_type = d['activity_product_type']
        if 'activity_status' in d:
            o.activity_status = d['activity_status']
        if 'belong_merchant_info' in d:
            o.belong_merchant_info = d['belong_merchant_info']
        if 'code_mode' in d:
            o.code_mode = d['code_mode']
        if 'out_activity_id' in d:
            o.out_activity_id = d['out_activity_id']
        return o



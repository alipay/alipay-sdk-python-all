#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiPcreditmerchantProductorderCancelModel(object):

    def __init__(self):
        self._biz_from = None
        self._cancel_system_code = None
        self._cancel_type = None
        self._extending_info = None
        self._from_app = None
        self._memo = None
        self._order_id = None
        self._pid = None

    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def cancel_system_code(self):
        return self._cancel_system_code

    @cancel_system_code.setter
    def cancel_system_code(self, value):
        self._cancel_system_code = value
    @property
    def cancel_type(self):
        return self._cancel_type

    @cancel_type.setter
    def cancel_type(self, value):
        self._cancel_type = value
    @property
    def extending_info(self):
        return self._extending_info

    @extending_info.setter
    def extending_info(self, value):
        self._extending_info = value
    @property
    def from_app(self):
        return self._from_app

    @from_app.setter
    def from_app(self, value):
        self._from_app = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
        if self.cancel_system_code:
            if hasattr(self.cancel_system_code, 'to_alipay_dict'):
                params['cancel_system_code'] = self.cancel_system_code.to_alipay_dict()
            else:
                params['cancel_system_code'] = self.cancel_system_code
        if self.cancel_type:
            if hasattr(self.cancel_type, 'to_alipay_dict'):
                params['cancel_type'] = self.cancel_type.to_alipay_dict()
            else:
                params['cancel_type'] = self.cancel_type
        if self.extending_info:
            if hasattr(self.extending_info, 'to_alipay_dict'):
                params['extending_info'] = self.extending_info.to_alipay_dict()
            else:
                params['extending_info'] = self.extending_info
        if self.from_app:
            if hasattr(self.from_app, 'to_alipay_dict'):
                params['from_app'] = self.from_app.to_alipay_dict()
            else:
                params['from_app'] = self.from_app
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiPcreditmerchantProductorderCancelModel()
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'cancel_system_code' in d:
            o.cancel_system_code = d['cancel_system_code']
        if 'cancel_type' in d:
            o.cancel_type = d['cancel_type']
        if 'extending_info' in d:
            o.extending_info = d['extending_info']
        if 'from_app' in d:
            o.from_app = d['from_app']
        if 'memo' in d:
            o.memo = d['memo']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'pid' in d:
            o.pid = d['pid']
        return o



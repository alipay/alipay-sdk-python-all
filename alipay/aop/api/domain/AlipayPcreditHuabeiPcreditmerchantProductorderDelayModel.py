#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiPcreditmerchantProductorderDelayModel(object):

    def __init__(self):
        self._extending_info = None
        self._from_app = None
        self._order_id = None
        self._pid = None
        self._renew_system_code = None
        self._renewing_datetime = None

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
    @property
    def renew_system_code(self):
        return self._renew_system_code

    @renew_system_code.setter
    def renew_system_code(self, value):
        self._renew_system_code = value
    @property
    def renewing_datetime(self):
        return self._renewing_datetime

    @renewing_datetime.setter
    def renewing_datetime(self, value):
        self._renewing_datetime = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.renew_system_code:
            if hasattr(self.renew_system_code, 'to_alipay_dict'):
                params['renew_system_code'] = self.renew_system_code.to_alipay_dict()
            else:
                params['renew_system_code'] = self.renew_system_code
        if self.renewing_datetime:
            if hasattr(self.renewing_datetime, 'to_alipay_dict'):
                params['renewing_datetime'] = self.renewing_datetime.to_alipay_dict()
            else:
                params['renewing_datetime'] = self.renewing_datetime
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiPcreditmerchantProductorderDelayModel()
        if 'extending_info' in d:
            o.extending_info = d['extending_info']
        if 'from_app' in d:
            o.from_app = d['from_app']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'renew_system_code' in d:
            o.renew_system_code = d['renew_system_code']
        if 'renewing_datetime' in d:
            o.renewing_datetime = d['renewing_datetime']
        return o



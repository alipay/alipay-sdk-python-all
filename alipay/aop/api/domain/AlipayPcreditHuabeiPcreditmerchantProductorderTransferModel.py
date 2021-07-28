#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiPcreditmerchantProductorderTransferModel(object):

    def __init__(self):
        self._active_datetime = None
        self._extending_info = None
        self._from_app = None
        self._inactive_datetime = None
        self._inactiving_datetime = None
        self._ordered_channel = None
        self._ordered_system_code = None
        self._ordering_datetime = None
        self._out_merchant_id = None
        self._pid = None
        self._ps_code = None
        self._renew = None
        self._taobao_order_id = None

    @property
    def active_datetime(self):
        return self._active_datetime

    @active_datetime.setter
    def active_datetime(self, value):
        self._active_datetime = value
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
    def inactive_datetime(self):
        return self._inactive_datetime

    @inactive_datetime.setter
    def inactive_datetime(self, value):
        self._inactive_datetime = value
    @property
    def inactiving_datetime(self):
        return self._inactiving_datetime

    @inactiving_datetime.setter
    def inactiving_datetime(self, value):
        self._inactiving_datetime = value
    @property
    def ordered_channel(self):
        return self._ordered_channel

    @ordered_channel.setter
    def ordered_channel(self, value):
        self._ordered_channel = value
    @property
    def ordered_system_code(self):
        return self._ordered_system_code

    @ordered_system_code.setter
    def ordered_system_code(self, value):
        self._ordered_system_code = value
    @property
    def ordering_datetime(self):
        return self._ordering_datetime

    @ordering_datetime.setter
    def ordering_datetime(self, value):
        self._ordering_datetime = value
    @property
    def out_merchant_id(self):
        return self._out_merchant_id

    @out_merchant_id.setter
    def out_merchant_id(self, value):
        self._out_merchant_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def ps_code(self):
        return self._ps_code

    @ps_code.setter
    def ps_code(self, value):
        self._ps_code = value
    @property
    def renew(self):
        return self._renew

    @renew.setter
    def renew(self, value):
        self._renew = value
    @property
    def taobao_order_id(self):
        return self._taobao_order_id

    @taobao_order_id.setter
    def taobao_order_id(self, value):
        self._taobao_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_datetime:
            if hasattr(self.active_datetime, 'to_alipay_dict'):
                params['active_datetime'] = self.active_datetime.to_alipay_dict()
            else:
                params['active_datetime'] = self.active_datetime
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
        if self.inactive_datetime:
            if hasattr(self.inactive_datetime, 'to_alipay_dict'):
                params['inactive_datetime'] = self.inactive_datetime.to_alipay_dict()
            else:
                params['inactive_datetime'] = self.inactive_datetime
        if self.inactiving_datetime:
            if hasattr(self.inactiving_datetime, 'to_alipay_dict'):
                params['inactiving_datetime'] = self.inactiving_datetime.to_alipay_dict()
            else:
                params['inactiving_datetime'] = self.inactiving_datetime
        if self.ordered_channel:
            if hasattr(self.ordered_channel, 'to_alipay_dict'):
                params['ordered_channel'] = self.ordered_channel.to_alipay_dict()
            else:
                params['ordered_channel'] = self.ordered_channel
        if self.ordered_system_code:
            if hasattr(self.ordered_system_code, 'to_alipay_dict'):
                params['ordered_system_code'] = self.ordered_system_code.to_alipay_dict()
            else:
                params['ordered_system_code'] = self.ordered_system_code
        if self.ordering_datetime:
            if hasattr(self.ordering_datetime, 'to_alipay_dict'):
                params['ordering_datetime'] = self.ordering_datetime.to_alipay_dict()
            else:
                params['ordering_datetime'] = self.ordering_datetime
        if self.out_merchant_id:
            if hasattr(self.out_merchant_id, 'to_alipay_dict'):
                params['out_merchant_id'] = self.out_merchant_id.to_alipay_dict()
            else:
                params['out_merchant_id'] = self.out_merchant_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.ps_code:
            if hasattr(self.ps_code, 'to_alipay_dict'):
                params['ps_code'] = self.ps_code.to_alipay_dict()
            else:
                params['ps_code'] = self.ps_code
        if self.renew:
            if hasattr(self.renew, 'to_alipay_dict'):
                params['renew'] = self.renew.to_alipay_dict()
            else:
                params['renew'] = self.renew
        if self.taobao_order_id:
            if hasattr(self.taobao_order_id, 'to_alipay_dict'):
                params['taobao_order_id'] = self.taobao_order_id.to_alipay_dict()
            else:
                params['taobao_order_id'] = self.taobao_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiPcreditmerchantProductorderTransferModel()
        if 'active_datetime' in d:
            o.active_datetime = d['active_datetime']
        if 'extending_info' in d:
            o.extending_info = d['extending_info']
        if 'from_app' in d:
            o.from_app = d['from_app']
        if 'inactive_datetime' in d:
            o.inactive_datetime = d['inactive_datetime']
        if 'inactiving_datetime' in d:
            o.inactiving_datetime = d['inactiving_datetime']
        if 'ordered_channel' in d:
            o.ordered_channel = d['ordered_channel']
        if 'ordered_system_code' in d:
            o.ordered_system_code = d['ordered_system_code']
        if 'ordering_datetime' in d:
            o.ordering_datetime = d['ordering_datetime']
        if 'out_merchant_id' in d:
            o.out_merchant_id = d['out_merchant_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'ps_code' in d:
            o.ps_code = d['ps_code']
        if 'renew' in d:
            o.renew = d['renew']
        if 'taobao_order_id' in d:
            o.taobao_order_id = d['taobao_order_id']
        return o



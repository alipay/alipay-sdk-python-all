#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiPcreditmerchantProductorderApplyModel(object):

    def __init__(self):
        self._active_datetime = None
        self._activity_id = None
        self._biz_from = None
        self._extending_info = None
        self._from_app = None
        self._ordered_channel = None
        self._ordered_system_code = None
        self._ordering_datetime = None
        self._pid = None
        self._ps_code = None

    @property
    def active_datetime(self):
        return self._active_datetime

    @active_datetime.setter
    def active_datetime(self, value):
        self._active_datetime = value
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.active_datetime:
            if hasattr(self.active_datetime, 'to_alipay_dict'):
                params['active_datetime'] = self.active_datetime.to_alipay_dict()
            else:
                params['active_datetime'] = self.active_datetime
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiPcreditmerchantProductorderApplyModel()
        if 'active_datetime' in d:
            o.active_datetime = d['active_datetime']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'extending_info' in d:
            o.extending_info = d['extending_info']
        if 'from_app' in d:
            o.from_app = d['from_app']
        if 'ordered_channel' in d:
            o.ordered_channel = d['ordered_channel']
        if 'ordered_system_code' in d:
            o.ordered_system_code = d['ordered_system_code']
        if 'ordering_datetime' in d:
            o.ordering_datetime = d['ordering_datetime']
        if 'pid' in d:
            o.pid = d['pid']
        if 'ps_code' in d:
            o.ps_code = d['ps_code']
        return o



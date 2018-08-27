#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppCommonNotifySendModel(object):

    def __init__(self):
        self._bill_key = None
        self._biz_type = None
        self._charge_inst = None
        self._extend_data = None
        self._notify_type = None
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
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def extend_data(self):
        return self._extend_data

    @extend_data.setter
    def extend_data(self, value):
        self._extend_data = value
    @property
    def notify_type(self):
        return self._notify_type

    @notify_type.setter
    def notify_type(self, value):
        self._notify_type = value
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
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.extend_data:
            if hasattr(self.extend_data, 'to_alipay_dict'):
                params['extend_data'] = self.extend_data.to_alipay_dict()
            else:
                params['extend_data'] = self.extend_data
        if self.notify_type:
            if hasattr(self.notify_type, 'to_alipay_dict'):
                params['notify_type'] = self.notify_type.to_alipay_dict()
            else:
                params['notify_type'] = self.notify_type
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
        o = AlipayEbppCommonNotifySendModel()
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'extend_data' in d:
            o.extend_data = d['extend_data']
        if 'notify_type' in d:
            o.notify_type = d['notify_type']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



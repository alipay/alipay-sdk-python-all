#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsWaybillOperationConfirmModel(object):

    def __init__(self):
        self._channel = None
        self._channel_waybill_operation_scope = None
        self._lbx = None
        self._logistics_code = None
        self._open_id = None
        self._operation_type = None
        self._outbiz_order_id = None
        self._user_id = None
        self._waybill_no = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def channel_waybill_operation_scope(self):
        return self._channel_waybill_operation_scope

    @channel_waybill_operation_scope.setter
    def channel_waybill_operation_scope(self, value):
        self._channel_waybill_operation_scope = value
    @property
    def lbx(self):
        return self._lbx

    @lbx.setter
    def lbx(self, value):
        self._lbx = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def outbiz_order_id(self):
        return self._outbiz_order_id

    @outbiz_order_id.setter
    def outbiz_order_id(self, value):
        self._outbiz_order_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.channel_waybill_operation_scope:
            if hasattr(self.channel_waybill_operation_scope, 'to_alipay_dict'):
                params['channel_waybill_operation_scope'] = self.channel_waybill_operation_scope.to_alipay_dict()
            else:
                params['channel_waybill_operation_scope'] = self.channel_waybill_operation_scope
        if self.lbx:
            if hasattr(self.lbx, 'to_alipay_dict'):
                params['lbx'] = self.lbx.to_alipay_dict()
            else:
                params['lbx'] = self.lbx
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.outbiz_order_id:
            if hasattr(self.outbiz_order_id, 'to_alipay_dict'):
                params['outbiz_order_id'] = self.outbiz_order_id.to_alipay_dict()
            else:
                params['outbiz_order_id'] = self.outbiz_order_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.waybill_no:
            if hasattr(self.waybill_no, 'to_alipay_dict'):
                params['waybill_no'] = self.waybill_no.to_alipay_dict()
            else:
                params['waybill_no'] = self.waybill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsWaybillOperationConfirmModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'channel_waybill_operation_scope' in d:
            o.channel_waybill_operation_scope = d['channel_waybill_operation_scope']
        if 'lbx' in d:
            o.lbx = d['lbx']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'outbiz_order_id' in d:
            o.outbiz_order_id = d['outbiz_order_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        return o



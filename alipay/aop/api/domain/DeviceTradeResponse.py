#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceTradeResponse(object):

    def __init__(self):
        self._biz_tid = None
        self._device_sn = None
        self._iot_trade_error_type = None
        self._item_id = None
        self._terminal_sdk_sign_info = None
        self._trade_finish_time = None
        self._trade_no = None

    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def iot_trade_error_type(self):
        return self._iot_trade_error_type

    @iot_trade_error_type.setter
    def iot_trade_error_type(self, value):
        self._iot_trade_error_type = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def terminal_sdk_sign_info(self):
        return self._terminal_sdk_sign_info

    @terminal_sdk_sign_info.setter
    def terminal_sdk_sign_info(self, value):
        self._terminal_sdk_sign_info = value
    @property
    def trade_finish_time(self):
        return self._trade_finish_time

    @trade_finish_time.setter
    def trade_finish_time(self, value):
        self._trade_finish_time = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.iot_trade_error_type:
            if hasattr(self.iot_trade_error_type, 'to_alipay_dict'):
                params['iot_trade_error_type'] = self.iot_trade_error_type.to_alipay_dict()
            else:
                params['iot_trade_error_type'] = self.iot_trade_error_type
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.terminal_sdk_sign_info:
            if hasattr(self.terminal_sdk_sign_info, 'to_alipay_dict'):
                params['terminal_sdk_sign_info'] = self.terminal_sdk_sign_info.to_alipay_dict()
            else:
                params['terminal_sdk_sign_info'] = self.terminal_sdk_sign_info
        if self.trade_finish_time:
            if hasattr(self.trade_finish_time, 'to_alipay_dict'):
                params['trade_finish_time'] = self.trade_finish_time.to_alipay_dict()
            else:
                params['trade_finish_time'] = self.trade_finish_time
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceTradeResponse()
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'iot_trade_error_type' in d:
            o.iot_trade_error_type = d['iot_trade_error_type']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'terminal_sdk_sign_info' in d:
            o.terminal_sdk_sign_info = d['terminal_sdk_sign_info']
        if 'trade_finish_time' in d:
            o.trade_finish_time = d['trade_finish_time']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o



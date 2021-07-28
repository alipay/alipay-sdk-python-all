#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceTradeInfoList(object):

    def __init__(self):
        self._biz_tid = None
        self._dau = None
        self._device_face_trade_dau = None
        self._device_face_trade_dau_d_value = None
        self._device_name = None
        self._device_sn = None
        self._device_status = None
        self._face_trade_cnt = None
        self._face_trd_amt = None
        self._face_trd_cnt_rate = None
        self._face_trd_user_cnt_rate = None
        self._face_trd_user_cnt_rate_d_value = None
        self._gmt_active = None
        self._iot_trd_up = None
        self._iot_trd_user_cnt = None
        self._iot_trd_user_cnt_d_value = None
        self._max_dt = None
        self._merchant_pid = None
        self._shop_id = None
        self._trade_amt = None
        self._trade_cnt = None

    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def dau(self):
        return self._dau

    @dau.setter
    def dau(self, value):
        self._dau = value
    @property
    def device_face_trade_dau(self):
        return self._device_face_trade_dau

    @device_face_trade_dau.setter
    def device_face_trade_dau(self, value):
        self._device_face_trade_dau = value
    @property
    def device_face_trade_dau_d_value(self):
        return self._device_face_trade_dau_d_value

    @device_face_trade_dau_d_value.setter
    def device_face_trade_dau_d_value(self, value):
        self._device_face_trade_dau_d_value = value
    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        self._device_name = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def device_status(self):
        return self._device_status

    @device_status.setter
    def device_status(self, value):
        self._device_status = value
    @property
    def face_trade_cnt(self):
        return self._face_trade_cnt

    @face_trade_cnt.setter
    def face_trade_cnt(self, value):
        self._face_trade_cnt = value
    @property
    def face_trd_amt(self):
        return self._face_trd_amt

    @face_trd_amt.setter
    def face_trd_amt(self, value):
        self._face_trd_amt = value
    @property
    def face_trd_cnt_rate(self):
        return self._face_trd_cnt_rate

    @face_trd_cnt_rate.setter
    def face_trd_cnt_rate(self, value):
        self._face_trd_cnt_rate = value
    @property
    def face_trd_user_cnt_rate(self):
        return self._face_trd_user_cnt_rate

    @face_trd_user_cnt_rate.setter
    def face_trd_user_cnt_rate(self, value):
        self._face_trd_user_cnt_rate = value
    @property
    def face_trd_user_cnt_rate_d_value(self):
        return self._face_trd_user_cnt_rate_d_value

    @face_trd_user_cnt_rate_d_value.setter
    def face_trd_user_cnt_rate_d_value(self, value):
        self._face_trd_user_cnt_rate_d_value = value
    @property
    def gmt_active(self):
        return self._gmt_active

    @gmt_active.setter
    def gmt_active(self, value):
        self._gmt_active = value
    @property
    def iot_trd_up(self):
        return self._iot_trd_up

    @iot_trd_up.setter
    def iot_trd_up(self, value):
        self._iot_trd_up = value
    @property
    def iot_trd_user_cnt(self):
        return self._iot_trd_user_cnt

    @iot_trd_user_cnt.setter
    def iot_trd_user_cnt(self, value):
        self._iot_trd_user_cnt = value
    @property
    def iot_trd_user_cnt_d_value(self):
        return self._iot_trd_user_cnt_d_value

    @iot_trd_user_cnt_d_value.setter
    def iot_trd_user_cnt_d_value(self, value):
        self._iot_trd_user_cnt_d_value = value
    @property
    def max_dt(self):
        return self._max_dt

    @max_dt.setter
    def max_dt(self, value):
        self._max_dt = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def trade_amt(self):
        return self._trade_amt

    @trade_amt.setter
    def trade_amt(self, value):
        self._trade_amt = value
    @property
    def trade_cnt(self):
        return self._trade_cnt

    @trade_cnt.setter
    def trade_cnt(self, value):
        self._trade_cnt = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.dau:
            if hasattr(self.dau, 'to_alipay_dict'):
                params['dau'] = self.dau.to_alipay_dict()
            else:
                params['dau'] = self.dau
        if self.device_face_trade_dau:
            if hasattr(self.device_face_trade_dau, 'to_alipay_dict'):
                params['device_face_trade_dau'] = self.device_face_trade_dau.to_alipay_dict()
            else:
                params['device_face_trade_dau'] = self.device_face_trade_dau
        if self.device_face_trade_dau_d_value:
            if hasattr(self.device_face_trade_dau_d_value, 'to_alipay_dict'):
                params['device_face_trade_dau_d_value'] = self.device_face_trade_dau_d_value.to_alipay_dict()
            else:
                params['device_face_trade_dau_d_value'] = self.device_face_trade_dau_d_value
        if self.device_name:
            if hasattr(self.device_name, 'to_alipay_dict'):
                params['device_name'] = self.device_name.to_alipay_dict()
            else:
                params['device_name'] = self.device_name
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.device_status:
            if hasattr(self.device_status, 'to_alipay_dict'):
                params['device_status'] = self.device_status.to_alipay_dict()
            else:
                params['device_status'] = self.device_status
        if self.face_trade_cnt:
            if hasattr(self.face_trade_cnt, 'to_alipay_dict'):
                params['face_trade_cnt'] = self.face_trade_cnt.to_alipay_dict()
            else:
                params['face_trade_cnt'] = self.face_trade_cnt
        if self.face_trd_amt:
            if hasattr(self.face_trd_amt, 'to_alipay_dict'):
                params['face_trd_amt'] = self.face_trd_amt.to_alipay_dict()
            else:
                params['face_trd_amt'] = self.face_trd_amt
        if self.face_trd_cnt_rate:
            if hasattr(self.face_trd_cnt_rate, 'to_alipay_dict'):
                params['face_trd_cnt_rate'] = self.face_trd_cnt_rate.to_alipay_dict()
            else:
                params['face_trd_cnt_rate'] = self.face_trd_cnt_rate
        if self.face_trd_user_cnt_rate:
            if hasattr(self.face_trd_user_cnt_rate, 'to_alipay_dict'):
                params['face_trd_user_cnt_rate'] = self.face_trd_user_cnt_rate.to_alipay_dict()
            else:
                params['face_trd_user_cnt_rate'] = self.face_trd_user_cnt_rate
        if self.face_trd_user_cnt_rate_d_value:
            if hasattr(self.face_trd_user_cnt_rate_d_value, 'to_alipay_dict'):
                params['face_trd_user_cnt_rate_d_value'] = self.face_trd_user_cnt_rate_d_value.to_alipay_dict()
            else:
                params['face_trd_user_cnt_rate_d_value'] = self.face_trd_user_cnt_rate_d_value
        if self.gmt_active:
            if hasattr(self.gmt_active, 'to_alipay_dict'):
                params['gmt_active'] = self.gmt_active.to_alipay_dict()
            else:
                params['gmt_active'] = self.gmt_active
        if self.iot_trd_up:
            if hasattr(self.iot_trd_up, 'to_alipay_dict'):
                params['iot_trd_up'] = self.iot_trd_up.to_alipay_dict()
            else:
                params['iot_trd_up'] = self.iot_trd_up
        if self.iot_trd_user_cnt:
            if hasattr(self.iot_trd_user_cnt, 'to_alipay_dict'):
                params['iot_trd_user_cnt'] = self.iot_trd_user_cnt.to_alipay_dict()
            else:
                params['iot_trd_user_cnt'] = self.iot_trd_user_cnt
        if self.iot_trd_user_cnt_d_value:
            if hasattr(self.iot_trd_user_cnt_d_value, 'to_alipay_dict'):
                params['iot_trd_user_cnt_d_value'] = self.iot_trd_user_cnt_d_value.to_alipay_dict()
            else:
                params['iot_trd_user_cnt_d_value'] = self.iot_trd_user_cnt_d_value
        if self.max_dt:
            if hasattr(self.max_dt, 'to_alipay_dict'):
                params['max_dt'] = self.max_dt.to_alipay_dict()
            else:
                params['max_dt'] = self.max_dt
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.trade_amt:
            if hasattr(self.trade_amt, 'to_alipay_dict'):
                params['trade_amt'] = self.trade_amt.to_alipay_dict()
            else:
                params['trade_amt'] = self.trade_amt
        if self.trade_cnt:
            if hasattr(self.trade_cnt, 'to_alipay_dict'):
                params['trade_cnt'] = self.trade_cnt.to_alipay_dict()
            else:
                params['trade_cnt'] = self.trade_cnt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceTradeInfoList()
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'dau' in d:
            o.dau = d['dau']
        if 'device_face_trade_dau' in d:
            o.device_face_trade_dau = d['device_face_trade_dau']
        if 'device_face_trade_dau_d_value' in d:
            o.device_face_trade_dau_d_value = d['device_face_trade_dau_d_value']
        if 'device_name' in d:
            o.device_name = d['device_name']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'device_status' in d:
            o.device_status = d['device_status']
        if 'face_trade_cnt' in d:
            o.face_trade_cnt = d['face_trade_cnt']
        if 'face_trd_amt' in d:
            o.face_trd_amt = d['face_trd_amt']
        if 'face_trd_cnt_rate' in d:
            o.face_trd_cnt_rate = d['face_trd_cnt_rate']
        if 'face_trd_user_cnt_rate' in d:
            o.face_trd_user_cnt_rate = d['face_trd_user_cnt_rate']
        if 'face_trd_user_cnt_rate_d_value' in d:
            o.face_trd_user_cnt_rate_d_value = d['face_trd_user_cnt_rate_d_value']
        if 'gmt_active' in d:
            o.gmt_active = d['gmt_active']
        if 'iot_trd_up' in d:
            o.iot_trd_up = d['iot_trd_up']
        if 'iot_trd_user_cnt' in d:
            o.iot_trd_user_cnt = d['iot_trd_user_cnt']
        if 'iot_trd_user_cnt_d_value' in d:
            o.iot_trd_user_cnt_d_value = d['iot_trd_user_cnt_d_value']
        if 'max_dt' in d:
            o.max_dt = d['max_dt']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'trade_amt' in d:
            o.trade_amt = d['trade_amt']
        if 'trade_cnt' in d:
            o.trade_cnt = d['trade_cnt']
        return o



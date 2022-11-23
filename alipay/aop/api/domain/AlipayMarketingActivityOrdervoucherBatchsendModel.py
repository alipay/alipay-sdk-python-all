#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivitySendVoucherInfo import ActivitySendVoucherInfo


class AlipayMarketingActivityOrdervoucherBatchsendModel(object):

    def __init__(self):
        self._activity_send_voucher_info_list = None
        self._biz_dt = None
        self._open_id = None
        self._promo_trace_info = None
        self._trade_channel = None
        self._trade_no = None
        self._user_id = None

    @property
    def activity_send_voucher_info_list(self):
        return self._activity_send_voucher_info_list

    @activity_send_voucher_info_list.setter
    def activity_send_voucher_info_list(self, value):
        if isinstance(value, list):
            self._activity_send_voucher_info_list = list()
            for i in value:
                if isinstance(i, ActivitySendVoucherInfo):
                    self._activity_send_voucher_info_list.append(i)
                else:
                    self._activity_send_voucher_info_list.append(ActivitySendVoucherInfo.from_alipay_dict(i))
    @property
    def biz_dt(self):
        return self._biz_dt

    @biz_dt.setter
    def biz_dt(self, value):
        self._biz_dt = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def promo_trace_info(self):
        return self._promo_trace_info

    @promo_trace_info.setter
    def promo_trace_info(self, value):
        self._promo_trace_info = value
    @property
    def trade_channel(self):
        return self._trade_channel

    @trade_channel.setter
    def trade_channel(self, value):
        self._trade_channel = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_send_voucher_info_list:
            if isinstance(self.activity_send_voucher_info_list, list):
                for i in range(0, len(self.activity_send_voucher_info_list)):
                    element = self.activity_send_voucher_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_send_voucher_info_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_send_voucher_info_list, 'to_alipay_dict'):
                params['activity_send_voucher_info_list'] = self.activity_send_voucher_info_list.to_alipay_dict()
            else:
                params['activity_send_voucher_info_list'] = self.activity_send_voucher_info_list
        if self.biz_dt:
            if hasattr(self.biz_dt, 'to_alipay_dict'):
                params['biz_dt'] = self.biz_dt.to_alipay_dict()
            else:
                params['biz_dt'] = self.biz_dt
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.promo_trace_info:
            if hasattr(self.promo_trace_info, 'to_alipay_dict'):
                params['promo_trace_info'] = self.promo_trace_info.to_alipay_dict()
            else:
                params['promo_trace_info'] = self.promo_trace_info
        if self.trade_channel:
            if hasattr(self.trade_channel, 'to_alipay_dict'):
                params['trade_channel'] = self.trade_channel.to_alipay_dict()
            else:
                params['trade_channel'] = self.trade_channel
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
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
        o = AlipayMarketingActivityOrdervoucherBatchsendModel()
        if 'activity_send_voucher_info_list' in d:
            o.activity_send_voucher_info_list = d['activity_send_voucher_info_list']
        if 'biz_dt' in d:
            o.biz_dt = d['biz_dt']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'promo_trace_info' in d:
            o.promo_trace_info = d['promo_trace_info']
        if 'trade_channel' in d:
            o.trade_channel = d['trade_channel']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



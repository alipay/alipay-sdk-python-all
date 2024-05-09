#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarMerchantOrderSyncModel(object):

    def __init__(self):
        self._alipay_trade_no = None
        self._ext_info = None
        self._open_id = None
        self._order_pay_time = None
        self._order_status = None
        self._order_type = None
        self._out_order_no = None
        self._out_order_time = None
        self._partner_id = None
        self._pay_amount = None
        self._pay_channel = None
        self._subject = None
        self._total_amount = None
        self._user_id = None
        self._user_phone = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_pay_time(self):
        return self._order_pay_time

    @order_pay_time.setter
    def order_pay_time(self, value):
        self._order_pay_time = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_order_time(self):
        return self._out_order_time

    @out_order_time.setter
    def out_order_time(self, value):
        self._out_order_time = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_phone(self):
        return self._user_phone

    @user_phone.setter
    def user_phone(self, value):
        self._user_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_pay_time:
            if hasattr(self.order_pay_time, 'to_alipay_dict'):
                params['order_pay_time'] = self.order_pay_time.to_alipay_dict()
            else:
                params['order_pay_time'] = self.order_pay_time
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_order_time:
            if hasattr(self.out_order_time, 'to_alipay_dict'):
                params['out_order_time'] = self.out_order_time.to_alipay_dict()
            else:
                params['out_order_time'] = self.out_order_time
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_phone:
            if hasattr(self.user_phone, 'to_alipay_dict'):
                params['user_phone'] = self.user_phone.to_alipay_dict()
            else:
                params['user_phone'] = self.user_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarMerchantOrderSyncModel()
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_pay_time' in d:
            o.order_pay_time = d['order_pay_time']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_order_time' in d:
            o.out_order_time = d['out_order_time']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_phone' in d:
            o.user_phone = d['user_phone']
        return o



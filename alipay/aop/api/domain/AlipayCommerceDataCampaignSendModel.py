#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceDataCampaignSendModel(object):

    def __init__(self):
        self._camp_category = None
        self._camp_channel = None
        self._camp_id = None
        self._camp_time = None
        self._cross_cycle = None
        self._cur_num = None
        self._ext_info = None
        self._notify_type = None
        self._serial_no = None
        self._total_num = None
        self._trade_no = None
        self._user_id = None

    @property
    def camp_category(self):
        return self._camp_category

    @camp_category.setter
    def camp_category(self, value):
        self._camp_category = value
    @property
    def camp_channel(self):
        return self._camp_channel

    @camp_channel.setter
    def camp_channel(self, value):
        self._camp_channel = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def camp_time(self):
        return self._camp_time

    @camp_time.setter
    def camp_time(self, value):
        self._camp_time = value
    @property
    def cross_cycle(self):
        return self._cross_cycle

    @cross_cycle.setter
    def cross_cycle(self, value):
        self._cross_cycle = value
    @property
    def cur_num(self):
        return self._cur_num

    @cur_num.setter
    def cur_num(self, value):
        self._cur_num = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def notify_type(self):
        return self._notify_type

    @notify_type.setter
    def notify_type(self, value):
        self._notify_type = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value
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
        if self.camp_category:
            if hasattr(self.camp_category, 'to_alipay_dict'):
                params['camp_category'] = self.camp_category.to_alipay_dict()
            else:
                params['camp_category'] = self.camp_category
        if self.camp_channel:
            if hasattr(self.camp_channel, 'to_alipay_dict'):
                params['camp_channel'] = self.camp_channel.to_alipay_dict()
            else:
                params['camp_channel'] = self.camp_channel
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.camp_time:
            if hasattr(self.camp_time, 'to_alipay_dict'):
                params['camp_time'] = self.camp_time.to_alipay_dict()
            else:
                params['camp_time'] = self.camp_time
        if self.cross_cycle:
            if hasattr(self.cross_cycle, 'to_alipay_dict'):
                params['cross_cycle'] = self.cross_cycle.to_alipay_dict()
            else:
                params['cross_cycle'] = self.cross_cycle
        if self.cur_num:
            if hasattr(self.cur_num, 'to_alipay_dict'):
                params['cur_num'] = self.cur_num.to_alipay_dict()
            else:
                params['cur_num'] = self.cur_num
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.notify_type:
            if hasattr(self.notify_type, 'to_alipay_dict'):
                params['notify_type'] = self.notify_type.to_alipay_dict()
            else:
                params['notify_type'] = self.notify_type
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.total_num:
            if hasattr(self.total_num, 'to_alipay_dict'):
                params['total_num'] = self.total_num.to_alipay_dict()
            else:
                params['total_num'] = self.total_num
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
        o = AlipayCommerceDataCampaignSendModel()
        if 'camp_category' in d:
            o.camp_category = d['camp_category']
        if 'camp_channel' in d:
            o.camp_channel = d['camp_channel']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'camp_time' in d:
            o.camp_time = d['camp_time']
        if 'cross_cycle' in d:
            o.cross_cycle = d['cross_cycle']
        if 'cur_num' in d:
            o.cur_num = d['cur_num']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'notify_type' in d:
            o.notify_type = d['notify_type']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'total_num' in d:
            o.total_num = d['total_num']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZMGOOpenConfig(object):

    def __init__(self):
        self._appoint_date = None
        self._card_color_scheme = None
        self._custom_open_tip_list = None
        self._custom_open_tips = None
        self._freeze_amount = None
        self._min_sign_interval = None
        self._period_mode = None
        self._period_time = None
        self._support_expire_deferral = None

    @property
    def appoint_date(self):
        return self._appoint_date

    @appoint_date.setter
    def appoint_date(self, value):
        self._appoint_date = value
    @property
    def card_color_scheme(self):
        return self._card_color_scheme

    @card_color_scheme.setter
    def card_color_scheme(self, value):
        self._card_color_scheme = value
    @property
    def custom_open_tip_list(self):
        return self._custom_open_tip_list

    @custom_open_tip_list.setter
    def custom_open_tip_list(self, value):
        self._custom_open_tip_list = value
    @property
    def custom_open_tips(self):
        return self._custom_open_tips

    @custom_open_tips.setter
    def custom_open_tips(self, value):
        self._custom_open_tips = value
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def min_sign_interval(self):
        return self._min_sign_interval

    @min_sign_interval.setter
    def min_sign_interval(self, value):
        self._min_sign_interval = value
    @property
    def period_mode(self):
        return self._period_mode

    @period_mode.setter
    def period_mode(self, value):
        self._period_mode = value
    @property
    def period_time(self):
        return self._period_time

    @period_time.setter
    def period_time(self, value):
        self._period_time = value
    @property
    def support_expire_deferral(self):
        return self._support_expire_deferral

    @support_expire_deferral.setter
    def support_expire_deferral(self, value):
        self._support_expire_deferral = value


    def to_alipay_dict(self):
        params = dict()
        if self.appoint_date:
            if hasattr(self.appoint_date, 'to_alipay_dict'):
                params['appoint_date'] = self.appoint_date.to_alipay_dict()
            else:
                params['appoint_date'] = self.appoint_date
        if self.card_color_scheme:
            if hasattr(self.card_color_scheme, 'to_alipay_dict'):
                params['card_color_scheme'] = self.card_color_scheme.to_alipay_dict()
            else:
                params['card_color_scheme'] = self.card_color_scheme
        if self.custom_open_tip_list:
            if hasattr(self.custom_open_tip_list, 'to_alipay_dict'):
                params['custom_open_tip_list'] = self.custom_open_tip_list.to_alipay_dict()
            else:
                params['custom_open_tip_list'] = self.custom_open_tip_list
        if self.custom_open_tips:
            if hasattr(self.custom_open_tips, 'to_alipay_dict'):
                params['custom_open_tips'] = self.custom_open_tips.to_alipay_dict()
            else:
                params['custom_open_tips'] = self.custom_open_tips
        if self.freeze_amount:
            if hasattr(self.freeze_amount, 'to_alipay_dict'):
                params['freeze_amount'] = self.freeze_amount.to_alipay_dict()
            else:
                params['freeze_amount'] = self.freeze_amount
        if self.min_sign_interval:
            if hasattr(self.min_sign_interval, 'to_alipay_dict'):
                params['min_sign_interval'] = self.min_sign_interval.to_alipay_dict()
            else:
                params['min_sign_interval'] = self.min_sign_interval
        if self.period_mode:
            if hasattr(self.period_mode, 'to_alipay_dict'):
                params['period_mode'] = self.period_mode.to_alipay_dict()
            else:
                params['period_mode'] = self.period_mode
        if self.period_time:
            if hasattr(self.period_time, 'to_alipay_dict'):
                params['period_time'] = self.period_time.to_alipay_dict()
            else:
                params['period_time'] = self.period_time
        if self.support_expire_deferral:
            if hasattr(self.support_expire_deferral, 'to_alipay_dict'):
                params['support_expire_deferral'] = self.support_expire_deferral.to_alipay_dict()
            else:
                params['support_expire_deferral'] = self.support_expire_deferral
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZMGOOpenConfig()
        if 'appoint_date' in d:
            o.appoint_date = d['appoint_date']
        if 'card_color_scheme' in d:
            o.card_color_scheme = d['card_color_scheme']
        if 'custom_open_tip_list' in d:
            o.custom_open_tip_list = d['custom_open_tip_list']
        if 'custom_open_tips' in d:
            o.custom_open_tips = d['custom_open_tips']
        if 'freeze_amount' in d:
            o.freeze_amount = d['freeze_amount']
        if 'min_sign_interval' in d:
            o.min_sign_interval = d['min_sign_interval']
        if 'period_mode' in d:
            o.period_mode = d['period_mode']
        if 'period_time' in d:
            o.period_time = d['period_time']
        if 'support_expire_deferral' in d:
            o.support_expire_deferral = d['support_expire_deferral']
        return o



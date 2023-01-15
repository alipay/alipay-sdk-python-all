#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZMGOOpenConfig(object):

    def __init__(self):
        self._apply_button_desc = None
        self._appoint_date = None
        self._card_color_scheme = None
        self._custom_open_tip_list = None
        self._custom_open_tips = None
        self._freeze_amount = None
        self._min_sign_interval = None
        self._period_mode = None
        self._period_time = None
        self._show_sign_success_page = None
        self._sign_again_schema = None
        self._sign_success_task_button_desc = None
        self._support_expire_deferral = None

    @property
    def apply_button_desc(self):
        return self._apply_button_desc

    @apply_button_desc.setter
    def apply_button_desc(self, value):
        self._apply_button_desc = value
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
    def show_sign_success_page(self):
        return self._show_sign_success_page

    @show_sign_success_page.setter
    def show_sign_success_page(self, value):
        self._show_sign_success_page = value
    @property
    def sign_again_schema(self):
        return self._sign_again_schema

    @sign_again_schema.setter
    def sign_again_schema(self, value):
        self._sign_again_schema = value
    @property
    def sign_success_task_button_desc(self):
        return self._sign_success_task_button_desc

    @sign_success_task_button_desc.setter
    def sign_success_task_button_desc(self, value):
        self._sign_success_task_button_desc = value
    @property
    def support_expire_deferral(self):
        return self._support_expire_deferral

    @support_expire_deferral.setter
    def support_expire_deferral(self, value):
        self._support_expire_deferral = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_button_desc:
            if hasattr(self.apply_button_desc, 'to_alipay_dict'):
                params['apply_button_desc'] = self.apply_button_desc.to_alipay_dict()
            else:
                params['apply_button_desc'] = self.apply_button_desc
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
        if self.show_sign_success_page:
            if hasattr(self.show_sign_success_page, 'to_alipay_dict'):
                params['show_sign_success_page'] = self.show_sign_success_page.to_alipay_dict()
            else:
                params['show_sign_success_page'] = self.show_sign_success_page
        if self.sign_again_schema:
            if hasattr(self.sign_again_schema, 'to_alipay_dict'):
                params['sign_again_schema'] = self.sign_again_schema.to_alipay_dict()
            else:
                params['sign_again_schema'] = self.sign_again_schema
        if self.sign_success_task_button_desc:
            if hasattr(self.sign_success_task_button_desc, 'to_alipay_dict'):
                params['sign_success_task_button_desc'] = self.sign_success_task_button_desc.to_alipay_dict()
            else:
                params['sign_success_task_button_desc'] = self.sign_success_task_button_desc
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
        if 'apply_button_desc' in d:
            o.apply_button_desc = d['apply_button_desc']
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
        if 'show_sign_success_page' in d:
            o.show_sign_success_page = d['show_sign_success_page']
        if 'sign_again_schema' in d:
            o.sign_again_schema = d['sign_again_schema']
        if 'sign_success_task_button_desc' in d:
            o.sign_success_task_button_desc = d['sign_success_task_button_desc']
        if 'support_expire_deferral' in d:
            o.support_expire_deferral = d['support_expire_deferral']
        return o



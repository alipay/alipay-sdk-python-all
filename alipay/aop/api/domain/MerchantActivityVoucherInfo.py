#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantActivityVoucherInfo(object):

    def __init__(self):
        self._logo = None
        self._sub_title = None
        self._user_introductions = None
        self._valid_days_range_from = None
        self._valid_days_range_to = None
        self._valid_time_range_from = None
        self._valid_time_range_to = None
        self._valid_time_type = None

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def user_introductions(self):
        return self._user_introductions

    @user_introductions.setter
    def user_introductions(self, value):
        self._user_introductions = value
    @property
    def valid_days_range_from(self):
        return self._valid_days_range_from

    @valid_days_range_from.setter
    def valid_days_range_from(self, value):
        self._valid_days_range_from = value
    @property
    def valid_days_range_to(self):
        return self._valid_days_range_to

    @valid_days_range_to.setter
    def valid_days_range_to(self, value):
        self._valid_days_range_to = value
    @property
    def valid_time_range_from(self):
        return self._valid_time_range_from

    @valid_time_range_from.setter
    def valid_time_range_from(self, value):
        self._valid_time_range_from = value
    @property
    def valid_time_range_to(self):
        return self._valid_time_range_to

    @valid_time_range_to.setter
    def valid_time_range_to(self, value):
        self._valid_time_range_to = value
    @property
    def valid_time_type(self):
        return self._valid_time_type

    @valid_time_type.setter
    def valid_time_type(self, value):
        self._valid_time_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.user_introductions:
            if hasattr(self.user_introductions, 'to_alipay_dict'):
                params['user_introductions'] = self.user_introductions.to_alipay_dict()
            else:
                params['user_introductions'] = self.user_introductions
        if self.valid_days_range_from:
            if hasattr(self.valid_days_range_from, 'to_alipay_dict'):
                params['valid_days_range_from'] = self.valid_days_range_from.to_alipay_dict()
            else:
                params['valid_days_range_from'] = self.valid_days_range_from
        if self.valid_days_range_to:
            if hasattr(self.valid_days_range_to, 'to_alipay_dict'):
                params['valid_days_range_to'] = self.valid_days_range_to.to_alipay_dict()
            else:
                params['valid_days_range_to'] = self.valid_days_range_to
        if self.valid_time_range_from:
            if hasattr(self.valid_time_range_from, 'to_alipay_dict'):
                params['valid_time_range_from'] = self.valid_time_range_from.to_alipay_dict()
            else:
                params['valid_time_range_from'] = self.valid_time_range_from
        if self.valid_time_range_to:
            if hasattr(self.valid_time_range_to, 'to_alipay_dict'):
                params['valid_time_range_to'] = self.valid_time_range_to.to_alipay_dict()
            else:
                params['valid_time_range_to'] = self.valid_time_range_to
        if self.valid_time_type:
            if hasattr(self.valid_time_type, 'to_alipay_dict'):
                params['valid_time_type'] = self.valid_time_type.to_alipay_dict()
            else:
                params['valid_time_type'] = self.valid_time_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantActivityVoucherInfo()
        if 'logo' in d:
            o.logo = d['logo']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'user_introductions' in d:
            o.user_introductions = d['user_introductions']
        if 'valid_days_range_from' in d:
            o.valid_days_range_from = d['valid_days_range_from']
        if 'valid_days_range_to' in d:
            o.valid_days_range_to = d['valid_days_range_to']
        if 'valid_time_range_from' in d:
            o.valid_time_range_from = d['valid_time_range_from']
        if 'valid_time_range_to' in d:
            o.valid_time_range_to = d['valid_time_range_to']
        if 'valid_time_type' in d:
            o.valid_time_type = d['valid_time_type']
        return o



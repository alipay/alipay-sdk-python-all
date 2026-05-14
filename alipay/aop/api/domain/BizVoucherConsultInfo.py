#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizVoucherConsultInfo(object):

    def __init__(self):
        self._active_time = None
        self._biz_logo = None
        self._expire_time = None
        self._optimal = None
        self._promo_text = None
        self._promo_type = None
        self._use_threshold_text = None
        self._voucher_id = None
        self._voucher_link_url = None
        self._voucher_name = None
        self._voucher_value = None

    @property
    def active_time(self):
        return self._active_time

    @active_time.setter
    def active_time(self, value):
        self._active_time = value
    @property
    def biz_logo(self):
        return self._biz_logo

    @biz_logo.setter
    def biz_logo(self, value):
        self._biz_logo = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def optimal(self):
        return self._optimal

    @optimal.setter
    def optimal(self, value):
        self._optimal = value
    @property
    def promo_text(self):
        return self._promo_text

    @promo_text.setter
    def promo_text(self, value):
        self._promo_text = value
    @property
    def promo_type(self):
        return self._promo_type

    @promo_type.setter
    def promo_type(self, value):
        self._promo_type = value
    @property
    def use_threshold_text(self):
        return self._use_threshold_text

    @use_threshold_text.setter
    def use_threshold_text(self, value):
        self._use_threshold_text = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_link_url(self):
        return self._voucher_link_url

    @voucher_link_url.setter
    def voucher_link_url(self, value):
        self._voucher_link_url = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_value(self):
        return self._voucher_value

    @voucher_value.setter
    def voucher_value(self, value):
        self._voucher_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_time:
            if hasattr(self.active_time, 'to_alipay_dict'):
                params['active_time'] = self.active_time.to_alipay_dict()
            else:
                params['active_time'] = self.active_time
        if self.biz_logo:
            if hasattr(self.biz_logo, 'to_alipay_dict'):
                params['biz_logo'] = self.biz_logo.to_alipay_dict()
            else:
                params['biz_logo'] = self.biz_logo
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.optimal:
            if hasattr(self.optimal, 'to_alipay_dict'):
                params['optimal'] = self.optimal.to_alipay_dict()
            else:
                params['optimal'] = self.optimal
        if self.promo_text:
            if hasattr(self.promo_text, 'to_alipay_dict'):
                params['promo_text'] = self.promo_text.to_alipay_dict()
            else:
                params['promo_text'] = self.promo_text
        if self.promo_type:
            if hasattr(self.promo_type, 'to_alipay_dict'):
                params['promo_type'] = self.promo_type.to_alipay_dict()
            else:
                params['promo_type'] = self.promo_type
        if self.use_threshold_text:
            if hasattr(self.use_threshold_text, 'to_alipay_dict'):
                params['use_threshold_text'] = self.use_threshold_text.to_alipay_dict()
            else:
                params['use_threshold_text'] = self.use_threshold_text
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_link_url:
            if hasattr(self.voucher_link_url, 'to_alipay_dict'):
                params['voucher_link_url'] = self.voucher_link_url.to_alipay_dict()
            else:
                params['voucher_link_url'] = self.voucher_link_url
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_value:
            if hasattr(self.voucher_value, 'to_alipay_dict'):
                params['voucher_value'] = self.voucher_value.to_alipay_dict()
            else:
                params['voucher_value'] = self.voucher_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizVoucherConsultInfo()
        if 'active_time' in d:
            o.active_time = d['active_time']
        if 'biz_logo' in d:
            o.biz_logo = d['biz_logo']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'optimal' in d:
            o.optimal = d['optimal']
        if 'promo_text' in d:
            o.promo_text = d['promo_text']
        if 'promo_type' in d:
            o.promo_type = d['promo_type']
        if 'use_threshold_text' in d:
            o.use_threshold_text = d['use_threshold_text']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_link_url' in d:
            o.voucher_link_url = d['voucher_link_url']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_value' in d:
            o.voucher_value = d['voucher_value']
        return o



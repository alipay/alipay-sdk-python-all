#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizCard(object):

    def __init__(self):
        self._active_time = None
        self._card_link_url = None
        self._card_name = None
        self._card_no = None
        self._card_status = None
        self._card_template_code = None
        self._card_type = None
        self._card_validity_period_type = None
        self._expire_time = None

    @property
    def active_time(self):
        return self._active_time

    @active_time.setter
    def active_time(self, value):
        self._active_time = value
    @property
    def card_link_url(self):
        return self._card_link_url

    @card_link_url.setter
    def card_link_url(self, value):
        self._card_link_url = value
    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_status(self):
        return self._card_status

    @card_status.setter
    def card_status(self, value):
        self._card_status = value
    @property
    def card_template_code(self):
        return self._card_template_code

    @card_template_code.setter
    def card_template_code(self, value):
        self._card_template_code = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def card_validity_period_type(self):
        return self._card_validity_period_type

    @card_validity_period_type.setter
    def card_validity_period_type(self, value):
        self._card_validity_period_type = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_time:
            if hasattr(self.active_time, 'to_alipay_dict'):
                params['active_time'] = self.active_time.to_alipay_dict()
            else:
                params['active_time'] = self.active_time
        if self.card_link_url:
            if hasattr(self.card_link_url, 'to_alipay_dict'):
                params['card_link_url'] = self.card_link_url.to_alipay_dict()
            else:
                params['card_link_url'] = self.card_link_url
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_status:
            if hasattr(self.card_status, 'to_alipay_dict'):
                params['card_status'] = self.card_status.to_alipay_dict()
            else:
                params['card_status'] = self.card_status
        if self.card_template_code:
            if hasattr(self.card_template_code, 'to_alipay_dict'):
                params['card_template_code'] = self.card_template_code.to_alipay_dict()
            else:
                params['card_template_code'] = self.card_template_code
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.card_validity_period_type:
            if hasattr(self.card_validity_period_type, 'to_alipay_dict'):
                params['card_validity_period_type'] = self.card_validity_period_type.to_alipay_dict()
            else:
                params['card_validity_period_type'] = self.card_validity_period_type
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizCard()
        if 'active_time' in d:
            o.active_time = d['active_time']
        if 'card_link_url' in d:
            o.card_link_url = d['card_link_url']
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_status' in d:
            o.card_status = d['card_status']
        if 'card_template_code' in d:
            o.card_template_code = d['card_template_code']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'card_validity_period_type' in d:
            o.card_validity_period_type = d['card_validity_period_type']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        return o



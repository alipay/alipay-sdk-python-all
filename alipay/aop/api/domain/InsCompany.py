#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsCompany(object):

    def __init__(self):
        self._alipay_account_no = None
        self._cert_name = None
        self._cert_no = None
        self._channel_account_id = None
        self._channel_account_type = None
        self._phone = None

    @property
    def alipay_account_no(self):
        return self._alipay_account_no

    @alipay_account_no.setter
    def alipay_account_no(self, value):
        self._alipay_account_no = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def channel_account_id(self):
        return self._channel_account_id

    @channel_account_id.setter
    def channel_account_id(self, value):
        self._channel_account_id = value
    @property
    def channel_account_type(self):
        return self._channel_account_type

    @channel_account_type.setter
    def channel_account_type(self, value):
        self._channel_account_type = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_account_no:
            if hasattr(self.alipay_account_no, 'to_alipay_dict'):
                params['alipay_account_no'] = self.alipay_account_no.to_alipay_dict()
            else:
                params['alipay_account_no'] = self.alipay_account_no
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.channel_account_id:
            if hasattr(self.channel_account_id, 'to_alipay_dict'):
                params['channel_account_id'] = self.channel_account_id.to_alipay_dict()
            else:
                params['channel_account_id'] = self.channel_account_id
        if self.channel_account_type:
            if hasattr(self.channel_account_type, 'to_alipay_dict'):
                params['channel_account_type'] = self.channel_account_type.to_alipay_dict()
            else:
                params['channel_account_type'] = self.channel_account_type
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsCompany()
        if 'alipay_account_no' in d:
            o.alipay_account_no = d['alipay_account_no']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'channel_account_id' in d:
            o.channel_account_id = d['channel_account_id']
        if 'channel_account_type' in d:
            o.channel_account_type = d['channel_account_type']
        if 'phone' in d:
            o.phone = d['phone']
        return o



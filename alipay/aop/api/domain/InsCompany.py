#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsCompany(object):

    def __init__(self):
        self._alipay_account_no = None
        self._alipay_account_open_id = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._channel_account_id = None
        self._channel_account_type = None
        self._company_cert_no = None
        self._company_name = None
        self._phone = None
        self._platform_identity = None

    @property
    def alipay_account_no(self):
        return self._alipay_account_no

    @alipay_account_no.setter
    def alipay_account_no(self, value):
        self._alipay_account_no = value
    @property
    def alipay_account_open_id(self):
        return self._alipay_account_open_id

    @alipay_account_open_id.setter
    def alipay_account_open_id(self, value):
        self._alipay_account_open_id = value
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
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
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
    def company_cert_no(self):
        return self._company_cert_no

    @company_cert_no.setter
    def company_cert_no(self, value):
        self._company_cert_no = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def platform_identity(self):
        return self._platform_identity

    @platform_identity.setter
    def platform_identity(self, value):
        self._platform_identity = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_account_no:
            if hasattr(self.alipay_account_no, 'to_alipay_dict'):
                params['alipay_account_no'] = self.alipay_account_no.to_alipay_dict()
            else:
                params['alipay_account_no'] = self.alipay_account_no
        if self.alipay_account_open_id:
            if hasattr(self.alipay_account_open_id, 'to_alipay_dict'):
                params['alipay_account_open_id'] = self.alipay_account_open_id.to_alipay_dict()
            else:
                params['alipay_account_open_id'] = self.alipay_account_open_id
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
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
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
        if self.company_cert_no:
            if hasattr(self.company_cert_no, 'to_alipay_dict'):
                params['company_cert_no'] = self.company_cert_no.to_alipay_dict()
            else:
                params['company_cert_no'] = self.company_cert_no
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.platform_identity:
            if hasattr(self.platform_identity, 'to_alipay_dict'):
                params['platform_identity'] = self.platform_identity.to_alipay_dict()
            else:
                params['platform_identity'] = self.platform_identity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsCompany()
        if 'alipay_account_no' in d:
            o.alipay_account_no = d['alipay_account_no']
        if 'alipay_account_open_id' in d:
            o.alipay_account_open_id = d['alipay_account_open_id']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'channel_account_id' in d:
            o.channel_account_id = d['channel_account_id']
        if 'channel_account_type' in d:
            o.channel_account_type = d['channel_account_type']
        if 'company_cert_no' in d:
            o.company_cert_no = d['company_cert_no']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'phone' in d:
            o.phone = d['phone']
        if 'platform_identity' in d:
            o.platform_identity = d['platform_identity']
        return o



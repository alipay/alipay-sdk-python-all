#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechMorseMarketingRtaSendModel(object):

    def __init__(self):
        self._campaign_id = None
        self._cert_encryption = None
        self._encryption_type = None
        self._extend_params = None
        self._login_id_encryption = None
        self._mobile_encryption = None
        self._out_biz_no = None
        self._resource_id = None
        self._send_type = None
        self._user_pass_time = None

    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value
    @property
    def cert_encryption(self):
        return self._cert_encryption

    @cert_encryption.setter
    def cert_encryption(self, value):
        self._cert_encryption = value
    @property
    def encryption_type(self):
        return self._encryption_type

    @encryption_type.setter
    def encryption_type(self, value):
        self._encryption_type = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def login_id_encryption(self):
        return self._login_id_encryption

    @login_id_encryption.setter
    def login_id_encryption(self, value):
        self._login_id_encryption = value
    @property
    def mobile_encryption(self):
        return self._mobile_encryption

    @mobile_encryption.setter
    def mobile_encryption(self, value):
        self._mobile_encryption = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def send_type(self):
        return self._send_type

    @send_type.setter
    def send_type(self, value):
        self._send_type = value
    @property
    def user_pass_time(self):
        return self._user_pass_time

    @user_pass_time.setter
    def user_pass_time(self, value):
        self._user_pass_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.campaign_id:
            if hasattr(self.campaign_id, 'to_alipay_dict'):
                params['campaign_id'] = self.campaign_id.to_alipay_dict()
            else:
                params['campaign_id'] = self.campaign_id
        if self.cert_encryption:
            if hasattr(self.cert_encryption, 'to_alipay_dict'):
                params['cert_encryption'] = self.cert_encryption.to_alipay_dict()
            else:
                params['cert_encryption'] = self.cert_encryption
        if self.encryption_type:
            if hasattr(self.encryption_type, 'to_alipay_dict'):
                params['encryption_type'] = self.encryption_type.to_alipay_dict()
            else:
                params['encryption_type'] = self.encryption_type
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.login_id_encryption:
            if hasattr(self.login_id_encryption, 'to_alipay_dict'):
                params['login_id_encryption'] = self.login_id_encryption.to_alipay_dict()
            else:
                params['login_id_encryption'] = self.login_id_encryption
        if self.mobile_encryption:
            if hasattr(self.mobile_encryption, 'to_alipay_dict'):
                params['mobile_encryption'] = self.mobile_encryption.to_alipay_dict()
            else:
                params['mobile_encryption'] = self.mobile_encryption
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        if self.send_type:
            if hasattr(self.send_type, 'to_alipay_dict'):
                params['send_type'] = self.send_type.to_alipay_dict()
            else:
                params['send_type'] = self.send_type
        if self.user_pass_time:
            if hasattr(self.user_pass_time, 'to_alipay_dict'):
                params['user_pass_time'] = self.user_pass_time.to_alipay_dict()
            else:
                params['user_pass_time'] = self.user_pass_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechMorseMarketingRtaSendModel()
        if 'campaign_id' in d:
            o.campaign_id = d['campaign_id']
        if 'cert_encryption' in d:
            o.cert_encryption = d['cert_encryption']
        if 'encryption_type' in d:
            o.encryption_type = d['encryption_type']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'login_id_encryption' in d:
            o.login_id_encryption = d['login_id_encryption']
        if 'mobile_encryption' in d:
            o.mobile_encryption = d['mobile_encryption']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        if 'send_type' in d:
            o.send_type = d['send_type']
        if 'user_pass_time' in d:
            o.user_pass_time = d['user_pass_time']
        return o



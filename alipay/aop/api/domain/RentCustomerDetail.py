#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentCustomerDetail(object):

    def __init__(self):
        self._alipay_open_id = None
        self._alipay_user_id = None
        self._cert_no = None
        self._cert_no_sha_256 = None
        self._mobile = None
        self._mobile_sha_256 = None

    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_no_sha_256(self):
        return self._cert_no_sha_256

    @cert_no_sha_256.setter
    def cert_no_sha_256(self, value):
        self._cert_no_sha_256 = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def mobile_sha_256(self):
        return self._mobile_sha_256

    @mobile_sha_256.setter
    def mobile_sha_256(self, value):
        self._mobile_sha_256 = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_no_sha_256:
            if hasattr(self.cert_no_sha_256, 'to_alipay_dict'):
                params['cert_no_sha_256'] = self.cert_no_sha_256.to_alipay_dict()
            else:
                params['cert_no_sha_256'] = self.cert_no_sha_256
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.mobile_sha_256:
            if hasattr(self.mobile_sha_256, 'to_alipay_dict'):
                params['mobile_sha_256'] = self.mobile_sha_256.to_alipay_dict()
            else:
                params['mobile_sha_256'] = self.mobile_sha_256
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCustomerDetail()
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_no_sha_256' in d:
            o.cert_no_sha_256 = d['cert_no_sha_256']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'mobile_sha_256' in d:
            o.mobile_sha_256 = d['mobile_sha_256']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpCertificationRiskIdentifyModel(object):

    def __init__(self):
        self._biz_no = None
        self._ep_cert_no = None
        self._ep_name = None
        self._risk_identify_type = None
        self._user_cert_no = None
        self._user_name = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def risk_identify_type(self):
        return self._risk_identify_type

    @risk_identify_type.setter
    def risk_identify_type(self, value):
        self._risk_identify_type = value
    @property
    def user_cert_no(self):
        return self._user_cert_no

    @user_cert_no.setter
    def user_cert_no(self, value):
        self._user_cert_no = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.risk_identify_type:
            if hasattr(self.risk_identify_type, 'to_alipay_dict'):
                params['risk_identify_type'] = self.risk_identify_type.to_alipay_dict()
            else:
                params['risk_identify_type'] = self.risk_identify_type
        if self.user_cert_no:
            if hasattr(self.user_cert_no, 'to_alipay_dict'):
                params['user_cert_no'] = self.user_cert_no.to_alipay_dict()
            else:
                params['user_cert_no'] = self.user_cert_no
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpCertificationRiskIdentifyModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'risk_identify_type' in d:
            o.risk_identify_type = d['risk_identify_type']
        if 'user_cert_no' in d:
            o.user_cert_no = d['user_cert_no']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o



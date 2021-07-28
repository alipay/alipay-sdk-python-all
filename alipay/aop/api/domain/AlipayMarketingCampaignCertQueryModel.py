#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignCertQueryModel(object):

    def __init__(self):
        self._cert_template_id = None
        self._login_id = None
        self._user_id = None

    @property
    def cert_template_id(self):
        return self._cert_template_id

    @cert_template_id.setter
    def cert_template_id(self, value):
        self._cert_template_id = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_template_id:
            if hasattr(self.cert_template_id, 'to_alipay_dict'):
                params['cert_template_id'] = self.cert_template_id.to_alipay_dict()
            else:
                params['cert_template_id'] = self.cert_template_id
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignCertQueryModel()
        if 'cert_template_id' in d:
            o.cert_template_id = d['cert_template_id']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



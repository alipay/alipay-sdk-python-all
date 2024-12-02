#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceUserAuthQueryModel(object):

    def __init__(self):
        self._mobile_phone = None
        self._redirect_url = None
        self._source_tag = None
        self._user_email = None

    @property
    def mobile_phone(self):
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        self._mobile_phone = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def source_tag(self):
        return self._source_tag

    @source_tag.setter
    def source_tag(self, value):
        self._source_tag = value
    @property
    def user_email(self):
        return self._user_email

    @user_email.setter
    def user_email(self, value):
        self._user_email = value


    def to_alipay_dict(self):
        params = dict()
        if self.mobile_phone:
            if hasattr(self.mobile_phone, 'to_alipay_dict'):
                params['mobile_phone'] = self.mobile_phone.to_alipay_dict()
            else:
                params['mobile_phone'] = self.mobile_phone
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        if self.source_tag:
            if hasattr(self.source_tag, 'to_alipay_dict'):
                params['source_tag'] = self.source_tag.to_alipay_dict()
            else:
                params['source_tag'] = self.source_tag
        if self.user_email:
            if hasattr(self.user_email, 'to_alipay_dict'):
                params['user_email'] = self.user_email.to_alipay_dict()
            else:
                params['user_email'] = self.user_email
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceUserAuthQueryModel()
        if 'mobile_phone' in d:
            o.mobile_phone = d['mobile_phone']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'source_tag' in d:
            o.source_tag = d['source_tag']
        if 'user_email' in d:
            o.user_email = d['user_email']
        return o



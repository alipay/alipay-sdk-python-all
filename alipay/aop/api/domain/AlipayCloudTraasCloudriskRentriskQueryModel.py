#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudTraasCloudriskRentriskQueryModel(object):

    def __init__(self):
        self._cert_no = None
        self._mobile = None
        self._out_biz_no = None
        self._user_authorization = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def user_authorization(self):
        return self._user_authorization

    @user_authorization.setter
    def user_authorization(self, value):
        self._user_authorization = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.user_authorization:
            if hasattr(self.user_authorization, 'to_alipay_dict'):
                params['user_authorization'] = self.user_authorization.to_alipay_dict()
            else:
                params['user_authorization'] = self.user_authorization
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudTraasCloudriskRentriskQueryModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'user_authorization' in d:
            o.user_authorization = d['user_authorization']
        return o



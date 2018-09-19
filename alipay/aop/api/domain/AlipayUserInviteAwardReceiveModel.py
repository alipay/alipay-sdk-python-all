#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserInviteAwardReceiveModel(object):

    def __init__(self):
        self._mobile = None
        self._out_biz_code = None
        self._out_biz_no = None
        self._user_id = None

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def out_biz_code(self):
        return self._out_biz_code

    @out_biz_code.setter
    def out_biz_code(self, value):
        self._out_biz_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.out_biz_code:
            if hasattr(self.out_biz_code, 'to_alipay_dict'):
                params['out_biz_code'] = self.out_biz_code.to_alipay_dict()
            else:
                params['out_biz_code'] = self.out_biz_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        o = AlipayUserInviteAwardReceiveModel()
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'out_biz_code' in d:
            o.out_biz_code = d['out_biz_code']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



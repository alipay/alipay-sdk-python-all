#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignData(object):

    def __init__(self):
        self._ori_app_id = None
        self._ori_char_set = None
        self._ori_out_biz_no = None
        self._ori_sign = None
        self._ori_sign_type = None
        self._partner_id = None

    @property
    def ori_app_id(self):
        return self._ori_app_id

    @ori_app_id.setter
    def ori_app_id(self, value):
        self._ori_app_id = value
    @property
    def ori_char_set(self):
        return self._ori_char_set

    @ori_char_set.setter
    def ori_char_set(self, value):
        self._ori_char_set = value
    @property
    def ori_out_biz_no(self):
        return self._ori_out_biz_no

    @ori_out_biz_no.setter
    def ori_out_biz_no(self, value):
        self._ori_out_biz_no = value
    @property
    def ori_sign(self):
        return self._ori_sign

    @ori_sign.setter
    def ori_sign(self, value):
        self._ori_sign = value
    @property
    def ori_sign_type(self):
        return self._ori_sign_type

    @ori_sign_type.setter
    def ori_sign_type(self, value):
        self._ori_sign_type = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ori_app_id:
            if hasattr(self.ori_app_id, 'to_alipay_dict'):
                params['ori_app_id'] = self.ori_app_id.to_alipay_dict()
            else:
                params['ori_app_id'] = self.ori_app_id
        if self.ori_char_set:
            if hasattr(self.ori_char_set, 'to_alipay_dict'):
                params['ori_char_set'] = self.ori_char_set.to_alipay_dict()
            else:
                params['ori_char_set'] = self.ori_char_set
        if self.ori_out_biz_no:
            if hasattr(self.ori_out_biz_no, 'to_alipay_dict'):
                params['ori_out_biz_no'] = self.ori_out_biz_no.to_alipay_dict()
            else:
                params['ori_out_biz_no'] = self.ori_out_biz_no
        if self.ori_sign:
            if hasattr(self.ori_sign, 'to_alipay_dict'):
                params['ori_sign'] = self.ori_sign.to_alipay_dict()
            else:
                params['ori_sign'] = self.ori_sign
        if self.ori_sign_type:
            if hasattr(self.ori_sign_type, 'to_alipay_dict'):
                params['ori_sign_type'] = self.ori_sign_type.to_alipay_dict()
            else:
                params['ori_sign_type'] = self.ori_sign_type
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignData()
        if 'ori_app_id' in d:
            o.ori_app_id = d['ori_app_id']
        if 'ori_char_set' in d:
            o.ori_char_set = d['ori_char_set']
        if 'ori_out_biz_no' in d:
            o.ori_out_biz_no = d['ori_out_biz_no']
        if 'ori_sign' in d:
            o.ori_sign = d['ori_sign']
        if 'ori_sign_type' in d:
            o.ori_sign_type = d['ori_sign_type']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCharityWithholdCreateModel(object):

    def __init__(self):
        self._biz_id = None
        self._donate_amount = None
        self._ext_info = None
        self._out_biz_no = None
        self._product_code = None
        self._project_id = None
        self._user_id = None
        self._withhold_pid = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def donate_amount(self):
        return self._donate_amount

    @donate_amount.setter
    def donate_amount(self, value):
        self._donate_amount = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def withhold_pid(self):
        return self._withhold_pid

    @withhold_pid.setter
    def withhold_pid(self, value):
        self._withhold_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.donate_amount:
            if hasattr(self.donate_amount, 'to_alipay_dict'):
                params['donate_amount'] = self.donate_amount.to_alipay_dict()
            else:
                params['donate_amount'] = self.donate_amount
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.withhold_pid:
            if hasattr(self.withhold_pid, 'to_alipay_dict'):
                params['withhold_pid'] = self.withhold_pid.to_alipay_dict()
            else:
                params['withhold_pid'] = self.withhold_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCharityWithholdCreateModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'donate_amount' in d:
            o.donate_amount = d['donate_amount']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'withhold_pid' in d:
            o.withhold_pid = d['withhold_pid']
        return o



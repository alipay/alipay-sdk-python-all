#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UseDetail import UseDetail


class AlipayInsAutoBenefitUseModel(object):

    def __init__(self):
        self._benefit_code = None
        self._out_biz_no = None
        self._use_detail = None
        self._user_id = None

    @property
    def benefit_code(self):
        return self._benefit_code

    @benefit_code.setter
    def benefit_code(self, value):
        self._benefit_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def use_detail(self):
        return self._use_detail

    @use_detail.setter
    def use_detail(self, value):
        if isinstance(value, UseDetail):
            self._use_detail = value
        else:
            self._use_detail = UseDetail.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_code:
            if hasattr(self.benefit_code, 'to_alipay_dict'):
                params['benefit_code'] = self.benefit_code.to_alipay_dict()
            else:
                params['benefit_code'] = self.benefit_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.use_detail:
            if hasattr(self.use_detail, 'to_alipay_dict'):
                params['use_detail'] = self.use_detail.to_alipay_dict()
            else:
                params['use_detail'] = self.use_detail
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
        o = AlipayInsAutoBenefitUseModel()
        if 'benefit_code' in d:
            o.benefit_code = d['benefit_code']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'use_detail' in d:
            o.use_detail = d['use_detail']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandBenefitConfirmModel(object):

    def __init__(self):
        self._biz_ext = None
        self._out_biz_time = None
        self._record_id = None
        self._user_id = None

    @property
    def biz_ext(self):
        return self._biz_ext

    @biz_ext.setter
    def biz_ext(self, value):
        self._biz_ext = value
    @property
    def out_biz_time(self):
        return self._out_biz_time

    @out_biz_time.setter
    def out_biz_time(self, value):
        self._out_biz_time = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_ext:
            if hasattr(self.biz_ext, 'to_alipay_dict'):
                params['biz_ext'] = self.biz_ext.to_alipay_dict()
            else:
                params['biz_ext'] = self.biz_ext
        if self.out_biz_time:
            if hasattr(self.out_biz_time, 'to_alipay_dict'):
                params['out_biz_time'] = self.out_biz_time.to_alipay_dict()
            else:
                params['out_biz_time'] = self.out_biz_time
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
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
        o = AntMerchantExpandBenefitConfirmModel()
        if 'biz_ext' in d:
            o.biz_ext = d['biz_ext']
        if 'out_biz_time' in d:
            o.out_biz_time = d['out_biz_time']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiPcreditbenefitFuncardreachSendModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._biz_no = None
        self._funka_dollar = None
        self._open_id = None
        self._solution_id = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def funka_dollar(self):
        return self._funka_dollar

    @funka_dollar.setter
    def funka_dollar(self, value):
        self._funka_dollar = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.funka_dollar:
            if hasattr(self.funka_dollar, 'to_alipay_dict'):
                params['funka_dollar'] = self.funka_dollar.to_alipay_dict()
            else:
                params['funka_dollar'] = self.funka_dollar
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.solution_id:
            if hasattr(self.solution_id, 'to_alipay_dict'):
                params['solution_id'] = self.solution_id.to_alipay_dict()
            else:
                params['solution_id'] = self.solution_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiPcreditbenefitFuncardreachSendModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'funka_dollar' in d:
            o.funka_dollar = d['funka_dollar']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'solution_id' in d:
            o.solution_id = d['solution_id']
        return o



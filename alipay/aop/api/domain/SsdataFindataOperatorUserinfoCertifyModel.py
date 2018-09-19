#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LoginForm import LoginForm


class SsdataFindataOperatorUserinfoCertifyModel(object):

    def __init__(self):
        self._biz_no = None
        self._form_map = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def form_map(self):
        return self._form_map

    @form_map.setter
    def form_map(self, value):
        if isinstance(value, LoginForm):
            self._form_map = value
        else:
            self._form_map = LoginForm.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.form_map:
            if hasattr(self.form_map, 'to_alipay_dict'):
                params['form_map'] = self.form_map.to_alipay_dict()
            else:
                params['form_map'] = self.form_map
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataFindataOperatorUserinfoCertifyModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'form_map' in d:
            o.form_map = d['form_map']
        return o



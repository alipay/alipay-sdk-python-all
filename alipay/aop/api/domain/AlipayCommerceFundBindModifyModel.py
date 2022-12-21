#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceFundBindModifyModel(object):

    def __init__(self):
        self._agreement_no = None
        self._expire_time = None
        self._out_bind_no = None
        self._redirect_url = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def out_bind_no(self):
        return self._out_bind_no

    @out_bind_no.setter
    def out_bind_no(self, value):
        self._out_bind_no = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.out_bind_no:
            if hasattr(self.out_bind_no, 'to_alipay_dict'):
                params['out_bind_no'] = self.out_bind_no.to_alipay_dict()
            else:
                params['out_bind_no'] = self.out_bind_no
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceFundBindModifyModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'out_bind_no' in d:
            o.out_bind_no = d['out_bind_no']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        return o



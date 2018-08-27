#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanApplyCreateModel(object):

    def __init__(self):
        self._apply_amt = None
        self._cert_no = None
        self._name = None
        self._out_biz_no = None
        self._ratio = None
        self._scene = None

    @property
    def apply_amt(self):
        return self._apply_amt

    @apply_amt.setter
    def apply_amt(self, value):
        self._apply_amt = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def ratio(self):
        return self._ratio

    @ratio.setter
    def ratio(self, value):
        self._ratio = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amt:
            if hasattr(self.apply_amt, 'to_alipay_dict'):
                params['apply_amt'] = self.apply_amt.to_alipay_dict()
            else:
                params['apply_amt'] = self.apply_amt
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.ratio:
            if hasattr(self.ratio, 'to_alipay_dict'):
                params['ratio'] = self.ratio.to_alipay_dict()
            else:
                params['ratio'] = self.ratio
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanApplyCreateModel()
        if 'apply_amt' in d:
            o.apply_amt = d['apply_amt']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'name' in d:
            o.name = d['name']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'ratio' in d:
            o.ratio = d['ratio']
        if 'scene' in d:
            o.scene = d['scene']
        return o



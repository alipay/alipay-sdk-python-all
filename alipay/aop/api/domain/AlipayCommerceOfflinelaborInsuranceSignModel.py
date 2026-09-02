#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOfflinelaborInsuranceSignModel(object):

    def __init__(self):
        self._mode = None
        self._out_biz_no = None
        self._social_unified_cert_no = None

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def social_unified_cert_no(self):
        return self._social_unified_cert_no

    @social_unified_cert_no.setter
    def social_unified_cert_no(self, value):
        self._social_unified_cert_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.social_unified_cert_no:
            if hasattr(self.social_unified_cert_no, 'to_alipay_dict'):
                params['social_unified_cert_no'] = self.social_unified_cert_no.to_alipay_dict()
            else:
                params['social_unified_cert_no'] = self.social_unified_cert_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOfflinelaborInsuranceSignModel()
        if 'mode' in d:
            o.mode = d['mode']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'social_unified_cert_no' in d:
            o.social_unified_cert_no = d['social_unified_cert_no']
        return o



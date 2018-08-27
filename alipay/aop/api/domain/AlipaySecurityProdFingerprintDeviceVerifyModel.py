#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdFingerprintDeviceVerifyModel(object):

    def __init__(self):
        self._ifaa_version = None
        self._ifaf_message = None
        self._out_biz_no = None

    @property
    def ifaa_version(self):
        return self._ifaa_version

    @ifaa_version.setter
    def ifaa_version(self, value):
        self._ifaa_version = value
    @property
    def ifaf_message(self):
        return self._ifaf_message

    @ifaf_message.setter
    def ifaf_message(self, value):
        self._ifaf_message = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ifaa_version:
            if hasattr(self.ifaa_version, 'to_alipay_dict'):
                params['ifaa_version'] = self.ifaa_version.to_alipay_dict()
            else:
                params['ifaa_version'] = self.ifaa_version
        if self.ifaf_message:
            if hasattr(self.ifaf_message, 'to_alipay_dict'):
                params['ifaf_message'] = self.ifaf_message.to_alipay_dict()
            else:
                params['ifaf_message'] = self.ifaf_message
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdFingerprintDeviceVerifyModel()
        if 'ifaa_version' in d:
            o.ifaa_version = d['ifaa_version']
        if 'ifaf_message' in d:
            o.ifaf_message = d['ifaf_message']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o



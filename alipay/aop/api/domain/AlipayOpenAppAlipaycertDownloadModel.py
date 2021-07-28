#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppAlipaycertDownloadModel(object):

    def __init__(self):
        self._alipay_cert_sn = None

    @property
    def alipay_cert_sn(self):
        return self._alipay_cert_sn

    @alipay_cert_sn.setter
    def alipay_cert_sn(self, value):
        self._alipay_cert_sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_cert_sn:
            if hasattr(self.alipay_cert_sn, 'to_alipay_dict'):
                params['alipay_cert_sn'] = self.alipay_cert_sn.to_alipay_dict()
            else:
                params['alipay_cert_sn'] = self.alipay_cert_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppAlipaycertDownloadModel()
        if 'alipay_cert_sn' in d:
            o.alipay_cert_sn = d['alipay_cert_sn']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcCertifiedQueryModel(object):

    def __init__(self):
        self._auth_agreement_no = None

    @property
    def auth_agreement_no(self):
        return self._auth_agreement_no

    @auth_agreement_no.setter
    def auth_agreement_no(self, value):
        self._auth_agreement_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_agreement_no:
            if hasattr(self.auth_agreement_no, 'to_alipay_dict'):
                params['auth_agreement_no'] = self.auth_agreement_no.to_alipay_dict()
            else:
                params['auth_agreement_no'] = self.auth_agreement_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcCertifiedQueryModel()
        if 'auth_agreement_no' in d:
            o.auth_agreement_no = d['auth_agreement_no']
        return o



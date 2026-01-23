#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationCarservicesaastldcAuthenticationQuerystatusModel(object):

    def __init__(self):
        self._auth_no = None

    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_no:
            if hasattr(self.auth_no, 'to_alipay_dict'):
                params['auth_no'] = self.auth_no.to_alipay_dict()
            else:
                params['auth_no'] = self.auth_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationCarservicesaastldcAuthenticationQuerystatusModel()
        if 'auth_no' in d:
            o.auth_no = d['auth_no']
        return o



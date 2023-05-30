#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsresourceUrquerybybusvcdomainQueryModel(object):

    def __init__(self):
        self._busvc_domain = None

    @property
    def busvc_domain(self):
        return self._busvc_domain

    @busvc_domain.setter
    def busvc_domain(self, value):
        self._busvc_domain = value


    def to_alipay_dict(self):
        params = dict()
        if self.busvc_domain:
            if hasattr(self.busvc_domain, 'to_alipay_dict'):
                params['busvc_domain'] = self.busvc_domain.to_alipay_dict()
            else:
                params['busvc_domain'] = self.busvc_domain
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIsresourceUrquerybybusvcdomainQueryModel()
        if 'busvc_domain' in d:
            o.busvc_domain = d['busvc_domain']
        return o



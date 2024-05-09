#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceItaskAvatarQuerytaskQueryModel(object):

    def __init__(self):
        self._ids = None
        self._tenant_code = None

    @property
    def ids(self):
        return self._ids

    @ids.setter
    def ids(self, value):
        if isinstance(value, list):
            self._ids = list()
            for i in value:
                self._ids.append(i)
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ids:
            if isinstance(self.ids, list):
                for i in range(0, len(self.ids)):
                    element = self.ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ids[i] = element.to_alipay_dict()
            if hasattr(self.ids, 'to_alipay_dict'):
                params['ids'] = self.ids.to_alipay_dict()
            else:
                params['ids'] = self.ids
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceItaskAvatarQuerytaskQueryModel()
        if 'ids' in d:
            o.ids = d['ids']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        return o



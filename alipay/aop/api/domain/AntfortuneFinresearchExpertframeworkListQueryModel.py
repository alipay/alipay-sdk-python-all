#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneFinresearchExpertframeworkListQueryModel(object):

    def __init__(self):
        self._tenant_id = None

    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneFinresearchExpertframeworkListQueryModel()
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o



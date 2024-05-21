#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneFinresearchSessionListQueryModel(object):

    def __init__(self):
        self._bu_unique_id = None
        self._tenant_id = None

    @property
    def bu_unique_id(self):
        return self._bu_unique_id

    @bu_unique_id.setter
    def bu_unique_id(self, value):
        self._bu_unique_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bu_unique_id:
            if hasattr(self.bu_unique_id, 'to_alipay_dict'):
                params['bu_unique_id'] = self.bu_unique_id.to_alipay_dict()
            else:
                params['bu_unique_id'] = self.bu_unique_id
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
        o = AntfortuneFinresearchSessionListQueryModel()
        if 'bu_unique_id' in d:
            o.bu_unique_id = d['bu_unique_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o



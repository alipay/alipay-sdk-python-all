#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneContentCommunityOpenSecuaiQueryModel(object):

    def __init__(self):
        self._biz_request = None
        self._biz_type = None
        self._tenant_id = None

    @property
    def biz_request(self):
        return self._biz_request

    @biz_request.setter
    def biz_request(self, value):
        self._biz_request = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_request:
            if hasattr(self.biz_request, 'to_alipay_dict'):
                params['biz_request'] = self.biz_request.to_alipay_dict()
            else:
                params['biz_request'] = self.biz_request
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
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
        o = AntfortuneContentCommunityOpenSecuaiQueryModel()
        if 'biz_request' in d:
            o.biz_request = d['biz_request']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o



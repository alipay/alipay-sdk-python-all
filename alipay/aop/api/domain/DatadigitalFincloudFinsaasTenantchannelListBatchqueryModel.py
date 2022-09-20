#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasTenantchannelListBatchqueryModel(object):

    def __init__(self):
        self._channel_category = None
        self._status = None
        self._tenant_code = None

    @property
    def channel_category(self):
        return self._channel_category

    @channel_category.setter
    def channel_category(self, value):
        self._channel_category = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_category:
            if hasattr(self.channel_category, 'to_alipay_dict'):
                params['channel_category'] = self.channel_category.to_alipay_dict()
            else:
                params['channel_category'] = self.channel_category
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = DatadigitalFincloudFinsaasTenantchannelListBatchqueryModel()
        if 'channel_category' in d:
            o.channel_category = d['channel_category']
        if 'status' in d:
            o.status = d['status']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        return o



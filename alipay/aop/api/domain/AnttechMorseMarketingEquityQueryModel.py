#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechMorseMarketingEquityQueryModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._resource_id = None
        self._send_type = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def send_type(self):
        return self._send_type

    @send_type.setter
    def send_type(self, value):
        self._send_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        if self.send_type:
            if hasattr(self.send_type, 'to_alipay_dict'):
                params['send_type'] = self.send_type.to_alipay_dict()
            else:
                params['send_type'] = self.send_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechMorseMarketingEquityQueryModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        if 'send_type' in d:
            o.send_type = d['send_type']
        return o



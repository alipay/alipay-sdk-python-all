#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApplySubAccountAndBindOrder(object):

    def __init__(self):
        self._inst_id = None
        self._ip_role_id = None
        self._out_biz_no = None
        self._source = None
        self._treasury_business_type = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def treasury_business_type(self):
        return self._treasury_business_type

    @treasury_business_type.setter
    def treasury_business_type(self, value):
        self._treasury_business_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.treasury_business_type:
            if hasattr(self.treasury_business_type, 'to_alipay_dict'):
                params['treasury_business_type'] = self.treasury_business_type.to_alipay_dict()
            else:
                params['treasury_business_type'] = self.treasury_business_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApplySubAccountAndBindOrder()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'source' in d:
            o.source = d['source']
        if 'treasury_business_type' in d:
            o.treasury_business_type = d['treasury_business_type']
        return o



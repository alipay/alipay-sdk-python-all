#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GFAOpenAPIQueryRequest(object):

    def __init__(self):
        self._acceptance_id = None
        self._biz_ev_code = None
        self._out_business_no = None
        self._service_type = None
        self._sub_out_business_no = None
        self._use_biz_ev_code = None
        self._use_sub_out_business_no = None

    @property
    def acceptance_id(self):
        return self._acceptance_id

    @acceptance_id.setter
    def acceptance_id(self, value):
        self._acceptance_id = value
    @property
    def biz_ev_code(self):
        return self._biz_ev_code

    @biz_ev_code.setter
    def biz_ev_code(self, value):
        self._biz_ev_code = value
    @property
    def out_business_no(self):
        return self._out_business_no

    @out_business_no.setter
    def out_business_no(self, value):
        self._out_business_no = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def sub_out_business_no(self):
        return self._sub_out_business_no

    @sub_out_business_no.setter
    def sub_out_business_no(self, value):
        self._sub_out_business_no = value
    @property
    def use_biz_ev_code(self):
        return self._use_biz_ev_code

    @use_biz_ev_code.setter
    def use_biz_ev_code(self, value):
        self._use_biz_ev_code = value
    @property
    def use_sub_out_business_no(self):
        return self._use_sub_out_business_no

    @use_sub_out_business_no.setter
    def use_sub_out_business_no(self, value):
        self._use_sub_out_business_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.acceptance_id:
            if hasattr(self.acceptance_id, 'to_alipay_dict'):
                params['acceptance_id'] = self.acceptance_id.to_alipay_dict()
            else:
                params['acceptance_id'] = self.acceptance_id
        if self.biz_ev_code:
            if hasattr(self.biz_ev_code, 'to_alipay_dict'):
                params['biz_ev_code'] = self.biz_ev_code.to_alipay_dict()
            else:
                params['biz_ev_code'] = self.biz_ev_code
        if self.out_business_no:
            if hasattr(self.out_business_no, 'to_alipay_dict'):
                params['out_business_no'] = self.out_business_no.to_alipay_dict()
            else:
                params['out_business_no'] = self.out_business_no
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.sub_out_business_no:
            if hasattr(self.sub_out_business_no, 'to_alipay_dict'):
                params['sub_out_business_no'] = self.sub_out_business_no.to_alipay_dict()
            else:
                params['sub_out_business_no'] = self.sub_out_business_no
        if self.use_biz_ev_code:
            if hasattr(self.use_biz_ev_code, 'to_alipay_dict'):
                params['use_biz_ev_code'] = self.use_biz_ev_code.to_alipay_dict()
            else:
                params['use_biz_ev_code'] = self.use_biz_ev_code
        if self.use_sub_out_business_no:
            if hasattr(self.use_sub_out_business_no, 'to_alipay_dict'):
                params['use_sub_out_business_no'] = self.use_sub_out_business_no.to_alipay_dict()
            else:
                params['use_sub_out_business_no'] = self.use_sub_out_business_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GFAOpenAPIQueryRequest()
        if 'acceptance_id' in d:
            o.acceptance_id = d['acceptance_id']
        if 'biz_ev_code' in d:
            o.biz_ev_code = d['biz_ev_code']
        if 'out_business_no' in d:
            o.out_business_no = d['out_business_no']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'sub_out_business_no' in d:
            o.sub_out_business_no = d['sub_out_business_no']
        if 'use_biz_ev_code' in d:
            o.use_biz_ev_code = d['use_biz_ev_code']
        if 'use_sub_out_business_no' in d:
            o.use_sub_out_business_no = d['use_sub_out_business_no']
        return o



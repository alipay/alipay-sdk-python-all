#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskAmlAnalyzeSubmitModel(object):

    def __init__(self):
        self._biz_code = None
        self._extend_data = None
        self._gmt_occur = None
        self._request_id = None
        self._tenant_id = None
        self._tnt_inst_id = None
        self._trace_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def extend_data(self):
        return self._extend_data

    @extend_data.setter
    def extend_data(self, value):
        self._extend_data = value
    @property
    def gmt_occur(self):
        return self._gmt_occur

    @gmt_occur.setter
    def gmt_occur(self, value):
        self._gmt_occur = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.extend_data:
            if hasattr(self.extend_data, 'to_alipay_dict'):
                params['extend_data'] = self.extend_data.to_alipay_dict()
            else:
                params['extend_data'] = self.extend_data
        if self.gmt_occur:
            if hasattr(self.gmt_occur, 'to_alipay_dict'):
                params['gmt_occur'] = self.gmt_occur.to_alipay_dict()
            else:
                params['gmt_occur'] = self.gmt_occur
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskAmlAnalyzeSubmitModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'extend_data' in d:
            o.extend_data = d['extend_data']
        if 'gmt_occur' in d:
            o.gmt_occur = d['gmt_occur']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o



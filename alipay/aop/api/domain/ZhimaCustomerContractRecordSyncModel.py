#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerContractRecordSyncModel(object):

    def __init__(self):
        self._biz_no = None
        self._biz_time = None
        self._biz_type = None
        self._contract_no = None
        self._record_content = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def record_content(self):
        return self._record_content

    @record_content.setter
    def record_content(self, value):
        self._record_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.record_content:
            if hasattr(self.record_content, 'to_alipay_dict'):
                params['record_content'] = self.record_content.to_alipay_dict()
            else:
                params['record_content'] = self.record_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerContractRecordSyncModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'record_content' in d:
            o.record_content = d['record_content']
        return o



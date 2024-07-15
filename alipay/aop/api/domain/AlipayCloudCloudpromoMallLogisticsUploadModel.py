#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoMallLogisticsUploadModel(object):

    def __init__(self):
        self._cp_code = None
        self._dispute_id = None
        self._logistics_no = None

    @property
    def cp_code(self):
        return self._cp_code

    @cp_code.setter
    def cp_code(self, value):
        self._cp_code = value
    @property
    def dispute_id(self):
        return self._dispute_id

    @dispute_id.setter
    def dispute_id(self, value):
        self._dispute_id = value
    @property
    def logistics_no(self):
        return self._logistics_no

    @logistics_no.setter
    def logistics_no(self, value):
        self._logistics_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cp_code:
            if hasattr(self.cp_code, 'to_alipay_dict'):
                params['cp_code'] = self.cp_code.to_alipay_dict()
            else:
                params['cp_code'] = self.cp_code
        if self.dispute_id:
            if hasattr(self.dispute_id, 'to_alipay_dict'):
                params['dispute_id'] = self.dispute_id.to_alipay_dict()
            else:
                params['dispute_id'] = self.dispute_id
        if self.logistics_no:
            if hasattr(self.logistics_no, 'to_alipay_dict'):
                params['logistics_no'] = self.logistics_no.to_alipay_dict()
            else:
                params['logistics_no'] = self.logistics_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMallLogisticsUploadModel()
        if 'cp_code' in d:
            o.cp_code = d['cp_code']
        if 'dispute_id' in d:
            o.dispute_id = d['dispute_id']
        if 'logistics_no' in d:
            o.logistics_no = d['logistics_no']
        return o



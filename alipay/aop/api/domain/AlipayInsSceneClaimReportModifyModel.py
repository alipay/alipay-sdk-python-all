#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneClaimReportModifyModel(object):

    def __init__(self):
        self._accident_address = None
        self._accident_desc = None
        self._accident_time = None
        self._biz_data = None
        self._claim_report_no = None

    @property
    def accident_address(self):
        return self._accident_address

    @accident_address.setter
    def accident_address(self, value):
        self._accident_address = value
    @property
    def accident_desc(self):
        return self._accident_desc

    @accident_desc.setter
    def accident_desc(self, value):
        self._accident_desc = value
    @property
    def accident_time(self):
        return self._accident_time

    @accident_time.setter
    def accident_time(self, value):
        self._accident_time = value
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def claim_report_no(self):
        return self._claim_report_no

    @claim_report_no.setter
    def claim_report_no(self, value):
        self._claim_report_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.accident_address:
            if hasattr(self.accident_address, 'to_alipay_dict'):
                params['accident_address'] = self.accident_address.to_alipay_dict()
            else:
                params['accident_address'] = self.accident_address
        if self.accident_desc:
            if hasattr(self.accident_desc, 'to_alipay_dict'):
                params['accident_desc'] = self.accident_desc.to_alipay_dict()
            else:
                params['accident_desc'] = self.accident_desc
        if self.accident_time:
            if hasattr(self.accident_time, 'to_alipay_dict'):
                params['accident_time'] = self.accident_time.to_alipay_dict()
            else:
                params['accident_time'] = self.accident_time
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.claim_report_no:
            if hasattr(self.claim_report_no, 'to_alipay_dict'):
                params['claim_report_no'] = self.claim_report_no.to_alipay_dict()
            else:
                params['claim_report_no'] = self.claim_report_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneClaimReportModifyModel()
        if 'accident_address' in d:
            o.accident_address = d['accident_address']
        if 'accident_desc' in d:
            o.accident_desc = d['accident_desc']
        if 'accident_time' in d:
            o.accident_time = d['accident_time']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'claim_report_no' in d:
            o.claim_report_no = d['claim_report_no']
        return o



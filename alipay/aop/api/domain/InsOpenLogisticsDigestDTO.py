#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOpenLogisticsDigestDTO(object):

    def __init__(self):
        self._logistics_company_name = None
        self._logistics_no = None
        self._logistics_status = None

    @property
    def logistics_company_name(self):
        return self._logistics_company_name

    @logistics_company_name.setter
    def logistics_company_name(self, value):
        self._logistics_company_name = value
    @property
    def logistics_no(self):
        return self._logistics_no

    @logistics_no.setter
    def logistics_no(self, value):
        self._logistics_no = value
    @property
    def logistics_status(self):
        return self._logistics_status

    @logistics_status.setter
    def logistics_status(self, value):
        self._logistics_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_company_name:
            if hasattr(self.logistics_company_name, 'to_alipay_dict'):
                params['logistics_company_name'] = self.logistics_company_name.to_alipay_dict()
            else:
                params['logistics_company_name'] = self.logistics_company_name
        if self.logistics_no:
            if hasattr(self.logistics_no, 'to_alipay_dict'):
                params['logistics_no'] = self.logistics_no.to_alipay_dict()
            else:
                params['logistics_no'] = self.logistics_no
        if self.logistics_status:
            if hasattr(self.logistics_status, 'to_alipay_dict'):
                params['logistics_status'] = self.logistics_status.to_alipay_dict()
            else:
                params['logistics_status'] = self.logistics_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsOpenLogisticsDigestDTO()
        if 'logistics_company_name' in d:
            o.logistics_company_name = d['logistics_company_name']
        if 'logistics_no' in d:
            o.logistics_no = d['logistics_no']
        if 'logistics_status' in d:
            o.logistics_status = d['logistics_status']
        return o



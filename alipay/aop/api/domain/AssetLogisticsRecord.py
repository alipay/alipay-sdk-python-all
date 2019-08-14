#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetLogisticsRecord(object):

    def __init__(self):
        self._last_logistics_detail = None
        self._logistics_code = None
        self._logistics_gmt_modified = None
        self._logistics_no = None
        self._logistics_status = None
        self._logistics_status_desc = None

    @property
    def last_logistics_detail(self):
        return self._last_logistics_detail

    @last_logistics_detail.setter
    def last_logistics_detail(self, value):
        self._last_logistics_detail = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def logistics_gmt_modified(self):
        return self._logistics_gmt_modified

    @logistics_gmt_modified.setter
    def logistics_gmt_modified(self, value):
        self._logistics_gmt_modified = value
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
    @property
    def logistics_status_desc(self):
        return self._logistics_status_desc

    @logistics_status_desc.setter
    def logistics_status_desc(self, value):
        self._logistics_status_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.last_logistics_detail:
            if hasattr(self.last_logistics_detail, 'to_alipay_dict'):
                params['last_logistics_detail'] = self.last_logistics_detail.to_alipay_dict()
            else:
                params['last_logistics_detail'] = self.last_logistics_detail
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.logistics_gmt_modified:
            if hasattr(self.logistics_gmt_modified, 'to_alipay_dict'):
                params['logistics_gmt_modified'] = self.logistics_gmt_modified.to_alipay_dict()
            else:
                params['logistics_gmt_modified'] = self.logistics_gmt_modified
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
        if self.logistics_status_desc:
            if hasattr(self.logistics_status_desc, 'to_alipay_dict'):
                params['logistics_status_desc'] = self.logistics_status_desc.to_alipay_dict()
            else:
                params['logistics_status_desc'] = self.logistics_status_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetLogisticsRecord()
        if 'last_logistics_detail' in d:
            o.last_logistics_detail = d['last_logistics_detail']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'logistics_gmt_modified' in d:
            o.logistics_gmt_modified = d['logistics_gmt_modified']
        if 'logistics_no' in d:
            o.logistics_no = d['logistics_no']
        if 'logistics_status' in d:
            o.logistics_status = d['logistics_status']
        if 'logistics_status_desc' in d:
            o.logistics_status_desc = d['logistics_status_desc']
        return o



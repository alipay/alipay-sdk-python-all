#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderLogisticsInformation(object):

    def __init__(self):
        self._detail = None
        self._express_company = None
        self._has_matched = None
        self._status = None
        self._status_desc = None
        self._tracking_no = None

    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value
    @property
    def express_company(self):
        return self._express_company

    @express_company.setter
    def express_company(self, value):
        self._express_company = value
    @property
    def has_matched(self):
        return self._has_matched

    @has_matched.setter
    def has_matched(self, value):
        self._has_matched = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value
    @property
    def tracking_no(self):
        return self._tracking_no

    @tracking_no.setter
    def tracking_no(self, value):
        self._tracking_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.detail:
            if hasattr(self.detail, 'to_alipay_dict'):
                params['detail'] = self.detail.to_alipay_dict()
            else:
                params['detail'] = self.detail
        if self.express_company:
            if hasattr(self.express_company, 'to_alipay_dict'):
                params['express_company'] = self.express_company.to_alipay_dict()
            else:
                params['express_company'] = self.express_company
        if self.has_matched:
            if hasattr(self.has_matched, 'to_alipay_dict'):
                params['has_matched'] = self.has_matched.to_alipay_dict()
            else:
                params['has_matched'] = self.has_matched
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_desc:
            if hasattr(self.status_desc, 'to_alipay_dict'):
                params['status_desc'] = self.status_desc.to_alipay_dict()
            else:
                params['status_desc'] = self.status_desc
        if self.tracking_no:
            if hasattr(self.tracking_no, 'to_alipay_dict'):
                params['tracking_no'] = self.tracking_no.to_alipay_dict()
            else:
                params['tracking_no'] = self.tracking_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderLogisticsInformation()
        if 'detail' in d:
            o.detail = d['detail']
        if 'express_company' in d:
            o.express_company = d['express_company']
        if 'has_matched' in d:
            o.has_matched = d['has_matched']
        if 'status' in d:
            o.status = d['status']
        if 'status_desc' in d:
            o.status_desc = d['status_desc']
        if 'tracking_no' in d:
            o.tracking_no = d['tracking_no']
        return o



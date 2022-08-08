#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasDesignPageBatchqueryModel(object):

    def __init__(self):
        self._creator_name = None
        self._page_name = None
        self._page_num = None
        self._page_size = None
        self._status = None
        self._tenant_code = None

    @property
    def creator_name(self):
        return self._creator_name

    @creator_name.setter
    def creator_name(self, value):
        self._creator_name = value
    @property
    def page_name(self):
        return self._page_name

    @page_name.setter
    def page_name(self, value):
        self._page_name = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.creator_name:
            if hasattr(self.creator_name, 'to_alipay_dict'):
                params['creator_name'] = self.creator_name.to_alipay_dict()
            else:
                params['creator_name'] = self.creator_name
        if self.page_name:
            if hasattr(self.page_name, 'to_alipay_dict'):
                params['page_name'] = self.page_name.to_alipay_dict()
            else:
                params['page_name'] = self.page_name
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasDesignPageBatchqueryModel()
        if 'creator_name' in d:
            o.creator_name = d['creator_name']
        if 'page_name' in d:
            o.page_name = d['page_name']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'status' in d:
            o.status = d['status']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        return o



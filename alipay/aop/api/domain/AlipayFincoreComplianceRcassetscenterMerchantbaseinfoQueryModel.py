#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceRcassetscenterMerchantbaseinfoQueryModel(object):

    def __init__(self):
        self._corp_name = None
        self._org_id = None
        self._page = None
        self._page_size = None
        self._source = None
        self._unified_social_credit_code = None

    @property
    def corp_name(self):
        return self._corp_name

    @corp_name.setter
    def corp_name(self, value):
        self._corp_name = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def unified_social_credit_code(self):
        return self._unified_social_credit_code

    @unified_social_credit_code.setter
    def unified_social_credit_code(self, value):
        self._unified_social_credit_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.corp_name:
            if hasattr(self.corp_name, 'to_alipay_dict'):
                params['corp_name'] = self.corp_name.to_alipay_dict()
            else:
                params['corp_name'] = self.corp_name
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.unified_social_credit_code:
            if hasattr(self.unified_social_credit_code, 'to_alipay_dict'):
                params['unified_social_credit_code'] = self.unified_social_credit_code.to_alipay_dict()
            else:
                params['unified_social_credit_code'] = self.unified_social_credit_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceRcassetscenterMerchantbaseinfoQueryModel()
        if 'corp_name' in d:
            o.corp_name = d['corp_name']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'page' in d:
            o.page = d['page']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'source' in d:
            o.source = d['source']
        if 'unified_social_credit_code' in d:
            o.unified_social_credit_code = d['unified_social_credit_code']
        return o



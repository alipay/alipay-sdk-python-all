#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpAssistantCustomerRecommendModel(object):

    def __init__(self):
        self._category_lv_2_name = None
        self._channel_code = None
        self._parterner_id = None
        self._prompt = None
        self._request_id = None
        self._size = None
        self._source_company_crn = None
        self._source_company_name = None
        self._tenant = None

    @property
    def category_lv_2_name(self):
        return self._category_lv_2_name

    @category_lv_2_name.setter
    def category_lv_2_name(self, value):
        self._category_lv_2_name = value
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def parterner_id(self):
        return self._parterner_id

    @parterner_id.setter
    def parterner_id(self, value):
        self._parterner_id = value
    @property
    def prompt(self):
        return self._prompt

    @prompt.setter
    def prompt(self, value):
        self._prompt = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def source_company_crn(self):
        return self._source_company_crn

    @source_company_crn.setter
    def source_company_crn(self, value):
        self._source_company_crn = value
    @property
    def source_company_name(self):
        return self._source_company_name

    @source_company_name.setter
    def source_company_name(self, value):
        self._source_company_name = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_lv_2_name:
            if hasattr(self.category_lv_2_name, 'to_alipay_dict'):
                params['category_lv_2_name'] = self.category_lv_2_name.to_alipay_dict()
            else:
                params['category_lv_2_name'] = self.category_lv_2_name
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.parterner_id:
            if hasattr(self.parterner_id, 'to_alipay_dict'):
                params['parterner_id'] = self.parterner_id.to_alipay_dict()
            else:
                params['parterner_id'] = self.parterner_id
        if self.prompt:
            if hasattr(self.prompt, 'to_alipay_dict'):
                params['prompt'] = self.prompt.to_alipay_dict()
            else:
                params['prompt'] = self.prompt
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.source_company_crn:
            if hasattr(self.source_company_crn, 'to_alipay_dict'):
                params['source_company_crn'] = self.source_company_crn.to_alipay_dict()
            else:
                params['source_company_crn'] = self.source_company_crn
        if self.source_company_name:
            if hasattr(self.source_company_name, 'to_alipay_dict'):
                params['source_company_name'] = self.source_company_name.to_alipay_dict()
            else:
                params['source_company_name'] = self.source_company_name
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAssistantCustomerRecommendModel()
        if 'category_lv_2_name' in d:
            o.category_lv_2_name = d['category_lv_2_name']
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'parterner_id' in d:
            o.parterner_id = d['parterner_id']
        if 'prompt' in d:
            o.prompt = d['prompt']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'size' in d:
            o.size = d['size']
        if 'source_company_crn' in d:
            o.source_company_crn = d['source_company_crn']
        if 'source_company_name' in d:
            o.source_company_name = d['source_company_name']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o



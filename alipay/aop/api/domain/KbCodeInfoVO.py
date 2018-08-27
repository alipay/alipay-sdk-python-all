#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbCodeInfoVO(object):

    def __init__(self):
        self._batch_id = None
        self._code_url = None
        self._create_time = None
        self._qr_code = None
        self._resource_url = None
        self._shop_id = None
        self._shop_name = None
        self._stuff_template = None
        self._stuff_template_desc = None
        self._stuff_type_desc = None
        self._table_no = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def code_url(self):
        return self._code_url

    @code_url.setter
    def code_url(self, value):
        self._code_url = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def resource_url(self):
        return self._resource_url

    @resource_url.setter
    def resource_url(self, value):
        self._resource_url = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def stuff_template(self):
        return self._stuff_template

    @stuff_template.setter
    def stuff_template(self, value):
        self._stuff_template = value
    @property
    def stuff_template_desc(self):
        return self._stuff_template_desc

    @stuff_template_desc.setter
    def stuff_template_desc(self, value):
        self._stuff_template_desc = value
    @property
    def stuff_type_desc(self):
        return self._stuff_type_desc

    @stuff_type_desc.setter
    def stuff_type_desc(self, value):
        self._stuff_type_desc = value
    @property
    def table_no(self):
        return self._table_no

    @table_no.setter
    def table_no(self, value):
        self._table_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.code_url:
            if hasattr(self.code_url, 'to_alipay_dict'):
                params['code_url'] = self.code_url.to_alipay_dict()
            else:
                params['code_url'] = self.code_url
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.qr_code:
            if hasattr(self.qr_code, 'to_alipay_dict'):
                params['qr_code'] = self.qr_code.to_alipay_dict()
            else:
                params['qr_code'] = self.qr_code
        if self.resource_url:
            if hasattr(self.resource_url, 'to_alipay_dict'):
                params['resource_url'] = self.resource_url.to_alipay_dict()
            else:
                params['resource_url'] = self.resource_url
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.stuff_template:
            if hasattr(self.stuff_template, 'to_alipay_dict'):
                params['stuff_template'] = self.stuff_template.to_alipay_dict()
            else:
                params['stuff_template'] = self.stuff_template
        if self.stuff_template_desc:
            if hasattr(self.stuff_template_desc, 'to_alipay_dict'):
                params['stuff_template_desc'] = self.stuff_template_desc.to_alipay_dict()
            else:
                params['stuff_template_desc'] = self.stuff_template_desc
        if self.stuff_type_desc:
            if hasattr(self.stuff_type_desc, 'to_alipay_dict'):
                params['stuff_type_desc'] = self.stuff_type_desc.to_alipay_dict()
            else:
                params['stuff_type_desc'] = self.stuff_type_desc
        if self.table_no:
            if hasattr(self.table_no, 'to_alipay_dict'):
                params['table_no'] = self.table_no.to_alipay_dict()
            else:
                params['table_no'] = self.table_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbCodeInfoVO()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'code_url' in d:
            o.code_url = d['code_url']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'qr_code' in d:
            o.qr_code = d['qr_code']
        if 'resource_url' in d:
            o.resource_url = d['resource_url']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'stuff_template' in d:
            o.stuff_template = d['stuff_template']
        if 'stuff_template_desc' in d:
            o.stuff_template_desc = d['stuff_template_desc']
        if 'stuff_type_desc' in d:
            o.stuff_type_desc = d['stuff_type_desc']
        if 'table_no' in d:
            o.table_no = d['table_no']
        return o



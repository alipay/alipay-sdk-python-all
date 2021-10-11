#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppServiceApplyModel(object):

    def __init__(self):
        self._category_id = None
        self._out_biz_no = None
        self._schema_version = None
        self._service_code = None
        self._service_xml = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def schema_version(self):
        return self._schema_version

    @schema_version.setter
    def schema_version(self, value):
        self._schema_version = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_xml(self):
        return self._service_xml

    @service_xml.setter
    def service_xml(self, value):
        self._service_xml = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.schema_version:
            if hasattr(self.schema_version, 'to_alipay_dict'):
                params['schema_version'] = self.schema_version.to_alipay_dict()
            else:
                params['schema_version'] = self.schema_version
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_xml:
            if hasattr(self.service_xml, 'to_alipay_dict'):
                params['service_xml'] = self.service_xml.to_alipay_dict()
            else:
                params['service_xml'] = self.service_xml
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppServiceApplyModel()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'schema_version' in d:
            o.schema_version = d['schema_version']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_xml' in d:
            o.service_xml = d['service_xml']
        return o



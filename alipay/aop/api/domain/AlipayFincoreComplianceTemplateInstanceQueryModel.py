#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceTemplateInstanceQueryModel(object):

    def __init__(self):
        self._biz_business_id = None
        self._biz_instance_id = None
        self._need_pdf_file = None
        self._source_system_id = None
        self._tenant = None

    @property
    def biz_business_id(self):
        return self._biz_business_id

    @biz_business_id.setter
    def biz_business_id(self, value):
        self._biz_business_id = value
    @property
    def biz_instance_id(self):
        return self._biz_instance_id

    @biz_instance_id.setter
    def biz_instance_id(self, value):
        self._biz_instance_id = value
    @property
    def need_pdf_file(self):
        return self._need_pdf_file

    @need_pdf_file.setter
    def need_pdf_file(self, value):
        self._need_pdf_file = value
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_business_id:
            if hasattr(self.biz_business_id, 'to_alipay_dict'):
                params['biz_business_id'] = self.biz_business_id.to_alipay_dict()
            else:
                params['biz_business_id'] = self.biz_business_id
        if self.biz_instance_id:
            if hasattr(self.biz_instance_id, 'to_alipay_dict'):
                params['biz_instance_id'] = self.biz_instance_id.to_alipay_dict()
            else:
                params['biz_instance_id'] = self.biz_instance_id
        if self.need_pdf_file:
            if hasattr(self.need_pdf_file, 'to_alipay_dict'):
                params['need_pdf_file'] = self.need_pdf_file.to_alipay_dict()
            else:
                params['need_pdf_file'] = self.need_pdf_file
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
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
        o = AlipayFincoreComplianceTemplateInstanceQueryModel()
        if 'biz_business_id' in d:
            o.biz_business_id = d['biz_business_id']
        if 'biz_instance_id' in d:
            o.biz_instance_id = d['biz_instance_id']
        if 'need_pdf_file' in d:
            o.need_pdf_file = d['need_pdf_file']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o



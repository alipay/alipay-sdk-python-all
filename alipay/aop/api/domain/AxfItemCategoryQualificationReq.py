#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AxfItemCategoryQualificationReq(object):

    def __init__(self):
        self._attachment_ids = None
        self._legal_cert_no = None
        self._legal_name = None
        self._org_cert_no = None
        self._qualification_content = None
        self._qualification_type = None

    @property
    def attachment_ids(self):
        return self._attachment_ids

    @attachment_ids.setter
    def attachment_ids(self, value):
        if isinstance(value, list):
            self._attachment_ids = list()
            for i in value:
                self._attachment_ids.append(i)
    @property
    def legal_cert_no(self):
        return self._legal_cert_no

    @legal_cert_no.setter
    def legal_cert_no(self, value):
        self._legal_cert_no = value
    @property
    def legal_name(self):
        return self._legal_name

    @legal_name.setter
    def legal_name(self, value):
        self._legal_name = value
    @property
    def org_cert_no(self):
        return self._org_cert_no

    @org_cert_no.setter
    def org_cert_no(self, value):
        self._org_cert_no = value
    @property
    def qualification_content(self):
        return self._qualification_content

    @qualification_content.setter
    def qualification_content(self, value):
        self._qualification_content = value
    @property
    def qualification_type(self):
        return self._qualification_type

    @qualification_type.setter
    def qualification_type(self, value):
        self._qualification_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_ids:
            if isinstance(self.attachment_ids, list):
                for i in range(0, len(self.attachment_ids)):
                    element = self.attachment_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachment_ids[i] = element.to_alipay_dict()
            if hasattr(self.attachment_ids, 'to_alipay_dict'):
                params['attachment_ids'] = self.attachment_ids.to_alipay_dict()
            else:
                params['attachment_ids'] = self.attachment_ids
        if self.legal_cert_no:
            if hasattr(self.legal_cert_no, 'to_alipay_dict'):
                params['legal_cert_no'] = self.legal_cert_no.to_alipay_dict()
            else:
                params['legal_cert_no'] = self.legal_cert_no
        if self.legal_name:
            if hasattr(self.legal_name, 'to_alipay_dict'):
                params['legal_name'] = self.legal_name.to_alipay_dict()
            else:
                params['legal_name'] = self.legal_name
        if self.org_cert_no:
            if hasattr(self.org_cert_no, 'to_alipay_dict'):
                params['org_cert_no'] = self.org_cert_no.to_alipay_dict()
            else:
                params['org_cert_no'] = self.org_cert_no
        if self.qualification_content:
            if hasattr(self.qualification_content, 'to_alipay_dict'):
                params['qualification_content'] = self.qualification_content.to_alipay_dict()
            else:
                params['qualification_content'] = self.qualification_content
        if self.qualification_type:
            if hasattr(self.qualification_type, 'to_alipay_dict'):
                params['qualification_type'] = self.qualification_type.to_alipay_dict()
            else:
                params['qualification_type'] = self.qualification_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AxfItemCategoryQualificationReq()
        if 'attachment_ids' in d:
            o.attachment_ids = d['attachment_ids']
        if 'legal_cert_no' in d:
            o.legal_cert_no = d['legal_cert_no']
        if 'legal_name' in d:
            o.legal_name = d['legal_name']
        if 'org_cert_no' in d:
            o.org_cert_no = d['org_cert_no']
        if 'qualification_content' in d:
            o.qualification_content = d['qualification_content']
        if 'qualification_type' in d:
            o.qualification_type = d['qualification_type']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderModifyEnterpriseInfoOpenApiVO(object):

    def __init__(self):
        self._enterprise_license_image_url = None
        self._enterprise_name = None
        self._legal_person_cert_no = None
        self._legal_person_emblem_cert_image_url = None
        self._legal_person_name = None
        self._unified_social_credit_code = None

    @property
    def enterprise_license_image_url(self):
        return self._enterprise_license_image_url

    @enterprise_license_image_url.setter
    def enterprise_license_image_url(self, value):
        self._enterprise_license_image_url = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def legal_person_cert_no(self):
        return self._legal_person_cert_no

    @legal_person_cert_no.setter
    def legal_person_cert_no(self, value):
        self._legal_person_cert_no = value
    @property
    def legal_person_emblem_cert_image_url(self):
        return self._legal_person_emblem_cert_image_url

    @legal_person_emblem_cert_image_url.setter
    def legal_person_emblem_cert_image_url(self, value):
        self._legal_person_emblem_cert_image_url = value
    @property
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def unified_social_credit_code(self):
        return self._unified_social_credit_code

    @unified_social_credit_code.setter
    def unified_social_credit_code(self, value):
        self._unified_social_credit_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_license_image_url:
            if hasattr(self.enterprise_license_image_url, 'to_alipay_dict'):
                params['enterprise_license_image_url'] = self.enterprise_license_image_url.to_alipay_dict()
            else:
                params['enterprise_license_image_url'] = self.enterprise_license_image_url
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.legal_person_cert_no:
            if hasattr(self.legal_person_cert_no, 'to_alipay_dict'):
                params['legal_person_cert_no'] = self.legal_person_cert_no.to_alipay_dict()
            else:
                params['legal_person_cert_no'] = self.legal_person_cert_no
        if self.legal_person_emblem_cert_image_url:
            if hasattr(self.legal_person_emblem_cert_image_url, 'to_alipay_dict'):
                params['legal_person_emblem_cert_image_url'] = self.legal_person_emblem_cert_image_url.to_alipay_dict()
            else:
                params['legal_person_emblem_cert_image_url'] = self.legal_person_emblem_cert_image_url
        if self.legal_person_name:
            if hasattr(self.legal_person_name, 'to_alipay_dict'):
                params['legal_person_name'] = self.legal_person_name.to_alipay_dict()
            else:
                params['legal_person_name'] = self.legal_person_name
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
        o = OrderModifyEnterpriseInfoOpenApiVO()
        if 'enterprise_license_image_url' in d:
            o.enterprise_license_image_url = d['enterprise_license_image_url']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'legal_person_cert_no' in d:
            o.legal_person_cert_no = d['legal_person_cert_no']
        if 'legal_person_emblem_cert_image_url' in d:
            o.legal_person_emblem_cert_image_url = d['legal_person_emblem_cert_image_url']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        if 'unified_social_credit_code' in d:
            o.unified_social_credit_code = d['unified_social_credit_code']
        return o



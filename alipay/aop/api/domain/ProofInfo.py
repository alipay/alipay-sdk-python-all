#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProofInfo(object):

    def __init__(self):
        self._fund_proofs_url = None
        self._fund_type = None
        self._legal_cert_image = None
        self._legal_cert_image_back = None
        self._org_cert_image = None

    @property
    def fund_proofs_url(self):
        return self._fund_proofs_url

    @fund_proofs_url.setter
    def fund_proofs_url(self, value):
        if isinstance(value, list):
            self._fund_proofs_url = list()
            for i in value:
                self._fund_proofs_url.append(i)
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def legal_cert_image(self):
        return self._legal_cert_image

    @legal_cert_image.setter
    def legal_cert_image(self, value):
        self._legal_cert_image = value
    @property
    def legal_cert_image_back(self):
        return self._legal_cert_image_back

    @legal_cert_image_back.setter
    def legal_cert_image_back(self, value):
        self._legal_cert_image_back = value
    @property
    def org_cert_image(self):
        return self._org_cert_image

    @org_cert_image.setter
    def org_cert_image(self, value):
        self._org_cert_image = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_proofs_url:
            if isinstance(self.fund_proofs_url, list):
                for i in range(0, len(self.fund_proofs_url)):
                    element = self.fund_proofs_url[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_proofs_url[i] = element.to_alipay_dict()
            if hasattr(self.fund_proofs_url, 'to_alipay_dict'):
                params['fund_proofs_url'] = self.fund_proofs_url.to_alipay_dict()
            else:
                params['fund_proofs_url'] = self.fund_proofs_url
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        if self.legal_cert_image:
            if hasattr(self.legal_cert_image, 'to_alipay_dict'):
                params['legal_cert_image'] = self.legal_cert_image.to_alipay_dict()
            else:
                params['legal_cert_image'] = self.legal_cert_image
        if self.legal_cert_image_back:
            if hasattr(self.legal_cert_image_back, 'to_alipay_dict'):
                params['legal_cert_image_back'] = self.legal_cert_image_back.to_alipay_dict()
            else:
                params['legal_cert_image_back'] = self.legal_cert_image_back
        if self.org_cert_image:
            if hasattr(self.org_cert_image, 'to_alipay_dict'):
                params['org_cert_image'] = self.org_cert_image.to_alipay_dict()
            else:
                params['org_cert_image'] = self.org_cert_image
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProofInfo()
        if 'fund_proofs_url' in d:
            o.fund_proofs_url = d['fund_proofs_url']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'legal_cert_image' in d:
            o.legal_cert_image = d['legal_cert_image']
        if 'legal_cert_image_back' in d:
            o.legal_cert_image_back = d['legal_cert_image_back']
        if 'org_cert_image' in d:
            o.org_cert_image = d['org_cert_image']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsCreateCertificateRequest import InsCreateCertificateRequest


class AlipayInsMarketingCertificateBatchcreateModel(object):

    def __init__(self):
        self._ins_create_certificate_requests = None

    @property
    def ins_create_certificate_requests(self):
        return self._ins_create_certificate_requests

    @ins_create_certificate_requests.setter
    def ins_create_certificate_requests(self, value):
        if isinstance(value, list):
            self._ins_create_certificate_requests = list()
            for i in value:
                if isinstance(i, InsCreateCertificateRequest):
                    self._ins_create_certificate_requests.append(i)
                else:
                    self._ins_create_certificate_requests.append(InsCreateCertificateRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ins_create_certificate_requests:
            if isinstance(self.ins_create_certificate_requests, list):
                for i in range(0, len(self.ins_create_certificate_requests)):
                    element = self.ins_create_certificate_requests[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ins_create_certificate_requests[i] = element.to_alipay_dict()
            if hasattr(self.ins_create_certificate_requests, 'to_alipay_dict'):
                params['ins_create_certificate_requests'] = self.ins_create_certificate_requests.to_alipay_dict()
            else:
                params['ins_create_certificate_requests'] = self.ins_create_certificate_requests
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsMarketingCertificateBatchcreateModel()
        if 'ins_create_certificate_requests' in d:
            o.ins_create_certificate_requests = d['ins_create_certificate_requests']
        return o



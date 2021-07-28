#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CertificateInfo import CertificateInfo


class AlipayEcoCityserviceIndustrymsgAuthBatchqueryModel(object):

    def __init__(self):
        self._certificate_info_list = None
        self._industry_type = None

    @property
    def certificate_info_list(self):
        return self._certificate_info_list

    @certificate_info_list.setter
    def certificate_info_list(self, value):
        if isinstance(value, list):
            self._certificate_info_list = list()
            for i in value:
                if isinstance(i, CertificateInfo):
                    self._certificate_info_list.append(i)
                else:
                    self._certificate_info_list.append(CertificateInfo.from_alipay_dict(i))
    @property
    def industry_type(self):
        return self._industry_type

    @industry_type.setter
    def industry_type(self, value):
        self._industry_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_info_list:
            if isinstance(self.certificate_info_list, list):
                for i in range(0, len(self.certificate_info_list)):
                    element = self.certificate_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.certificate_info_list[i] = element.to_alipay_dict()
            if hasattr(self.certificate_info_list, 'to_alipay_dict'):
                params['certificate_info_list'] = self.certificate_info_list.to_alipay_dict()
            else:
                params['certificate_info_list'] = self.certificate_info_list
        if self.industry_type:
            if hasattr(self.industry_type, 'to_alipay_dict'):
                params['industry_type'] = self.industry_type.to_alipay_dict()
            else:
                params['industry_type'] = self.industry_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCityserviceIndustrymsgAuthBatchqueryModel()
        if 'certificate_info_list' in d:
            o.certificate_info_list = d['certificate_info_list']
        if 'industry_type' in d:
            o.industry_type = d['industry_type']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CertInfoRequest import CertInfoRequest


class AlipayEcoCityserviceCertinfoQueryModel(object):

    def __init__(self):
        self._cert_infos = None

    @property
    def cert_infos(self):
        return self._cert_infos

    @cert_infos.setter
    def cert_infos(self, value):
        if isinstance(value, list):
            self._cert_infos = list()
            for i in value:
                if isinstance(i, CertInfoRequest):
                    self._cert_infos.append(i)
                else:
                    self._cert_infos.append(CertInfoRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.cert_infos:
            if isinstance(self.cert_infos, list):
                for i in range(0, len(self.cert_infos)):
                    element = self.cert_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cert_infos[i] = element.to_alipay_dict()
            if hasattr(self.cert_infos, 'to_alipay_dict'):
                params['cert_infos'] = self.cert_infos.to_alipay_dict()
            else:
                params['cert_infos'] = self.cert_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCityserviceCertinfoQueryModel()
        if 'cert_infos' in d:
            o.cert_infos = d['cert_infos']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreatePartnerRequest import CreatePartnerRequest


class AnttechOceanbaseObglobalPartnerCreateModel(object):

    def __init__(self):
        self._create_partner_request = None

    @property
    def create_partner_request(self):
        return self._create_partner_request

    @create_partner_request.setter
    def create_partner_request(self, value):
        if isinstance(value, CreatePartnerRequest):
            self._create_partner_request = value
        else:
            self._create_partner_request = CreatePartnerRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.create_partner_request:
            if hasattr(self.create_partner_request, 'to_alipay_dict'):
                params['create_partner_request'] = self.create_partner_request.to_alipay_dict()
            else:
                params['create_partner_request'] = self.create_partner_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalPartnerCreateModel()
        if 'create_partner_request' in d:
            o.create_partner_request = d['create_partner_request']
        return o



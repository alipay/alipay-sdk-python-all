#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreateContactRequest import CreateContactRequest


class AnttechOceanbaseObglobalContactCreateModel(object):

    def __init__(self):
        self._create_contact_request = None

    @property
    def create_contact_request(self):
        return self._create_contact_request

    @create_contact_request.setter
    def create_contact_request(self, value):
        if isinstance(value, CreateContactRequest):
            self._create_contact_request = value
        else:
            self._create_contact_request = CreateContactRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.create_contact_request:
            if hasattr(self.create_contact_request, 'to_alipay_dict'):
                params['create_contact_request'] = self.create_contact_request.to_alipay_dict()
            else:
                params['create_contact_request'] = self.create_contact_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalContactCreateModel()
        if 'create_contact_request' in d:
            o.create_contact_request = d['create_contact_request']
        return o



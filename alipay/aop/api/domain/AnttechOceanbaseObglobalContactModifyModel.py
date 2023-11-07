#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UpdateContactRequest import UpdateContactRequest


class AnttechOceanbaseObglobalContactModifyModel(object):

    def __init__(self):
        self._update_contact_request = None

    @property
    def update_contact_request(self):
        return self._update_contact_request

    @update_contact_request.setter
    def update_contact_request(self, value):
        if isinstance(value, UpdateContactRequest):
            self._update_contact_request = value
        else:
            self._update_contact_request = UpdateContactRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.update_contact_request:
            if hasattr(self.update_contact_request, 'to_alipay_dict'):
                params['update_contact_request'] = self.update_contact_request.to_alipay_dict()
            else:
                params['update_contact_request'] = self.update_contact_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalContactModifyModel()
        if 'update_contact_request' in d:
            o.update_contact_request = d['update_contact_request']
        return o



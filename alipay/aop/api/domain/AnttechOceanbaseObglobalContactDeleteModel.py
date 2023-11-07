#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeleteContactRequest import DeleteContactRequest


class AnttechOceanbaseObglobalContactDeleteModel(object):

    def __init__(self):
        self._delete_contact_request = None

    @property
    def delete_contact_request(self):
        return self._delete_contact_request

    @delete_contact_request.setter
    def delete_contact_request(self, value):
        if isinstance(value, DeleteContactRequest):
            self._delete_contact_request = value
        else:
            self._delete_contact_request = DeleteContactRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.delete_contact_request:
            if hasattr(self.delete_contact_request, 'to_alipay_dict'):
                params['delete_contact_request'] = self.delete_contact_request.to_alipay_dict()
            else:
                params['delete_contact_request'] = self.delete_contact_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalContactDeleteModel()
        if 'delete_contact_request' in d:
            o.delete_contact_request = d['delete_contact_request']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalCrmmsgSendModel(object):

    def __init__(self):
        self._crm_notify_request = None

    @property
    def crm_notify_request(self):
        return self._crm_notify_request

    @crm_notify_request.setter
    def crm_notify_request(self, value):
        self._crm_notify_request = value


    def to_alipay_dict(self):
        params = dict()
        if self.crm_notify_request:
            if hasattr(self.crm_notify_request, 'to_alipay_dict'):
                params['crm_notify_request'] = self.crm_notify_request.to_alipay_dict()
            else:
                params['crm_notify_request'] = self.crm_notify_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalCrmmsgSendModel()
        if 'crm_notify_request' in d:
            o.crm_notify_request = d['crm_notify_request']
        return o



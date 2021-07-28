#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantCreditserviceDetailQueryModel(object):

    def __init__(self):
        self._credit_service_id = None
        self._version_no = None

    @property
    def credit_service_id(self):
        return self._credit_service_id

    @credit_service_id.setter
    def credit_service_id(self, value):
        self._credit_service_id = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_service_id:
            if hasattr(self.credit_service_id, 'to_alipay_dict'):
                params['credit_service_id'] = self.credit_service_id.to_alipay_dict()
            else:
                params['credit_service_id'] = self.credit_service_id
        if self.version_no:
            if hasattr(self.version_no, 'to_alipay_dict'):
                params['version_no'] = self.version_no.to_alipay_dict()
            else:
                params['version_no'] = self.version_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantCreditserviceDetailQueryModel()
        if 'credit_service_id' in d:
            o.credit_service_id = d['credit_service_id']
        if 'version_no' in d:
            o.version_no = d['version_no']
        return o



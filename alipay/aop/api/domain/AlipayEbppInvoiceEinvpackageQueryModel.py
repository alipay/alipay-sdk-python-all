#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceEinvpackageQueryModel(object):

    def __init__(self):
        self._encrypted_uid = None
        self._package_id = None

    @property
    def encrypted_uid(self):
        return self._encrypted_uid

    @encrypted_uid.setter
    def encrypted_uid(self, value):
        self._encrypted_uid = value
    @property
    def package_id(self):
        return self._package_id

    @package_id.setter
    def package_id(self, value):
        self._package_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.encrypted_uid:
            if hasattr(self.encrypted_uid, 'to_alipay_dict'):
                params['encrypted_uid'] = self.encrypted_uid.to_alipay_dict()
            else:
                params['encrypted_uid'] = self.encrypted_uid
        if self.package_id:
            if hasattr(self.package_id, 'to_alipay_dict'):
                params['package_id'] = self.package_id.to_alipay_dict()
            else:
                params['package_id'] = self.package_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceEinvpackageQueryModel()
        if 'encrypted_uid' in d:
            o.encrypted_uid = d['encrypted_uid']
        if 'package_id' in d:
            o.package_id = d['package_id']
        return o



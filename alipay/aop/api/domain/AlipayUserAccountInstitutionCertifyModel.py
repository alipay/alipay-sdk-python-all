#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAccountInstitutionCertifyModel(object):

    def __init__(self):
        self._institution_name = None
        self._logon_id = None

    @property
    def institution_name(self):
        return self._institution_name

    @institution_name.setter
    def institution_name(self, value):
        self._institution_name = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.institution_name:
            if hasattr(self.institution_name, 'to_alipay_dict'):
                params['institution_name'] = self.institution_name.to_alipay_dict()
            else:
                params['institution_name'] = self.institution_name
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAccountInstitutionCertifyModel()
        if 'institution_name' in d:
            o.institution_name = d['institution_name']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        return o



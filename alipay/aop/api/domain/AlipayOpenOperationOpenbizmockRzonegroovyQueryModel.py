#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgreementParams import AgreementParams


class AlipayOpenOperationOpenbizmockRzonegroovyQueryModel(object):

    def __init__(self):
        self._agreement_params = None
        self._uid = None

    @property
    def agreement_params(self):
        return self._agreement_params

    @agreement_params.setter
    def agreement_params(self, value):
        if isinstance(value, AgreementParams):
            self._agreement_params = value
        else:
            self._agreement_params = AgreementParams.from_alipay_dict(value)
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_params:
            if hasattr(self.agreement_params, 'to_alipay_dict'):
                params['agreement_params'] = self.agreement_params.to_alipay_dict()
            else:
                params['agreement_params'] = self.agreement_params
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockRzonegroovyQueryModel()
        if 'agreement_params' in d:
            o.agreement_params = d['agreement_params']
        if 'uid' in d:
            o.uid = d['uid']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditLinkAgreementInfo(object):

    def __init__(self):
        self._agreement_path = None
        self._agreement_type = None
        self._seal_flag = None

    @property
    def agreement_path(self):
        return self._agreement_path

    @agreement_path.setter
    def agreement_path(self, value):
        self._agreement_path = value
    @property
    def agreement_type(self):
        return self._agreement_type

    @agreement_type.setter
    def agreement_type(self, value):
        self._agreement_type = value
    @property
    def seal_flag(self):
        return self._seal_flag

    @seal_flag.setter
    def seal_flag(self, value):
        self._seal_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_path:
            if hasattr(self.agreement_path, 'to_alipay_dict'):
                params['agreement_path'] = self.agreement_path.to_alipay_dict()
            else:
                params['agreement_path'] = self.agreement_path
        if self.agreement_type:
            if hasattr(self.agreement_type, 'to_alipay_dict'):
                params['agreement_type'] = self.agreement_type.to_alipay_dict()
            else:
                params['agreement_type'] = self.agreement_type
        if self.seal_flag:
            if hasattr(self.seal_flag, 'to_alipay_dict'):
                params['seal_flag'] = self.seal_flag.to_alipay_dict()
            else:
                params['seal_flag'] = self.seal_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditLinkAgreementInfo()
        if 'agreement_path' in d:
            o.agreement_path = d['agreement_path']
        if 'agreement_type' in d:
            o.agreement_type = d['agreement_type']
        if 'seal_flag' in d:
            o.seal_flag = d['seal_flag']
        return o



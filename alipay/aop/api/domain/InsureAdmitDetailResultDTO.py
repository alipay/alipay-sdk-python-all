#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsureAdmitDetailResultDTO(object):

    def __init__(self):
        self._echo_key = None
        self._risk_code = None
        self._risk_desc = None
        self._risky = None

    @property
    def echo_key(self):
        return self._echo_key

    @echo_key.setter
    def echo_key(self, value):
        self._echo_key = value
    @property
    def risk_code(self):
        return self._risk_code

    @risk_code.setter
    def risk_code(self, value):
        self._risk_code = value
    @property
    def risk_desc(self):
        return self._risk_desc

    @risk_desc.setter
    def risk_desc(self, value):
        self._risk_desc = value
    @property
    def risky(self):
        return self._risky

    @risky.setter
    def risky(self, value):
        self._risky = value


    def to_alipay_dict(self):
        params = dict()
        if self.echo_key:
            if hasattr(self.echo_key, 'to_alipay_dict'):
                params['echo_key'] = self.echo_key.to_alipay_dict()
            else:
                params['echo_key'] = self.echo_key
        if self.risk_code:
            if hasattr(self.risk_code, 'to_alipay_dict'):
                params['risk_code'] = self.risk_code.to_alipay_dict()
            else:
                params['risk_code'] = self.risk_code
        if self.risk_desc:
            if hasattr(self.risk_desc, 'to_alipay_dict'):
                params['risk_desc'] = self.risk_desc.to_alipay_dict()
            else:
                params['risk_desc'] = self.risk_desc
        if self.risky:
            if hasattr(self.risky, 'to_alipay_dict'):
                params['risky'] = self.risky.to_alipay_dict()
            else:
                params['risky'] = self.risky
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsureAdmitDetailResultDTO()
        if 'echo_key' in d:
            o.echo_key = d['echo_key']
        if 'risk_code' in d:
            o.risk_code = d['risk_code']
        if 'risk_desc' in d:
            o.risk_desc = d['risk_desc']
        if 'risky' in d:
            o.risky = d['risky']
        return o



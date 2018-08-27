#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataSmartactivityForecastModel(object):

    def __init__(self):
        self._config_code = None
        self._diagnose_code = None
        self._ext_info = None

    @property
    def config_code(self):
        return self._config_code

    @config_code.setter
    def config_code(self, value):
        self._config_code = value
    @property
    def diagnose_code(self):
        return self._diagnose_code

    @diagnose_code.setter
    def diagnose_code(self, value):
        self._diagnose_code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.config_code:
            if hasattr(self.config_code, 'to_alipay_dict'):
                params['config_code'] = self.config_code.to_alipay_dict()
            else:
                params['config_code'] = self.config_code
        if self.diagnose_code:
            if hasattr(self.diagnose_code, 'to_alipay_dict'):
                params['diagnose_code'] = self.diagnose_code.to_alipay_dict()
            else:
                params['diagnose_code'] = self.diagnose_code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataSmartactivityForecastModel()
        if 'config_code' in d:
            o.config_code = d['config_code']
        if 'diagnose_code' in d:
            o.diagnose_code = d['diagnose_code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCdpRecommendQueryModel(object):

    def __init__(self):
        self._ad_code = None
        self._ext_info = None
        self._logon_id = None

    @property
    def ad_code(self):
        return self._ad_code

    @ad_code.setter
    def ad_code(self, value):
        self._ad_code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_code:
            if hasattr(self.ad_code, 'to_alipay_dict'):
                params['ad_code'] = self.ad_code.to_alipay_dict()
            else:
                params['ad_code'] = self.ad_code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        o = AlipayMarketingCdpRecommendQueryModel()
        if 'ad_code' in d:
            o.ad_code = d['ad_code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        return o



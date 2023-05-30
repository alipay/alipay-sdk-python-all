#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DspCreative import DspCreative


class AlipayDataDataserviceDspcreativeUploadModel(object):

    def __init__(self):
        self._biz_token = None
        self._creatives = None
        self._dsp_id = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def creatives(self):
        return self._creatives

    @creatives.setter
    def creatives(self, value):
        if isinstance(value, list):
            self._creatives = list()
            for i in value:
                if isinstance(i, DspCreative):
                    self._creatives.append(i)
                else:
                    self._creatives.append(DspCreative.from_alipay_dict(i))
    @property
    def dsp_id(self):
        return self._dsp_id

    @dsp_id.setter
    def dsp_id(self, value):
        self._dsp_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.creatives:
            if isinstance(self.creatives, list):
                for i in range(0, len(self.creatives)):
                    element = self.creatives[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.creatives[i] = element.to_alipay_dict()
            if hasattr(self.creatives, 'to_alipay_dict'):
                params['creatives'] = self.creatives.to_alipay_dict()
            else:
                params['creatives'] = self.creatives
        if self.dsp_id:
            if hasattr(self.dsp_id, 'to_alipay_dict'):
                params['dsp_id'] = self.dsp_id.to_alipay_dict()
            else:
                params['dsp_id'] = self.dsp_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceDspcreativeUploadModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'creatives' in d:
            o.creatives = d['creatives']
        if 'dsp_id' in d:
            o.dsp_id = d['dsp_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayCodecAcodeCertExpireModel(object):

    def __init__(self):
        self._biz_id = None
        self._institution_type = None
        self._time = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def institution_type(self):
        return self._institution_type

    @institution_type.setter
    def institution_type(self, value):
        self._institution_type = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.institution_type:
            if hasattr(self.institution_type, 'to_alipay_dict'):
                params['institution_type'] = self.institution_type.to_alipay_dict()
            else:
                params['institution_type'] = self.institution_type
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayCodecAcodeCertExpireModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'institution_type' in d:
            o.institution_type = d['institution_type']
        if 'time' in d:
            o.time = d['time']
        return o



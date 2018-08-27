#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CplifeResidentInfo import CplifeResidentInfo


class AlipayEcoCplifeResidentinfoUploadModel(object):

    def __init__(self):
        self._batch_id = None
        self._community_id = None
        self._resident_info = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value
    @property
    def resident_info(self):
        return self._resident_info

    @resident_info.setter
    def resident_info(self, value):
        if isinstance(value, list):
            self._resident_info = list()
            for i in value:
                if isinstance(i, CplifeResidentInfo):
                    self._resident_info.append(i)
                else:
                    self._resident_info.append(CplifeResidentInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.community_id:
            if hasattr(self.community_id, 'to_alipay_dict'):
                params['community_id'] = self.community_id.to_alipay_dict()
            else:
                params['community_id'] = self.community_id
        if self.resident_info:
            if isinstance(self.resident_info, list):
                for i in range(0, len(self.resident_info)):
                    element = self.resident_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.resident_info[i] = element.to_alipay_dict()
            if hasattr(self.resident_info, 'to_alipay_dict'):
                params['resident_info'] = self.resident_info.to_alipay_dict()
            else:
                params['resident_info'] = self.resident_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCplifeResidentinfoUploadModel()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'community_id' in d:
            o.community_id = d['community_id']
        if 'resident_info' in d:
            o.resident_info = d['resident_info']
        return o



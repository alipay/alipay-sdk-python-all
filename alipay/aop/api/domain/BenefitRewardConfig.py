#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitDisplayInfoResponse import BenefitDisplayInfoResponse


class BenefitRewardConfig(object):

    def __init__(self):
        self._display_info = None
        self._id = None
        self._source_id = None

    @property
    def display_info(self):
        return self._display_info

    @display_info.setter
    def display_info(self, value):
        if isinstance(value, BenefitDisplayInfoResponse):
            self._display_info = value
        else:
            self._display_info = BenefitDisplayInfoResponse.from_alipay_dict(value)
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.display_info:
            if hasattr(self.display_info, 'to_alipay_dict'):
                params['display_info'] = self.display_info.to_alipay_dict()
            else:
                params['display_info'] = self.display_info
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitRewardConfig()
        if 'display_info' in d:
            o.display_info = d['display_info']
        if 'id' in d:
            o.id = d['id']
        if 'source_id' in d:
            o.source_id = d['source_id']
        return o



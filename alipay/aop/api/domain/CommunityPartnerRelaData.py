#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommunityPartnerRelaData(object):

    def __init__(self):
        self._biz_data = None
        self._rela_type = None
        self._source_id = None
        self._target_id = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def rela_type(self):
        return self._rela_type

    @rela_type.setter
    def rela_type(self, value):
        self._rela_type = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.rela_type:
            if hasattr(self.rela_type, 'to_alipay_dict'):
                params['rela_type'] = self.rela_type.to_alipay_dict()
            else:
                params['rela_type'] = self.rela_type
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommunityPartnerRelaData()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'rela_type' in d:
            o.rela_type = d['rela_type']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'target_id' in d:
            o.target_id = d['target_id']
        return o



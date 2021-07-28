#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiQualityTestShieldCaselaunchApplyModel(object):

    def __init__(self):
        self._collection_ids = None
        self._dingding_token = None
        self._ext_infos = None

    @property
    def collection_ids(self):
        return self._collection_ids

    @collection_ids.setter
    def collection_ids(self, value):
        self._collection_ids = value
    @property
    def dingding_token(self):
        return self._dingding_token

    @dingding_token.setter
    def dingding_token(self, value):
        self._dingding_token = value
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value


    def to_alipay_dict(self):
        params = dict()
        if self.collection_ids:
            if hasattr(self.collection_ids, 'to_alipay_dict'):
                params['collection_ids'] = self.collection_ids.to_alipay_dict()
            else:
                params['collection_ids'] = self.collection_ids
        if self.dingding_token:
            if hasattr(self.dingding_token, 'to_alipay_dict'):
                params['dingding_token'] = self.dingding_token.to_alipay_dict()
            else:
                params['dingding_token'] = self.dingding_token
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiQualityTestShieldCaselaunchApplyModel()
        if 'collection_ids' in d:
            o.collection_ids = d['collection_ids']
        if 'dingding_token' in d:
            o.dingding_token = d['dingding_token']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEduCampusJobPublishModel(object):

    def __init__(self):
        self._gmt_expired = None
        self._gmt_refresh = None
        self._source_code = None
        self._source_id = None

    @property
    def gmt_expired(self):
        return self._gmt_expired

    @gmt_expired.setter
    def gmt_expired(self, value):
        self._gmt_expired = value
    @property
    def gmt_refresh(self):
        return self._gmt_refresh

    @gmt_refresh.setter
    def gmt_refresh(self, value):
        self._gmt_refresh = value
    @property
    def source_code(self):
        return self._source_code

    @source_code.setter
    def source_code(self, value):
        self._source_code = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_expired:
            if hasattr(self.gmt_expired, 'to_alipay_dict'):
                params['gmt_expired'] = self.gmt_expired.to_alipay_dict()
            else:
                params['gmt_expired'] = self.gmt_expired
        if self.gmt_refresh:
            if hasattr(self.gmt_refresh, 'to_alipay_dict'):
                params['gmt_refresh'] = self.gmt_refresh.to_alipay_dict()
            else:
                params['gmt_refresh'] = self.gmt_refresh
        if self.source_code:
            if hasattr(self.source_code, 'to_alipay_dict'):
                params['source_code'] = self.source_code.to_alipay_dict()
            else:
                params['source_code'] = self.source_code
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
        o = AlipayEcoEduCampusJobPublishModel()
        if 'gmt_expired' in d:
            o.gmt_expired = d['gmt_expired']
        if 'gmt_refresh' in d:
            o.gmt_refresh = d['gmt_refresh']
        if 'source_code' in d:
            o.source_code = d['source_code']
        if 'source_id' in d:
            o.source_id = d['source_id']
        return o



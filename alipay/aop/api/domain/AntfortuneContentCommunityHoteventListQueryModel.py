#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneContentCommunityHoteventListQueryModel(object):

    def __init__(self):
        self._date = None
        self._tenant_id = None
        self._topn_count = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def topn_count(self):
        return self._topn_count

    @topn_count.setter
    def topn_count(self, value):
        self._topn_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.topn_count:
            if hasattr(self.topn_count, 'to_alipay_dict'):
                params['topn_count'] = self.topn_count.to_alipay_dict()
            else:
                params['topn_count'] = self.topn_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneContentCommunityHoteventListQueryModel()
        if 'date' in d:
            o.date = d['date']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'topn_count' in d:
            o.topn_count = d['topn_count']
        return o



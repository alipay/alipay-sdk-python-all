#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YunTaskRankStatistic(object):

    def __init__(self):
        self._biz_rank = None
        self._biz_value = None
        self._principal_id = None
        self._principal_type = None

    @property
    def biz_rank(self):
        return self._biz_rank

    @biz_rank.setter
    def biz_rank(self, value):
        self._biz_rank = value
    @property
    def biz_value(self):
        return self._biz_value

    @biz_value.setter
    def biz_value(self, value):
        self._biz_value = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_type(self):
        return self._principal_type

    @principal_type.setter
    def principal_type(self, value):
        self._principal_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_rank:
            if hasattr(self.biz_rank, 'to_alipay_dict'):
                params['biz_rank'] = self.biz_rank.to_alipay_dict()
            else:
                params['biz_rank'] = self.biz_rank
        if self.biz_value:
            if hasattr(self.biz_value, 'to_alipay_dict'):
                params['biz_value'] = self.biz_value.to_alipay_dict()
            else:
                params['biz_value'] = self.biz_value
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.principal_type:
            if hasattr(self.principal_type, 'to_alipay_dict'):
                params['principal_type'] = self.principal_type.to_alipay_dict()
            else:
                params['principal_type'] = self.principal_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YunTaskRankStatistic()
        if 'biz_rank' in d:
            o.biz_rank = d['biz_rank']
        if 'biz_value' in d:
            o.biz_value = d['biz_value']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_type' in d:
            o.principal_type = d['principal_type']
        return o



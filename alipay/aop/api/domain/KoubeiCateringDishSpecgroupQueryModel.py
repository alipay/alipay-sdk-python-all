#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringDishSpecgroupQueryModel(object):

    def __init__(self):
        self._detail_spec_id = None
        self._group_spec_id = None

    @property
    def detail_spec_id(self):
        return self._detail_spec_id

    @detail_spec_id.setter
    def detail_spec_id(self, value):
        self._detail_spec_id = value
    @property
    def group_spec_id(self):
        return self._group_spec_id

    @group_spec_id.setter
    def group_spec_id(self, value):
        self._group_spec_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.detail_spec_id:
            if hasattr(self.detail_spec_id, 'to_alipay_dict'):
                params['detail_spec_id'] = self.detail_spec_id.to_alipay_dict()
            else:
                params['detail_spec_id'] = self.detail_spec_id
        if self.group_spec_id:
            if hasattr(self.group_spec_id, 'to_alipay_dict'):
                params['group_spec_id'] = self.group_spec_id.to_alipay_dict()
            else:
                params['group_spec_id'] = self.group_spec_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishSpecgroupQueryModel()
        if 'detail_spec_id' in d:
            o.detail_spec_id = d['detail_spec_id']
        if 'group_spec_id' in d:
            o.group_spec_id = d['group_spec_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseGroupQueryModel(object):

    def __init__(self):
        self._group_id = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseGroupQueryModel()
        if 'group_id' in d:
            o.group_id = d['group_id']
        return o



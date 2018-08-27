#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiItemExtitemCategoryQueryModel(object):

    def __init__(self):
        self._parent_id = None

    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.parent_id:
            if hasattr(self.parent_id, 'to_alipay_dict'):
                params['parent_id'] = self.parent_id.to_alipay_dict()
            else:
                params['parent_id'] = self.parent_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiItemExtitemCategoryQueryModel()
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        return o



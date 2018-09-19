#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiItemCategoryChildrenBatchqueryModel(object):

    def __init__(self):
        self._root_category_id = None

    @property
    def root_category_id(self):
        return self._root_category_id

    @root_category_id.setter
    def root_category_id(self, value):
        self._root_category_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.root_category_id:
            if hasattr(self.root_category_id, 'to_alipay_dict'):
                params['root_category_id'] = self.root_category_id.to_alipay_dict()
            else:
                params['root_category_id'] = self.root_category_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiItemCategoryChildrenBatchqueryModel()
        if 'root_category_id' in d:
            o.root_category_id = d['root_category_id']
        return o



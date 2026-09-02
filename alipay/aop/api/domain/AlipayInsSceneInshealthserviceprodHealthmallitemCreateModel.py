#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExternalItemImportRequest import ExternalItemImportRequest


class AlipayInsSceneInshealthserviceprodHealthmallitemCreateModel(object):

    def __init__(self):
        self._item_import_request = None

    @property
    def item_import_request(self):
        return self._item_import_request

    @item_import_request.setter
    def item_import_request(self, value):
        if isinstance(value, ExternalItemImportRequest):
            self._item_import_request = value
        else:
            self._item_import_request = ExternalItemImportRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.item_import_request:
            if hasattr(self.item_import_request, 'to_alipay_dict'):
                params['item_import_request'] = self.item_import_request.to_alipay_dict()
            else:
                params['item_import_request'] = self.item_import_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInshealthserviceprodHealthmallitemCreateModel()
        if 'item_import_request' in d:
            o.item_import_request = d['item_import_request']
        return o



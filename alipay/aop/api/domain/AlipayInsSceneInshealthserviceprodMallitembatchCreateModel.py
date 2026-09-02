#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExternalItemImportRequest import ExternalItemImportRequest


class AlipayInsSceneInshealthserviceprodMallitembatchCreateModel(object):

    def __init__(self):
        self._item_batch_import_request = None

    @property
    def item_batch_import_request(self):
        return self._item_batch_import_request

    @item_batch_import_request.setter
    def item_batch_import_request(self, value):
        if isinstance(value, list):
            self._item_batch_import_request = list()
            for i in value:
                if isinstance(i, ExternalItemImportRequest):
                    self._item_batch_import_request.append(i)
                else:
                    self._item_batch_import_request.append(ExternalItemImportRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.item_batch_import_request:
            if isinstance(self.item_batch_import_request, list):
                for i in range(0, len(self.item_batch_import_request)):
                    element = self.item_batch_import_request[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_batch_import_request[i] = element.to_alipay_dict()
            if hasattr(self.item_batch_import_request, 'to_alipay_dict'):
                params['item_batch_import_request'] = self.item_batch_import_request.to_alipay_dict()
            else:
                params['item_batch_import_request'] = self.item_batch_import_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInshealthserviceprodMallitembatchCreateModel()
        if 'item_batch_import_request' in d:
            o.item_batch_import_request = d['item_batch_import_request']
        return o



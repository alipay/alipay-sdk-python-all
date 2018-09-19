#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialGiftStockUploadModel(object):

    def __init__(self):
        self._entity_list = None
        self._idempotent_no = None
        self._mid = None
        self._sku_id = None

    @property
    def entity_list(self):
        return self._entity_list

    @entity_list.setter
    def entity_list(self, value):
        if isinstance(value, list):
            self._entity_list = list()
            for i in value:
                self._entity_list.append(i)
    @property
    def idempotent_no(self):
        return self._idempotent_no

    @idempotent_no.setter
    def idempotent_no(self, value):
        self._idempotent_no = value
    @property
    def mid(self):
        return self._mid

    @mid.setter
    def mid(self, value):
        self._mid = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.entity_list:
            if isinstance(self.entity_list, list):
                for i in range(0, len(self.entity_list)):
                    element = self.entity_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.entity_list[i] = element.to_alipay_dict()
            if hasattr(self.entity_list, 'to_alipay_dict'):
                params['entity_list'] = self.entity_list.to_alipay_dict()
            else:
                params['entity_list'] = self.entity_list
        if self.idempotent_no:
            if hasattr(self.idempotent_no, 'to_alipay_dict'):
                params['idempotent_no'] = self.idempotent_no.to_alipay_dict()
            else:
                params['idempotent_no'] = self.idempotent_no
        if self.mid:
            if hasattr(self.mid, 'to_alipay_dict'):
                params['mid'] = self.mid.to_alipay_dict()
            else:
                params['mid'] = self.mid
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialGiftStockUploadModel()
        if 'entity_list' in d:
            o.entity_list = d['entity_list']
        if 'idempotent_no' in d:
            o.idempotent_no = d['idempotent_no']
        if 'mid' in d:
            o.mid = d['mid']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o



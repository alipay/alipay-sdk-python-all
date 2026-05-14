#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLifeserviceShopCopyModel(object):

    def __init__(self):
        self._copy_type = None
        self._source_shop_id = None
        self._target_out_shop_ids = None
        self._target_shop_ids = None

    @property
    def copy_type(self):
        return self._copy_type

    @copy_type.setter
    def copy_type(self, value):
        self._copy_type = value
    @property
    def source_shop_id(self):
        return self._source_shop_id

    @source_shop_id.setter
    def source_shop_id(self, value):
        self._source_shop_id = value
    @property
    def target_out_shop_ids(self):
        return self._target_out_shop_ids

    @target_out_shop_ids.setter
    def target_out_shop_ids(self, value):
        if isinstance(value, list):
            self._target_out_shop_ids = list()
            for i in value:
                self._target_out_shop_ids.append(i)
    @property
    def target_shop_ids(self):
        return self._target_shop_ids

    @target_shop_ids.setter
    def target_shop_ids(self, value):
        if isinstance(value, list):
            self._target_shop_ids = list()
            for i in value:
                self._target_shop_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.copy_type:
            if hasattr(self.copy_type, 'to_alipay_dict'):
                params['copy_type'] = self.copy_type.to_alipay_dict()
            else:
                params['copy_type'] = self.copy_type
        if self.source_shop_id:
            if hasattr(self.source_shop_id, 'to_alipay_dict'):
                params['source_shop_id'] = self.source_shop_id.to_alipay_dict()
            else:
                params['source_shop_id'] = self.source_shop_id
        if self.target_out_shop_ids:
            if isinstance(self.target_out_shop_ids, list):
                for i in range(0, len(self.target_out_shop_ids)):
                    element = self.target_out_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_out_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.target_out_shop_ids, 'to_alipay_dict'):
                params['target_out_shop_ids'] = self.target_out_shop_ids.to_alipay_dict()
            else:
                params['target_out_shop_ids'] = self.target_out_shop_ids
        if self.target_shop_ids:
            if isinstance(self.target_shop_ids, list):
                for i in range(0, len(self.target_shop_ids)):
                    element = self.target_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.target_shop_ids, 'to_alipay_dict'):
                params['target_shop_ids'] = self.target_shop_ids.to_alipay_dict()
            else:
                params['target_shop_ids'] = self.target_shop_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceShopCopyModel()
        if 'copy_type' in d:
            o.copy_type = d['copy_type']
        if 'source_shop_id' in d:
            o.source_shop_id = d['source_shop_id']
        if 'target_out_shop_ids' in d:
            o.target_out_shop_ids = d['target_out_shop_ids']
        if 'target_shop_ids' in d:
            o.target_shop_ids = d['target_shop_ids']
        return o



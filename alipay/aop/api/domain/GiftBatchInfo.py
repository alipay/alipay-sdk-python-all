#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BatchList import BatchList


class GiftBatchInfo(object):

    def __init__(self):
        self._batch_list = None
        self._batch_sub_title = None
        self._gift_id = None

    @property
    def batch_list(self):
        return self._batch_list

    @batch_list.setter
    def batch_list(self, value):
        if isinstance(value, list):
            self._batch_list = list()
            for i in value:
                if isinstance(i, BatchList):
                    self._batch_list.append(i)
                else:
                    self._batch_list.append(BatchList.from_alipay_dict(i))
    @property
    def batch_sub_title(self):
        return self._batch_sub_title

    @batch_sub_title.setter
    def batch_sub_title(self, value):
        self._batch_sub_title = value
    @property
    def gift_id(self):
        return self._gift_id

    @gift_id.setter
    def gift_id(self, value):
        self._gift_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_list:
            if isinstance(self.batch_list, list):
                for i in range(0, len(self.batch_list)):
                    element = self.batch_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.batch_list[i] = element.to_alipay_dict()
            if hasattr(self.batch_list, 'to_alipay_dict'):
                params['batch_list'] = self.batch_list.to_alipay_dict()
            else:
                params['batch_list'] = self.batch_list
        if self.batch_sub_title:
            if hasattr(self.batch_sub_title, 'to_alipay_dict'):
                params['batch_sub_title'] = self.batch_sub_title.to_alipay_dict()
            else:
                params['batch_sub_title'] = self.batch_sub_title
        if self.gift_id:
            if hasattr(self.gift_id, 'to_alipay_dict'):
                params['gift_id'] = self.gift_id.to_alipay_dict()
            else:
                params['gift_id'] = self.gift_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GiftBatchInfo()
        if 'batch_list' in d:
            o.batch_list = d['batch_list']
        if 'batch_sub_title' in d:
            o.batch_sub_title = d['batch_sub_title']
        if 'gift_id' in d:
            o.gift_id = d['gift_id']
        return o



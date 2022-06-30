#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NimitzTable import NimitzTable


class RsData(object):

    def __init__(self):
        self._data = None
        self._rs_dataset = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, NimitzTable):
            self._data = value
        else:
            self._data = NimitzTable.from_alipay_dict(value)
    @property
    def rs_dataset(self):
        return self._rs_dataset

    @rs_dataset.setter
    def rs_dataset(self, value):
        self._rs_dataset = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.rs_dataset:
            if hasattr(self.rs_dataset, 'to_alipay_dict'):
                params['rs_dataset'] = self.rs_dataset.to_alipay_dict()
            else:
                params['rs_dataset'] = self.rs_dataset
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RsData()
        if 'data' in d:
            o.data = d['data']
        if 'rs_dataset' in d:
            o.rs_dataset = d['rs_dataset']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DataSecCheckContent import DataSecCheckContent


class KoubeiMarketingDataMallCheckGetModel(object):

    def __init__(self):
        self._check_contents = None
        self._data_source = None

    @property
    def check_contents(self):
        return self._check_contents

    @check_contents.setter
    def check_contents(self, value):
        if isinstance(value, list):
            self._check_contents = list()
            for i in value:
                if isinstance(i, DataSecCheckContent):
                    self._check_contents.append(i)
                else:
                    self._check_contents.append(DataSecCheckContent.from_alipay_dict(i))
    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_contents:
            if isinstance(self.check_contents, list):
                for i in range(0, len(self.check_contents)):
                    element = self.check_contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_contents[i] = element.to_alipay_dict()
            if hasattr(self.check_contents, 'to_alipay_dict'):
                params['check_contents'] = self.check_contents.to_alipay_dict()
            else:
                params['check_contents'] = self.check_contents
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataMallCheckGetModel()
        if 'check_contents' in d:
            o.check_contents = d['check_contents']
        if 'data_source' in d:
            o.data_source = d['data_source']
        return o



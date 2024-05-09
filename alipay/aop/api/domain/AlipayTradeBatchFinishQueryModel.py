#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BatchFinishQueryInfo import BatchFinishQueryInfo


class AlipayTradeBatchFinishQueryModel(object):

    def __init__(self):
        self._query_info_list = None

    @property
    def query_info_list(self):
        return self._query_info_list

    @query_info_list.setter
    def query_info_list(self, value):
        if isinstance(value, list):
            self._query_info_list = list()
            for i in value:
                if isinstance(i, BatchFinishQueryInfo):
                    self._query_info_list.append(i)
                else:
                    self._query_info_list.append(BatchFinishQueryInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.query_info_list:
            if isinstance(self.query_info_list, list):
                for i in range(0, len(self.query_info_list)):
                    element = self.query_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.query_info_list[i] = element.to_alipay_dict()
            if hasattr(self.query_info_list, 'to_alipay_dict'):
                params['query_info_list'] = self.query_info_list.to_alipay_dict()
            else:
                params['query_info_list'] = self.query_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeBatchFinishQueryModel()
        if 'query_info_list' in d:
            o.query_info_list = d['query_info_list']
        return o



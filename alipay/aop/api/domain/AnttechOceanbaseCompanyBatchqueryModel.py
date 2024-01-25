#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseCompanyBatchqueryModel(object):

    def __init__(self):
        self._entity_id_list = None

    @property
    def entity_id_list(self):
        return self._entity_id_list

    @entity_id_list.setter
    def entity_id_list(self, value):
        if isinstance(value, list):
            self._entity_id_list = list()
            for i in value:
                self._entity_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.entity_id_list:
            if isinstance(self.entity_id_list, list):
                for i in range(0, len(self.entity_id_list)):
                    element = self.entity_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.entity_id_list[i] = element.to_alipay_dict()
            if hasattr(self.entity_id_list, 'to_alipay_dict'):
                params['entity_id_list'] = self.entity_id_list.to_alipay_dict()
            else:
                params['entity_id_list'] = self.entity_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseCompanyBatchqueryModel()
        if 'entity_id_list' in d:
            o.entity_id_list = d['entity_id_list']
        return o



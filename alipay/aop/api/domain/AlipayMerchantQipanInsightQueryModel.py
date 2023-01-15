#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantQipanInsightQueryModel(object):

    def __init__(self):
        self._crowd_id = None
        self._portr_type_list = None
        self._relation_type = None
        self._report_date = None

    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
    @property
    def portr_type_list(self):
        return self._portr_type_list

    @portr_type_list.setter
    def portr_type_list(self, value):
        if isinstance(value, list):
            self._portr_type_list = list()
            for i in value:
                self._portr_type_list.append(i)
    @property
    def relation_type(self):
        return self._relation_type

    @relation_type.setter
    def relation_type(self, value):
        self._relation_type = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_id:
            if hasattr(self.crowd_id, 'to_alipay_dict'):
                params['crowd_id'] = self.crowd_id.to_alipay_dict()
            else:
                params['crowd_id'] = self.crowd_id
        if self.portr_type_list:
            if isinstance(self.portr_type_list, list):
                for i in range(0, len(self.portr_type_list)):
                    element = self.portr_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.portr_type_list[i] = element.to_alipay_dict()
            if hasattr(self.portr_type_list, 'to_alipay_dict'):
                params['portr_type_list'] = self.portr_type_list.to_alipay_dict()
            else:
                params['portr_type_list'] = self.portr_type_list
        if self.relation_type:
            if hasattr(self.relation_type, 'to_alipay_dict'):
                params['relation_type'] = self.relation_type.to_alipay_dict()
            else:
                params['relation_type'] = self.relation_type
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantQipanInsightQueryModel()
        if 'crowd_id' in d:
            o.crowd_id = d['crowd_id']
        if 'portr_type_list' in d:
            o.portr_type_list = d['portr_type_list']
        if 'relation_type' in d:
            o.relation_type = d['relation_type']
        if 'report_date' in d:
            o.report_date = d['report_date']
        return o



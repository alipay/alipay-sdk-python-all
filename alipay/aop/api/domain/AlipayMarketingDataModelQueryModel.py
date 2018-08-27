#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ModelQueryParam import ModelQueryParam


class AlipayMarketingDataModelQueryModel(object):

    def __init__(self):
        self._model_query_param = None
        self._model_uk = None

    @property
    def model_query_param(self):
        return self._model_query_param

    @model_query_param.setter
    def model_query_param(self, value):
        if isinstance(value, list):
            self._model_query_param = list()
            for i in value:
                if isinstance(i, ModelQueryParam):
                    self._model_query_param.append(i)
                else:
                    self._model_query_param.append(ModelQueryParam.from_alipay_dict(i))
    @property
    def model_uk(self):
        return self._model_uk

    @model_uk.setter
    def model_uk(self, value):
        self._model_uk = value


    def to_alipay_dict(self):
        params = dict()
        if self.model_query_param:
            if isinstance(self.model_query_param, list):
                for i in range(0, len(self.model_query_param)):
                    element = self.model_query_param[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.model_query_param[i] = element.to_alipay_dict()
            if hasattr(self.model_query_param, 'to_alipay_dict'):
                params['model_query_param'] = self.model_query_param.to_alipay_dict()
            else:
                params['model_query_param'] = self.model_query_param
        if self.model_uk:
            if hasattr(self.model_uk, 'to_alipay_dict'):
                params['model_uk'] = self.model_uk.to_alipay_dict()
            else:
                params['model_uk'] = self.model_uk
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingDataModelQueryModel()
        if 'model_query_param' in d:
            o.model_query_param = d['model_query_param']
        if 'model_uk' in d:
            o.model_uk = d['model_uk']
        return o



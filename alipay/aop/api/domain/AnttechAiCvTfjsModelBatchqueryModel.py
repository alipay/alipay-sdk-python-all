#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechAiCvTfjsModelBatchqueryModel(object):

    def __init__(self):
        self._model_info = None

    @property
    def model_info(self):
        return self._model_info

    @model_info.setter
    def model_info(self, value):
        self._model_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.model_info:
            if hasattr(self.model_info, 'to_alipay_dict'):
                params['model_info'] = self.model_info.to_alipay_dict()
            else:
                params['model_info'] = self.model_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechAiCvTfjsModelBatchqueryModel()
        if 'model_info' in d:
            o.model_info = d['model_info']
        return o



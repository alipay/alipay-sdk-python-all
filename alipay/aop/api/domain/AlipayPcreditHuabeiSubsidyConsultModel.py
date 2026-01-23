#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubsidySimpleRequest import SubsidySimpleRequest


class AlipayPcreditHuabeiSubsidyConsultModel(object):

    def __init__(self):
        self._subsidy_aggregated_req_models = None

    @property
    def subsidy_aggregated_req_models(self):
        return self._subsidy_aggregated_req_models

    @subsidy_aggregated_req_models.setter
    def subsidy_aggregated_req_models(self, value):
        if isinstance(value, list):
            self._subsidy_aggregated_req_models = list()
            for i in value:
                if isinstance(i, SubsidySimpleRequest):
                    self._subsidy_aggregated_req_models.append(i)
                else:
                    self._subsidy_aggregated_req_models.append(SubsidySimpleRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.subsidy_aggregated_req_models:
            if isinstance(self.subsidy_aggregated_req_models, list):
                for i in range(0, len(self.subsidy_aggregated_req_models)):
                    element = self.subsidy_aggregated_req_models[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.subsidy_aggregated_req_models[i] = element.to_alipay_dict()
            if hasattr(self.subsidy_aggregated_req_models, 'to_alipay_dict'):
                params['subsidy_aggregated_req_models'] = self.subsidy_aggregated_req_models.to_alipay_dict()
            else:
                params['subsidy_aggregated_req_models'] = self.subsidy_aggregated_req_models
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiSubsidyConsultModel()
        if 'subsidy_aggregated_req_models' in d:
            o.subsidy_aggregated_req_models = d['subsidy_aggregated_req_models']
        return o



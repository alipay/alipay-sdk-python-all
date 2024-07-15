#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RiskMetaData import RiskMetaData


class AlipayCloudTraasCloudriskRiskmetadataSyncModel(object):

    def __init__(self):
        self._risk_meta_data_list = None

    @property
    def risk_meta_data_list(self):
        return self._risk_meta_data_list

    @risk_meta_data_list.setter
    def risk_meta_data_list(self, value):
        if isinstance(value, list):
            self._risk_meta_data_list = list()
            for i in value:
                if isinstance(i, RiskMetaData):
                    self._risk_meta_data_list.append(i)
                else:
                    self._risk_meta_data_list.append(RiskMetaData.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.risk_meta_data_list:
            if isinstance(self.risk_meta_data_list, list):
                for i in range(0, len(self.risk_meta_data_list)):
                    element = self.risk_meta_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_meta_data_list[i] = element.to_alipay_dict()
            if hasattr(self.risk_meta_data_list, 'to_alipay_dict'):
                params['risk_meta_data_list'] = self.risk_meta_data_list.to_alipay_dict()
            else:
                params['risk_meta_data_list'] = self.risk_meta_data_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudTraasCloudriskRiskmetadataSyncModel()
        if 'risk_meta_data_list' in d:
            o.risk_meta_data_list = d['risk_meta_data_list']
        return o



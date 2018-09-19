#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SingleFundDetailItemAOPModel import SingleFundDetailItemAOPModel


class FundDetailItemAOPModel(object):

    def __init__(self):
        self._single_fund_detail_item_aopmodel_list = None

    @property
    def single_fund_detail_item_aopmodel_list(self):
        return self._single_fund_detail_item_aopmodel_list

    @single_fund_detail_item_aopmodel_list.setter
    def single_fund_detail_item_aopmodel_list(self, value):
        if isinstance(value, list):
            self._single_fund_detail_item_aopmodel_list = list()
            for i in value:
                if isinstance(i, SingleFundDetailItemAOPModel):
                    self._single_fund_detail_item_aopmodel_list.append(i)
                else:
                    self._single_fund_detail_item_aopmodel_list.append(SingleFundDetailItemAOPModel.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.single_fund_detail_item_aopmodel_list:
            if isinstance(self.single_fund_detail_item_aopmodel_list, list):
                for i in range(0, len(self.single_fund_detail_item_aopmodel_list)):
                    element = self.single_fund_detail_item_aopmodel_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.single_fund_detail_item_aopmodel_list[i] = element.to_alipay_dict()
            if hasattr(self.single_fund_detail_item_aopmodel_list, 'to_alipay_dict'):
                params['single_fund_detail_item_aopmodel_list'] = self.single_fund_detail_item_aopmodel_list.to_alipay_dict()
            else:
                params['single_fund_detail_item_aopmodel_list'] = self.single_fund_detail_item_aopmodel_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundDetailItemAOPModel()
        if 'single_fund_detail_item_aopmodel_list' in d:
            o.single_fund_detail_item_aopmodel_list = d['single_fund_detail_item_aopmodel_list']
        return o



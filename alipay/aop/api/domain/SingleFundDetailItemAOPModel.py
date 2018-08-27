#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BatchFundItemAOPModel import BatchFundItemAOPModel
from alipay.aop.api.domain.ConsumeRecordAOPModel import ConsumeRecordAOPModel


class SingleFundDetailItemAOPModel(object):

    def __init__(self):
        self._batch_fund_item_model_list = None
        self._consume_record = None

    @property
    def batch_fund_item_model_list(self):
        return self._batch_fund_item_model_list

    @batch_fund_item_model_list.setter
    def batch_fund_item_model_list(self, value):
        if isinstance(value, list):
            self._batch_fund_item_model_list = list()
            for i in value:
                if isinstance(i, BatchFundItemAOPModel):
                    self._batch_fund_item_model_list.append(i)
                else:
                    self._batch_fund_item_model_list.append(BatchFundItemAOPModel.from_alipay_dict(i))
    @property
    def consume_record(self):
        return self._consume_record

    @consume_record.setter
    def consume_record(self, value):
        if isinstance(value, ConsumeRecordAOPModel):
            self._consume_record = value
        else:
            self._consume_record = ConsumeRecordAOPModel.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.batch_fund_item_model_list:
            if isinstance(self.batch_fund_item_model_list, list):
                for i in range(0, len(self.batch_fund_item_model_list)):
                    element = self.batch_fund_item_model_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.batch_fund_item_model_list[i] = element.to_alipay_dict()
            if hasattr(self.batch_fund_item_model_list, 'to_alipay_dict'):
                params['batch_fund_item_model_list'] = self.batch_fund_item_model_list.to_alipay_dict()
            else:
                params['batch_fund_item_model_list'] = self.batch_fund_item_model_list
        if self.consume_record:
            if hasattr(self.consume_record, 'to_alipay_dict'):
                params['consume_record'] = self.consume_record.to_alipay_dict()
            else:
                params['consume_record'] = self.consume_record
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SingleFundDetailItemAOPModel()
        if 'batch_fund_item_model_list' in d:
            o.batch_fund_item_model_list = d['batch_fund_item_model_list']
        if 'consume_record' in d:
            o.consume_record = d['consume_record']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SupplierAppendixUrl import SupplierAppendixUrl
from alipay.aop.api.domain.SupplierProduceBatch import SupplierProduceBatch
from alipay.aop.api.domain.SupplierItemAttrField import SupplierItemAttrField


class AntProdpaasProductProduceCompleteCallbackModel(object):

    def __init__(self):
        self._abnormal_feedback = None
        self._abnormal_reason = None
        self._actual_amount = None
        self._actual_end_time = None
        self._appendix_urls = None
        self._batch_flag = None
        self._batch_no = None
        self._batchs = None
        self._extend_pros = None
        self._last_batch_flag = None
        self._plan_end_time = None
        self._plan_start_time = None
        self._produce_order_code = None

    @property
    def abnormal_feedback(self):
        return self._abnormal_feedback

    @abnormal_feedback.setter
    def abnormal_feedback(self, value):
        self._abnormal_feedback = value
    @property
    def abnormal_reason(self):
        return self._abnormal_reason

    @abnormal_reason.setter
    def abnormal_reason(self, value):
        self._abnormal_reason = value
    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def actual_end_time(self):
        return self._actual_end_time

    @actual_end_time.setter
    def actual_end_time(self, value):
        self._actual_end_time = value
    @property
    def appendix_urls(self):
        return self._appendix_urls

    @appendix_urls.setter
    def appendix_urls(self, value):
        if isinstance(value, list):
            self._appendix_urls = list()
            for i in value:
                if isinstance(i, SupplierAppendixUrl):
                    self._appendix_urls.append(i)
                else:
                    self._appendix_urls.append(SupplierAppendixUrl.from_alipay_dict(i))
    @property
    def batch_flag(self):
        return self._batch_flag

    @batch_flag.setter
    def batch_flag(self, value):
        self._batch_flag = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def batchs(self):
        return self._batchs

    @batchs.setter
    def batchs(self, value):
        if isinstance(value, list):
            self._batchs = list()
            for i in value:
                if isinstance(i, SupplierProduceBatch):
                    self._batchs.append(i)
                else:
                    self._batchs.append(SupplierProduceBatch.from_alipay_dict(i))
    @property
    def extend_pros(self):
        return self._extend_pros

    @extend_pros.setter
    def extend_pros(self, value):
        if isinstance(value, list):
            self._extend_pros = list()
            for i in value:
                if isinstance(i, SupplierItemAttrField):
                    self._extend_pros.append(i)
                else:
                    self._extend_pros.append(SupplierItemAttrField.from_alipay_dict(i))
    @property
    def last_batch_flag(self):
        return self._last_batch_flag

    @last_batch_flag.setter
    def last_batch_flag(self, value):
        self._last_batch_flag = value
    @property
    def plan_end_time(self):
        return self._plan_end_time

    @plan_end_time.setter
    def plan_end_time(self, value):
        self._plan_end_time = value
    @property
    def plan_start_time(self):
        return self._plan_start_time

    @plan_start_time.setter
    def plan_start_time(self, value):
        self._plan_start_time = value
    @property
    def produce_order_code(self):
        return self._produce_order_code

    @produce_order_code.setter
    def produce_order_code(self, value):
        self._produce_order_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.abnormal_feedback:
            if hasattr(self.abnormal_feedback, 'to_alipay_dict'):
                params['abnormal_feedback'] = self.abnormal_feedback.to_alipay_dict()
            else:
                params['abnormal_feedback'] = self.abnormal_feedback
        if self.abnormal_reason:
            if hasattr(self.abnormal_reason, 'to_alipay_dict'):
                params['abnormal_reason'] = self.abnormal_reason.to_alipay_dict()
            else:
                params['abnormal_reason'] = self.abnormal_reason
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.actual_end_time:
            if hasattr(self.actual_end_time, 'to_alipay_dict'):
                params['actual_end_time'] = self.actual_end_time.to_alipay_dict()
            else:
                params['actual_end_time'] = self.actual_end_time
        if self.appendix_urls:
            if isinstance(self.appendix_urls, list):
                for i in range(0, len(self.appendix_urls)):
                    element = self.appendix_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.appendix_urls[i] = element.to_alipay_dict()
            if hasattr(self.appendix_urls, 'to_alipay_dict'):
                params['appendix_urls'] = self.appendix_urls.to_alipay_dict()
            else:
                params['appendix_urls'] = self.appendix_urls
        if self.batch_flag:
            if hasattr(self.batch_flag, 'to_alipay_dict'):
                params['batch_flag'] = self.batch_flag.to_alipay_dict()
            else:
                params['batch_flag'] = self.batch_flag
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.batchs:
            if isinstance(self.batchs, list):
                for i in range(0, len(self.batchs)):
                    element = self.batchs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.batchs[i] = element.to_alipay_dict()
            if hasattr(self.batchs, 'to_alipay_dict'):
                params['batchs'] = self.batchs.to_alipay_dict()
            else:
                params['batchs'] = self.batchs
        if self.extend_pros:
            if isinstance(self.extend_pros, list):
                for i in range(0, len(self.extend_pros)):
                    element = self.extend_pros[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extend_pros[i] = element.to_alipay_dict()
            if hasattr(self.extend_pros, 'to_alipay_dict'):
                params['extend_pros'] = self.extend_pros.to_alipay_dict()
            else:
                params['extend_pros'] = self.extend_pros
        if self.last_batch_flag:
            if hasattr(self.last_batch_flag, 'to_alipay_dict'):
                params['last_batch_flag'] = self.last_batch_flag.to_alipay_dict()
            else:
                params['last_batch_flag'] = self.last_batch_flag
        if self.plan_end_time:
            if hasattr(self.plan_end_time, 'to_alipay_dict'):
                params['plan_end_time'] = self.plan_end_time.to_alipay_dict()
            else:
                params['plan_end_time'] = self.plan_end_time
        if self.plan_start_time:
            if hasattr(self.plan_start_time, 'to_alipay_dict'):
                params['plan_start_time'] = self.plan_start_time.to_alipay_dict()
            else:
                params['plan_start_time'] = self.plan_start_time
        if self.produce_order_code:
            if hasattr(self.produce_order_code, 'to_alipay_dict'):
                params['produce_order_code'] = self.produce_order_code.to_alipay_dict()
            else:
                params['produce_order_code'] = self.produce_order_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntProdpaasProductProduceCompleteCallbackModel()
        if 'abnormal_feedback' in d:
            o.abnormal_feedback = d['abnormal_feedback']
        if 'abnormal_reason' in d:
            o.abnormal_reason = d['abnormal_reason']
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'actual_end_time' in d:
            o.actual_end_time = d['actual_end_time']
        if 'appendix_urls' in d:
            o.appendix_urls = d['appendix_urls']
        if 'batch_flag' in d:
            o.batch_flag = d['batch_flag']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'batchs' in d:
            o.batchs = d['batchs']
        if 'extend_pros' in d:
            o.extend_pros = d['extend_pros']
        if 'last_batch_flag' in d:
            o.last_batch_flag = d['last_batch_flag']
        if 'plan_end_time' in d:
            o.plan_end_time = d['plan_end_time']
        if 'plan_start_time' in d:
            o.plan_start_time = d['plan_start_time']
        if 'produce_order_code' in d:
            o.produce_order_code = d['produce_order_code']
        return o



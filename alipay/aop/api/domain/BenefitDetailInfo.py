#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitAmountInfo import BenefitAmountInfo
from alipay.aop.api.domain.BenefitDateInfo import BenefitDateInfo
from alipay.aop.api.domain.BenefitDisplayInfo import BenefitDisplayInfo
from alipay.aop.api.domain.BenefitSource import BenefitSource


class BenefitDetailInfo(object):

    def __init__(self):
        self._benefit_amount_info = None
        self._benefit_date_info = None
        self._benefit_display_info = None
        self._benefit_id = None
        self._benefit_operation_id = None
        self._benefit_operation_time = None
        self._benefit_source = None
        self._benefit_status = None
        self._benefit_type = None
        self._customer_id = None

    @property
    def benefit_amount_info(self):
        return self._benefit_amount_info

    @benefit_amount_info.setter
    def benefit_amount_info(self, value):
        if isinstance(value, BenefitAmountInfo):
            self._benefit_amount_info = value
        else:
            self._benefit_amount_info = BenefitAmountInfo.from_alipay_dict(value)
    @property
    def benefit_date_info(self):
        return self._benefit_date_info

    @benefit_date_info.setter
    def benefit_date_info(self, value):
        if isinstance(value, BenefitDateInfo):
            self._benefit_date_info = value
        else:
            self._benefit_date_info = BenefitDateInfo.from_alipay_dict(value)
    @property
    def benefit_display_info(self):
        return self._benefit_display_info

    @benefit_display_info.setter
    def benefit_display_info(self, value):
        if isinstance(value, BenefitDisplayInfo):
            self._benefit_display_info = value
        else:
            self._benefit_display_info = BenefitDisplayInfo.from_alipay_dict(value)
    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def benefit_operation_id(self):
        return self._benefit_operation_id

    @benefit_operation_id.setter
    def benefit_operation_id(self, value):
        self._benefit_operation_id = value
    @property
    def benefit_operation_time(self):
        return self._benefit_operation_time

    @benefit_operation_time.setter
    def benefit_operation_time(self, value):
        self._benefit_operation_time = value
    @property
    def benefit_source(self):
        return self._benefit_source

    @benefit_source.setter
    def benefit_source(self, value):
        if isinstance(value, BenefitSource):
            self._benefit_source = value
        else:
            self._benefit_source = BenefitSource.from_alipay_dict(value)
    @property
    def benefit_status(self):
        return self._benefit_status

    @benefit_status.setter
    def benefit_status(self, value):
        self._benefit_status = value
    @property
    def benefit_type(self):
        return self._benefit_type

    @benefit_type.setter
    def benefit_type(self, value):
        self._benefit_type = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_amount_info:
            if hasattr(self.benefit_amount_info, 'to_alipay_dict'):
                params['benefit_amount_info'] = self.benefit_amount_info.to_alipay_dict()
            else:
                params['benefit_amount_info'] = self.benefit_amount_info
        if self.benefit_date_info:
            if hasattr(self.benefit_date_info, 'to_alipay_dict'):
                params['benefit_date_info'] = self.benefit_date_info.to_alipay_dict()
            else:
                params['benefit_date_info'] = self.benefit_date_info
        if self.benefit_display_info:
            if hasattr(self.benefit_display_info, 'to_alipay_dict'):
                params['benefit_display_info'] = self.benefit_display_info.to_alipay_dict()
            else:
                params['benefit_display_info'] = self.benefit_display_info
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.benefit_operation_id:
            if hasattr(self.benefit_operation_id, 'to_alipay_dict'):
                params['benefit_operation_id'] = self.benefit_operation_id.to_alipay_dict()
            else:
                params['benefit_operation_id'] = self.benefit_operation_id
        if self.benefit_operation_time:
            if hasattr(self.benefit_operation_time, 'to_alipay_dict'):
                params['benefit_operation_time'] = self.benefit_operation_time.to_alipay_dict()
            else:
                params['benefit_operation_time'] = self.benefit_operation_time
        if self.benefit_source:
            if hasattr(self.benefit_source, 'to_alipay_dict'):
                params['benefit_source'] = self.benefit_source.to_alipay_dict()
            else:
                params['benefit_source'] = self.benefit_source
        if self.benefit_status:
            if hasattr(self.benefit_status, 'to_alipay_dict'):
                params['benefit_status'] = self.benefit_status.to_alipay_dict()
            else:
                params['benefit_status'] = self.benefit_status
        if self.benefit_type:
            if hasattr(self.benefit_type, 'to_alipay_dict'):
                params['benefit_type'] = self.benefit_type.to_alipay_dict()
            else:
                params['benefit_type'] = self.benefit_type
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitDetailInfo()
        if 'benefit_amount_info' in d:
            o.benefit_amount_info = d['benefit_amount_info']
        if 'benefit_date_info' in d:
            o.benefit_date_info = d['benefit_date_info']
        if 'benefit_display_info' in d:
            o.benefit_display_info = d['benefit_display_info']
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'benefit_operation_id' in d:
            o.benefit_operation_id = d['benefit_operation_id']
        if 'benefit_operation_time' in d:
            o.benefit_operation_time = d['benefit_operation_time']
        if 'benefit_source' in d:
            o.benefit_source = d['benefit_source']
        if 'benefit_status' in d:
            o.benefit_status = d['benefit_status']
        if 'benefit_type' in d:
            o.benefit_type = d['benefit_type']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RetryDataItem import RetryDataItem


class DataSyncResponse(object):

    def __init__(self):
        self._batch_id = None
        self._failed_num = None
        self._retry_data_list = None
        self._success_num = None
        self._total_num = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def failed_num(self):
        return self._failed_num

    @failed_num.setter
    def failed_num(self, value):
        self._failed_num = value
    @property
    def retry_data_list(self):
        return self._retry_data_list

    @retry_data_list.setter
    def retry_data_list(self, value):
        if isinstance(value, list):
            self._retry_data_list = list()
            for i in value:
                if isinstance(i, RetryDataItem):
                    self._retry_data_list.append(i)
                else:
                    self._retry_data_list.append(RetryDataItem.from_alipay_dict(i))
    @property
    def success_num(self):
        return self._success_num

    @success_num.setter
    def success_num(self, value):
        self._success_num = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.failed_num:
            if hasattr(self.failed_num, 'to_alipay_dict'):
                params['failed_num'] = self.failed_num.to_alipay_dict()
            else:
                params['failed_num'] = self.failed_num
        if self.retry_data_list:
            if isinstance(self.retry_data_list, list):
                for i in range(0, len(self.retry_data_list)):
                    element = self.retry_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.retry_data_list[i] = element.to_alipay_dict()
            if hasattr(self.retry_data_list, 'to_alipay_dict'):
                params['retry_data_list'] = self.retry_data_list.to_alipay_dict()
            else:
                params['retry_data_list'] = self.retry_data_list
        if self.success_num:
            if hasattr(self.success_num, 'to_alipay_dict'):
                params['success_num'] = self.success_num.to_alipay_dict()
            else:
                params['success_num'] = self.success_num
        if self.total_num:
            if hasattr(self.total_num, 'to_alipay_dict'):
                params['total_num'] = self.total_num.to_alipay_dict()
            else:
                params['total_num'] = self.total_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DataSyncResponse()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'failed_num' in d:
            o.failed_num = d['failed_num']
        if 'retry_data_list' in d:
            o.retry_data_list = d['retry_data_list']
        if 'success_num' in d:
            o.success_num = d['success_num']
        if 'total_num' in d:
            o.total_num = d['total_num']
        return o



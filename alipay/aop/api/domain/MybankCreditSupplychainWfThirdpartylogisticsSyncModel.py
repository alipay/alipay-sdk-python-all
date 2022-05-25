#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LendingDataList import LendingDataList


class MybankCreditSupplychainWfThirdpartylogisticsSyncModel(object):

    def __init__(self):
        self._customer_id = None
        self._lending_data_list = None
        self._request_id = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def lending_data_list(self):
        return self._lending_data_list

    @lending_data_list.setter
    def lending_data_list(self, value):
        if isinstance(value, list):
            self._lending_data_list = list()
            for i in value:
                if isinstance(i, LendingDataList):
                    self._lending_data_list.append(i)
                else:
                    self._lending_data_list.append(LendingDataList.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.lending_data_list:
            if isinstance(self.lending_data_list, list):
                for i in range(0, len(self.lending_data_list)):
                    element = self.lending_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.lending_data_list[i] = element.to_alipay_dict()
            if hasattr(self.lending_data_list, 'to_alipay_dict'):
                params['lending_data_list'] = self.lending_data_list.to_alipay_dict()
            else:
                params['lending_data_list'] = self.lending_data_list
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainWfThirdpartylogisticsSyncModel()
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'lending_data_list' in d:
            o.lending_data_list = d['lending_data_list']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MpcpromoGoodsList import MpcpromoGoodsList
from alipay.aop.api.domain.MpcpromoVoucherList import MpcpromoVoucherList


class TechriskInnovateMpcpromoDataSyncModel(object):

    def __init__(self):
        self._data_list = None
        self._data_type = None
        self._industry = None
        self._voucher_list = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, MpcpromoGoodsList):
                    self._data_list.append(i)
                else:
                    self._data_list.append(MpcpromoGoodsList.from_alipay_dict(i))
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def voucher_list(self):
        return self._voucher_list

    @voucher_list.setter
    def voucher_list(self, value):
        if isinstance(value, list):
            self._voucher_list = list()
            for i in value:
                if isinstance(i, MpcpromoVoucherList):
                    self._voucher_list.append(i)
                else:
                    self._voucher_list.append(MpcpromoVoucherList.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.data_list:
            if isinstance(self.data_list, list):
                for i in range(0, len(self.data_list)):
                    element = self.data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data_list[i] = element.to_alipay_dict()
            if hasattr(self.data_list, 'to_alipay_dict'):
                params['data_list'] = self.data_list.to_alipay_dict()
            else:
                params['data_list'] = self.data_list
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.voucher_list:
            if isinstance(self.voucher_list, list):
                for i in range(0, len(self.voucher_list)):
                    element = self.voucher_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_list[i] = element.to_alipay_dict()
            if hasattr(self.voucher_list, 'to_alipay_dict'):
                params['voucher_list'] = self.voucher_list.to_alipay_dict()
            else:
                params['voucher_list'] = self.voucher_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TechriskInnovateMpcpromoDataSyncModel()
        if 'data_list' in d:
            o.data_list = d['data_list']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'industry' in d:
            o.industry = d['industry']
        if 'voucher_list' in d:
            o.voucher_list = d['voucher_list']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CarInfo import CarInfo
from alipay.aop.api.domain.FileDetail import FileDetail
from alipay.aop.api.domain.ValuationInfo import ValuationInfo


class XingheLendassistCarfinInstinfoNotifyModel(object):

    def __init__(self):
        self._apply_no = None
        self._car_info = None
        self._file_list = None
        self._out_apply_no = None
        self._postback_list = None
        self._valuation_info = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def car_info(self):
        return self._car_info

    @car_info.setter
    def car_info(self, value):
        if isinstance(value, CarInfo):
            self._car_info = value
        else:
            self._car_info = CarInfo.from_alipay_dict(value)
    @property
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, value):
        if isinstance(value, list):
            self._file_list = list()
            for i in value:
                if isinstance(i, FileDetail):
                    self._file_list.append(i)
                else:
                    self._file_list.append(FileDetail.from_alipay_dict(i))
    @property
    def out_apply_no(self):
        return self._out_apply_no

    @out_apply_no.setter
    def out_apply_no(self, value):
        self._out_apply_no = value
    @property
    def postback_list(self):
        return self._postback_list

    @postback_list.setter
    def postback_list(self, value):
        if isinstance(value, list):
            self._postback_list = list()
            for i in value:
                self._postback_list.append(i)
    @property
    def valuation_info(self):
        return self._valuation_info

    @valuation_info.setter
    def valuation_info(self, value):
        if isinstance(value, ValuationInfo):
            self._valuation_info = value
        else:
            self._valuation_info = ValuationInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.car_info:
            if hasattr(self.car_info, 'to_alipay_dict'):
                params['car_info'] = self.car_info.to_alipay_dict()
            else:
                params['car_info'] = self.car_info
        if self.file_list:
            if isinstance(self.file_list, list):
                for i in range(0, len(self.file_list)):
                    element = self.file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_list[i] = element.to_alipay_dict()
            if hasattr(self.file_list, 'to_alipay_dict'):
                params['file_list'] = self.file_list.to_alipay_dict()
            else:
                params['file_list'] = self.file_list
        if self.out_apply_no:
            if hasattr(self.out_apply_no, 'to_alipay_dict'):
                params['out_apply_no'] = self.out_apply_no.to_alipay_dict()
            else:
                params['out_apply_no'] = self.out_apply_no
        if self.postback_list:
            if isinstance(self.postback_list, list):
                for i in range(0, len(self.postback_list)):
                    element = self.postback_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.postback_list[i] = element.to_alipay_dict()
            if hasattr(self.postback_list, 'to_alipay_dict'):
                params['postback_list'] = self.postback_list.to_alipay_dict()
            else:
                params['postback_list'] = self.postback_list
        if self.valuation_info:
            if hasattr(self.valuation_info, 'to_alipay_dict'):
                params['valuation_info'] = self.valuation_info.to_alipay_dict()
            else:
                params['valuation_info'] = self.valuation_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinInstinfoNotifyModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'car_info' in d:
            o.car_info = d['car_info']
        if 'file_list' in d:
            o.file_list = d['file_list']
        if 'out_apply_no' in d:
            o.out_apply_no = d['out_apply_no']
        if 'postback_list' in d:
            o.postback_list = d['postback_list']
        if 'valuation_info' in d:
            o.valuation_info = d['valuation_info']
        return o



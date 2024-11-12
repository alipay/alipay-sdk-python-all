#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpReportDataInfo import EpReportDataInfo


class ZhimaCreditEpDataReceiveModel(object):

    def __init__(self):
        self._data_info = None
        self._ep_cert_no = None
        self._ep_name = None
        self._order_no = None
        self._order_type = None

    @property
    def data_info(self):
        return self._data_info

    @data_info.setter
    def data_info(self, value):
        if isinstance(value, list):
            self._data_info = list()
            for i in value:
                if isinstance(i, EpReportDataInfo):
                    self._data_info.append(i)
                else:
                    self._data_info.append(EpReportDataInfo.from_alipay_dict(i))
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_info:
            if isinstance(self.data_info, list):
                for i in range(0, len(self.data_info)):
                    element = self.data_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data_info[i] = element.to_alipay_dict()
            if hasattr(self.data_info, 'to_alipay_dict'):
                params['data_info'] = self.data_info.to_alipay_dict()
            else:
                params['data_info'] = self.data_info
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpDataReceiveModel()
        if 'data_info' in d:
            o.data_info = d['data_info']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_type' in d:
            o.order_type = d['order_type']
        return o



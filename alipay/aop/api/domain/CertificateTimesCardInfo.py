#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CertificateSerialInfo import CertificateSerialInfo


class CertificateTimesCardInfo(object):

    def __init__(self):
        self._serial_info_list = None
        self._total_count = None
        self._used_count = None

    @property
    def serial_info_list(self):
        return self._serial_info_list

    @serial_info_list.setter
    def serial_info_list(self, value):
        if isinstance(value, list):
            self._serial_info_list = list()
            for i in value:
                if isinstance(i, CertificateSerialInfo):
                    self._serial_info_list.append(i)
                else:
                    self._serial_info_list.append(CertificateSerialInfo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def used_count(self):
        return self._used_count

    @used_count.setter
    def used_count(self, value):
        self._used_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.serial_info_list:
            if isinstance(self.serial_info_list, list):
                for i in range(0, len(self.serial_info_list)):
                    element = self.serial_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.serial_info_list[i] = element.to_alipay_dict()
            if hasattr(self.serial_info_list, 'to_alipay_dict'):
                params['serial_info_list'] = self.serial_info_list.to_alipay_dict()
            else:
                params['serial_info_list'] = self.serial_info_list
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.used_count:
            if hasattr(self.used_count, 'to_alipay_dict'):
                params['used_count'] = self.used_count.to_alipay_dict()
            else:
                params['used_count'] = self.used_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateTimesCardInfo()
        if 'serial_info_list' in d:
            o.serial_info_list = d['serial_info_list']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'used_count' in d:
            o.used_count = d['used_count']
        return o



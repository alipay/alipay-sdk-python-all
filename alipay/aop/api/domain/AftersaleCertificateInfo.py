#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AftersaleSerialInfo import AftersaleSerialInfo


class AftersaleCertificateInfo(object):

    def __init__(self):
        self._aftersale_serial_info_vo_list = None
        self._certificate_id = None

    @property
    def aftersale_serial_info_vo_list(self):
        return self._aftersale_serial_info_vo_list

    @aftersale_serial_info_vo_list.setter
    def aftersale_serial_info_vo_list(self, value):
        if isinstance(value, list):
            self._aftersale_serial_info_vo_list = list()
            for i in value:
                if isinstance(i, AftersaleSerialInfo):
                    self._aftersale_serial_info_vo_list.append(i)
                else:
                    self._aftersale_serial_info_vo_list.append(AftersaleSerialInfo.from_alipay_dict(i))
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aftersale_serial_info_vo_list:
            if isinstance(self.aftersale_serial_info_vo_list, list):
                for i in range(0, len(self.aftersale_serial_info_vo_list)):
                    element = self.aftersale_serial_info_vo_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.aftersale_serial_info_vo_list[i] = element.to_alipay_dict()
            if hasattr(self.aftersale_serial_info_vo_list, 'to_alipay_dict'):
                params['aftersale_serial_info_vo_list'] = self.aftersale_serial_info_vo_list.to_alipay_dict()
            else:
                params['aftersale_serial_info_vo_list'] = self.aftersale_serial_info_vo_list
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AftersaleCertificateInfo()
        if 'aftersale_serial_info_vo_list' in d:
            o.aftersale_serial_info_vo_list = d['aftersale_serial_info_vo_list']
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        return o



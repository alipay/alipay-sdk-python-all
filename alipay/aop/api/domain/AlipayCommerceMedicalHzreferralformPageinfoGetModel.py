#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHzreferralformPageinfoGetModel(object):

    def __init__(self):
        self._doctor_cert_no = None
        self._page_num = None
        self._page_size = None
        self._source = None
        self._status_list = None

    @property
    def doctor_cert_no(self):
        return self._doctor_cert_no

    @doctor_cert_no.setter
    def doctor_cert_no(self, value):
        self._doctor_cert_no = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status_list(self):
        return self._status_list

    @status_list.setter
    def status_list(self, value):
        if isinstance(value, list):
            self._status_list = list()
            for i in value:
                self._status_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_cert_no:
            if hasattr(self.doctor_cert_no, 'to_alipay_dict'):
                params['doctor_cert_no'] = self.doctor_cert_no.to_alipay_dict()
            else:
                params['doctor_cert_no'] = self.doctor_cert_no
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.status_list:
            if isinstance(self.status_list, list):
                for i in range(0, len(self.status_list)):
                    element = self.status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status_list[i] = element.to_alipay_dict()
            if hasattr(self.status_list, 'to_alipay_dict'):
                params['status_list'] = self.status_list.to_alipay_dict()
            else:
                params['status_list'] = self.status_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHzreferralformPageinfoGetModel()
        if 'doctor_cert_no' in d:
            o.doctor_cert_no = d['doctor_cert_no']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'source' in d:
            o.source = d['source']
        if 'status_list' in d:
            o.status_list = d['status_list']
        return o



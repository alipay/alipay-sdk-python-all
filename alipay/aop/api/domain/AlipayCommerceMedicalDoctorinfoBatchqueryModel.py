#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalDoctorinfoBatchqueryModel(object):

    def __init__(self):
        self._doctorid_list = None

    @property
    def doctorid_list(self):
        return self._doctorid_list

    @doctorid_list.setter
    def doctorid_list(self, value):
        if isinstance(value, list):
            self._doctorid_list = list()
            for i in value:
                self._doctorid_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.doctorid_list:
            if isinstance(self.doctorid_list, list):
                for i in range(0, len(self.doctorid_list)):
                    element = self.doctorid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.doctorid_list[i] = element.to_alipay_dict()
            if hasattr(self.doctorid_list, 'to_alipay_dict'):
                params['doctorid_list'] = self.doctorid_list.to_alipay_dict()
            else:
                params['doctorid_list'] = self.doctorid_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalDoctorinfoBatchqueryModel()
        if 'doctorid_list' in d:
            o.doctorid_list = d['doctorid_list']
        return o



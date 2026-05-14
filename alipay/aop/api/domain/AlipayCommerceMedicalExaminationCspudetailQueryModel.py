#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalExaminationCspudetailQueryModel(object):

    def __init__(self):
        self._spu_id_list = None

    @property
    def spu_id_list(self):
        return self._spu_id_list

    @spu_id_list.setter
    def spu_id_list(self, value):
        if isinstance(value, list):
            self._spu_id_list = list()
            for i in value:
                self._spu_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.spu_id_list:
            if isinstance(self.spu_id_list, list):
                for i in range(0, len(self.spu_id_list)):
                    element = self.spu_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.spu_id_list[i] = element.to_alipay_dict()
            if hasattr(self.spu_id_list, 'to_alipay_dict'):
                params['spu_id_list'] = self.spu_id_list.to_alipay_dict()
            else:
                params['spu_id_list'] = self.spu_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalExaminationCspudetailQueryModel()
        if 'spu_id_list' in d:
            o.spu_id_list = d['spu_id_list']
        return o



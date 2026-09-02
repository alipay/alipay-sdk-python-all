#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FulfillmentItemInfoDTO import FulfillmentItemInfoDTO


class FulfillmentReportInfoDTO(object):

    def __init__(self):
        self._file_id = None
        self._item_infos = None
        self._patient_id = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, FulfillmentItemInfoDTO):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(FulfillmentItemInfoDTO.from_alipay_dict(i))
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.item_infos:
            if isinstance(self.item_infos, list):
                for i in range(0, len(self.item_infos)):
                    element = self.item_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_infos[i] = element.to_alipay_dict()
            if hasattr(self.item_infos, 'to_alipay_dict'):
                params['item_infos'] = self.item_infos.to_alipay_dict()
            else:
                params['item_infos'] = self.item_infos
        if self.patient_id:
            if hasattr(self.patient_id, 'to_alipay_dict'):
                params['patient_id'] = self.patient_id.to_alipay_dict()
            else:
                params['patient_id'] = self.patient_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FulfillmentReportInfoDTO()
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'item_infos' in d:
            o.item_infos = d['item_infos']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntdataassetsOdpsColumn import AntdataassetsOdpsColumn


class AlipayDataDataserviceAntdataassetsUploadjobCreateModel(object):

    def __init__(self):
        self._guid = None
        self._odps_columns = None

    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, value):
        self._guid = value
    @property
    def odps_columns(self):
        return self._odps_columns

    @odps_columns.setter
    def odps_columns(self, value):
        if isinstance(value, list):
            self._odps_columns = list()
            for i in value:
                if isinstance(i, AntdataassetsOdpsColumn):
                    self._odps_columns.append(i)
                else:
                    self._odps_columns.append(AntdataassetsOdpsColumn.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.guid:
            if hasattr(self.guid, 'to_alipay_dict'):
                params['guid'] = self.guid.to_alipay_dict()
            else:
                params['guid'] = self.guid
        if self.odps_columns:
            if isinstance(self.odps_columns, list):
                for i in range(0, len(self.odps_columns)):
                    element = self.odps_columns[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.odps_columns[i] = element.to_alipay_dict()
            if hasattr(self.odps_columns, 'to_alipay_dict'):
                params['odps_columns'] = self.odps_columns.to_alipay_dict()
            else:
                params['odps_columns'] = self.odps_columns
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAntdataassetsUploadjobCreateModel()
        if 'guid' in d:
            o.guid = d['guid']
        if 'odps_columns' in d:
            o.odps_columns = d['odps_columns']
        return o



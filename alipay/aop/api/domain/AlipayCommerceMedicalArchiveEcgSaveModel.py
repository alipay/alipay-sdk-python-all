#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcgReportDatail import EcgReportDatail


class AlipayCommerceMedicalArchiveEcgSaveModel(object):

    def __init__(self):
        self._access_token = None
        self._data_source = None
        self._data_type = None
        self._ecg_report_datail = None
        self._member_id = None
        self._open_id = None
        self._user_id = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def ecg_report_datail(self):
        return self._ecg_report_datail

    @ecg_report_datail.setter
    def ecg_report_datail(self, value):
        if isinstance(value, list):
            self._ecg_report_datail = list()
            for i in value:
                if isinstance(i, EcgReportDatail):
                    self._ecg_report_datail.append(i)
                else:
                    self._ecg_report_datail.append(EcgReportDatail.from_alipay_dict(i))
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_token:
            if hasattr(self.access_token, 'to_alipay_dict'):
                params['access_token'] = self.access_token.to_alipay_dict()
            else:
                params['access_token'] = self.access_token
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.ecg_report_datail:
            if isinstance(self.ecg_report_datail, list):
                for i in range(0, len(self.ecg_report_datail)):
                    element = self.ecg_report_datail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ecg_report_datail[i] = element.to_alipay_dict()
            if hasattr(self.ecg_report_datail, 'to_alipay_dict'):
                params['ecg_report_datail'] = self.ecg_report_datail.to_alipay_dict()
            else:
                params['ecg_report_datail'] = self.ecg_report_datail
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalArchiveEcgSaveModel()
        if 'access_token' in d:
            o.access_token = d['access_token']
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'ecg_report_datail' in d:
            o.ecg_report_datail = d['ecg_report_datail']
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ClaimStatusInfo import ClaimStatusInfo
from alipay.aop.api.domain.SerialInfo import SerialInfo


class AlipayCommerceMedicalInsuranceClaimModifyModel(object):

    def __init__(self):
        self._apply_no = None
        self._claim_no = None
        self._claim_status_info = None
        self._open_id = None
        self._serial_infos = None
        self._source = None
        self._user_id = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def claim_status_info(self):
        return self._claim_status_info

    @claim_status_info.setter
    def claim_status_info(self, value):
        if isinstance(value, ClaimStatusInfo):
            self._claim_status_info = value
        else:
            self._claim_status_info = ClaimStatusInfo.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def serial_infos(self):
        return self._serial_infos

    @serial_infos.setter
    def serial_infos(self, value):
        if isinstance(value, list):
            self._serial_infos = list()
            for i in value:
                if isinstance(i, SerialInfo):
                    self._serial_infos.append(i)
                else:
                    self._serial_infos.append(SerialInfo.from_alipay_dict(i))
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.claim_status_info:
            if hasattr(self.claim_status_info, 'to_alipay_dict'):
                params['claim_status_info'] = self.claim_status_info.to_alipay_dict()
            else:
                params['claim_status_info'] = self.claim_status_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.serial_infos:
            if isinstance(self.serial_infos, list):
                for i in range(0, len(self.serial_infos)):
                    element = self.serial_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.serial_infos[i] = element.to_alipay_dict()
            if hasattr(self.serial_infos, 'to_alipay_dict'):
                params['serial_infos'] = self.serial_infos.to_alipay_dict()
            else:
                params['serial_infos'] = self.serial_infos
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipayCommerceMedicalInsuranceClaimModifyModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'claim_status_info' in d:
            o.claim_status_info = d['claim_status_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'serial_infos' in d:
            o.serial_infos = d['serial_infos']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



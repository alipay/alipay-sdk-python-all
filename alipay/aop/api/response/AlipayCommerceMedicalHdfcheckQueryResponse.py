#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GetInspectionDetailDiagnosisInfo import GetInspectionDetailDiagnosisInfo
from alipay.aop.api.domain.GetInspectionDetailItemInfo import GetInspectionDetailItemInfo


class AlipayCommerceMedicalHdfcheckQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfcheckQueryResponse, self).__init__()
        self._apply_department_name = None
        self._apply_time = None
        self._diagnosis_info = None
        self._hdf_check_no = None
        self._hdf_user_age = None
        self._hdf_user_mb = None
        self._hdf_user_name = None
        self._hdf_user_no = None
        self._hdf_user_sex = None
        self._item_info_list = None

    @property
    def apply_department_name(self):
        return self._apply_department_name

    @apply_department_name.setter
    def apply_department_name(self, value):
        self._apply_department_name = value
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def diagnosis_info(self):
        return self._diagnosis_info

    @diagnosis_info.setter
    def diagnosis_info(self, value):
        if isinstance(value, GetInspectionDetailDiagnosisInfo):
            self._diagnosis_info = value
        else:
            self._diagnosis_info = GetInspectionDetailDiagnosisInfo.from_alipay_dict(value)
    @property
    def hdf_check_no(self):
        return self._hdf_check_no

    @hdf_check_no.setter
    def hdf_check_no(self, value):
        self._hdf_check_no = value
    @property
    def hdf_user_age(self):
        return self._hdf_user_age

    @hdf_user_age.setter
    def hdf_user_age(self, value):
        self._hdf_user_age = value
    @property
    def hdf_user_mb(self):
        return self._hdf_user_mb

    @hdf_user_mb.setter
    def hdf_user_mb(self, value):
        self._hdf_user_mb = value
    @property
    def hdf_user_name(self):
        return self._hdf_user_name

    @hdf_user_name.setter
    def hdf_user_name(self, value):
        self._hdf_user_name = value
    @property
    def hdf_user_no(self):
        return self._hdf_user_no

    @hdf_user_no.setter
    def hdf_user_no(self, value):
        self._hdf_user_no = value
    @property
    def hdf_user_sex(self):
        return self._hdf_user_sex

    @hdf_user_sex.setter
    def hdf_user_sex(self, value):
        self._hdf_user_sex = value
    @property
    def item_info_list(self):
        return self._item_info_list

    @item_info_list.setter
    def item_info_list(self, value):
        if isinstance(value, list):
            self._item_info_list = list()
            for i in value:
                if isinstance(i, GetInspectionDetailItemInfo):
                    self._item_info_list.append(i)
                else:
                    self._item_info_list.append(GetInspectionDetailItemInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfcheckQueryResponse, self).parse_response_content(response_content)
        if 'apply_department_name' in response:
            self.apply_department_name = response['apply_department_name']
        if 'apply_time' in response:
            self.apply_time = response['apply_time']
        if 'diagnosis_info' in response:
            self.diagnosis_info = response['diagnosis_info']
        if 'hdf_check_no' in response:
            self.hdf_check_no = response['hdf_check_no']
        if 'hdf_user_age' in response:
            self.hdf_user_age = response['hdf_user_age']
        if 'hdf_user_mb' in response:
            self.hdf_user_mb = response['hdf_user_mb']
        if 'hdf_user_name' in response:
            self.hdf_user_name = response['hdf_user_name']
        if 'hdf_user_no' in response:
            self.hdf_user_no = response['hdf_user_no']
        if 'hdf_user_sex' in response:
            self.hdf_user_sex = response['hdf_user_sex']
        if 'item_info_list' in response:
            self.item_info_list = response['item_info_list']

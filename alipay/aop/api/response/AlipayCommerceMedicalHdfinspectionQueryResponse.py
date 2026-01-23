#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHdfinspectionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfinspectionQueryResponse, self).__init__()
        self._hdf_check_no = None
        self._hdf_user_age = None
        self._hdf_user_mb = None
        self._hdf_user_name = None
        self._hdf_user_no = None
        self._hdf_user_sex = None
        self._inspection_item_sku_ids = None
        self._inspection_package_sku_ids = None

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
    def inspection_item_sku_ids(self):
        return self._inspection_item_sku_ids

    @inspection_item_sku_ids.setter
    def inspection_item_sku_ids(self, value):
        self._inspection_item_sku_ids = value
    @property
    def inspection_package_sku_ids(self):
        return self._inspection_package_sku_ids

    @inspection_package_sku_ids.setter
    def inspection_package_sku_ids(self, value):
        self._inspection_package_sku_ids = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfinspectionQueryResponse, self).parse_response_content(response_content)
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
        if 'inspection_item_sku_ids' in response:
            self.inspection_item_sku_ids = response['inspection_item_sku_ids']
        if 'inspection_package_sku_ids' in response:
            self.inspection_package_sku_ids = response['inspection_package_sku_ids']

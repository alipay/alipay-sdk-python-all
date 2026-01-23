#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HDFMedicalRecordInfo import HDFMedicalRecordInfo
from alipay.aop.api.domain.HDFPatientInfo import HDFPatientInfo


class AlipayCommerceMedicalOuterorderCreateModel(object):

    def __init__(self):
        self._biz_identity = None
        self._consult_business = None
        self._fulfillment_order_id = None
        self._hdf_user = None
        self._medical_record_info_list = None
        self._partner_user = None
        self._patient_info = None
        self._transer_info = None

    @property
    def biz_identity(self):
        return self._biz_identity

    @biz_identity.setter
    def biz_identity(self, value):
        self._biz_identity = value
    @property
    def consult_business(self):
        return self._consult_business

    @consult_business.setter
    def consult_business(self, value):
        self._consult_business = value
    @property
    def fulfillment_order_id(self):
        return self._fulfillment_order_id

    @fulfillment_order_id.setter
    def fulfillment_order_id(self, value):
        self._fulfillment_order_id = value
    @property
    def hdf_user(self):
        return self._hdf_user

    @hdf_user.setter
    def hdf_user(self, value):
        self._hdf_user = value
    @property
    def medical_record_info_list(self):
        return self._medical_record_info_list

    @medical_record_info_list.setter
    def medical_record_info_list(self, value):
        if isinstance(value, list):
            self._medical_record_info_list = list()
            for i in value:
                if isinstance(i, HDFMedicalRecordInfo):
                    self._medical_record_info_list.append(i)
                else:
                    self._medical_record_info_list.append(HDFMedicalRecordInfo.from_alipay_dict(i))
    @property
    def partner_user(self):
        return self._partner_user

    @partner_user.setter
    def partner_user(self, value):
        self._partner_user = value
    @property
    def patient_info(self):
        return self._patient_info

    @patient_info.setter
    def patient_info(self, value):
        if isinstance(value, HDFPatientInfo):
            self._patient_info = value
        else:
            self._patient_info = HDFPatientInfo.from_alipay_dict(value)
    @property
    def transer_info(self):
        return self._transer_info

    @transer_info.setter
    def transer_info(self, value):
        self._transer_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_identity:
            if hasattr(self.biz_identity, 'to_alipay_dict'):
                params['biz_identity'] = self.biz_identity.to_alipay_dict()
            else:
                params['biz_identity'] = self.biz_identity
        if self.consult_business:
            if hasattr(self.consult_business, 'to_alipay_dict'):
                params['consult_business'] = self.consult_business.to_alipay_dict()
            else:
                params['consult_business'] = self.consult_business
        if self.fulfillment_order_id:
            if hasattr(self.fulfillment_order_id, 'to_alipay_dict'):
                params['fulfillment_order_id'] = self.fulfillment_order_id.to_alipay_dict()
            else:
                params['fulfillment_order_id'] = self.fulfillment_order_id
        if self.hdf_user:
            if hasattr(self.hdf_user, 'to_alipay_dict'):
                params['hdf_user'] = self.hdf_user.to_alipay_dict()
            else:
                params['hdf_user'] = self.hdf_user
        if self.medical_record_info_list:
            if isinstance(self.medical_record_info_list, list):
                for i in range(0, len(self.medical_record_info_list)):
                    element = self.medical_record_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.medical_record_info_list[i] = element.to_alipay_dict()
            if hasattr(self.medical_record_info_list, 'to_alipay_dict'):
                params['medical_record_info_list'] = self.medical_record_info_list.to_alipay_dict()
            else:
                params['medical_record_info_list'] = self.medical_record_info_list
        if self.partner_user:
            if hasattr(self.partner_user, 'to_alipay_dict'):
                params['partner_user'] = self.partner_user.to_alipay_dict()
            else:
                params['partner_user'] = self.partner_user
        if self.patient_info:
            if hasattr(self.patient_info, 'to_alipay_dict'):
                params['patient_info'] = self.patient_info.to_alipay_dict()
            else:
                params['patient_info'] = self.patient_info
        if self.transer_info:
            if hasattr(self.transer_info, 'to_alipay_dict'):
                params['transer_info'] = self.transer_info.to_alipay_dict()
            else:
                params['transer_info'] = self.transer_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalOuterorderCreateModel()
        if 'biz_identity' in d:
            o.biz_identity = d['biz_identity']
        if 'consult_business' in d:
            o.consult_business = d['consult_business']
        if 'fulfillment_order_id' in d:
            o.fulfillment_order_id = d['fulfillment_order_id']
        if 'hdf_user' in d:
            o.hdf_user = d['hdf_user']
        if 'medical_record_info_list' in d:
            o.medical_record_info_list = d['medical_record_info_list']
        if 'partner_user' in d:
            o.partner_user = d['partner_user']
        if 'patient_info' in d:
            o.patient_info = d['patient_info']
        if 'transer_info' in d:
            o.transer_info = d['transer_info']
        return o



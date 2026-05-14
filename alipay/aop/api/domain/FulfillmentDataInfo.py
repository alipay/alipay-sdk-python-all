#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsultationParam import ConsultationParam
from alipay.aop.api.domain.ExaminationParam import ExaminationParam
from alipay.aop.api.domain.InpatientNursingFulfillmentDetailData import InpatientNursingFulfillmentDetailData
from alipay.aop.api.domain.OfflineEscortFulfillmentDetailData import OfflineEscortFulfillmentDetailData


class FulfillmentDataInfo(object):

    def __init__(self):
        self._consultation = None
        self._examination = None
        self._inpatient_nursing_fulfillment_detail_data = None
        self._offline_escort_fulfillment_detail_data = None

    @property
    def consultation(self):
        return self._consultation

    @consultation.setter
    def consultation(self, value):
        if isinstance(value, ConsultationParam):
            self._consultation = value
        else:
            self._consultation = ConsultationParam.from_alipay_dict(value)
    @property
    def examination(self):
        return self._examination

    @examination.setter
    def examination(self, value):
        if isinstance(value, ExaminationParam):
            self._examination = value
        else:
            self._examination = ExaminationParam.from_alipay_dict(value)
    @property
    def inpatient_nursing_fulfillment_detail_data(self):
        return self._inpatient_nursing_fulfillment_detail_data

    @inpatient_nursing_fulfillment_detail_data.setter
    def inpatient_nursing_fulfillment_detail_data(self, value):
        if isinstance(value, InpatientNursingFulfillmentDetailData):
            self._inpatient_nursing_fulfillment_detail_data = value
        else:
            self._inpatient_nursing_fulfillment_detail_data = InpatientNursingFulfillmentDetailData.from_alipay_dict(value)
    @property
    def offline_escort_fulfillment_detail_data(self):
        return self._offline_escort_fulfillment_detail_data

    @offline_escort_fulfillment_detail_data.setter
    def offline_escort_fulfillment_detail_data(self, value):
        if isinstance(value, OfflineEscortFulfillmentDetailData):
            self._offline_escort_fulfillment_detail_data = value
        else:
            self._offline_escort_fulfillment_detail_data = OfflineEscortFulfillmentDetailData.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.consultation:
            if hasattr(self.consultation, 'to_alipay_dict'):
                params['consultation'] = self.consultation.to_alipay_dict()
            else:
                params['consultation'] = self.consultation
        if self.examination:
            if hasattr(self.examination, 'to_alipay_dict'):
                params['examination'] = self.examination.to_alipay_dict()
            else:
                params['examination'] = self.examination
        if self.inpatient_nursing_fulfillment_detail_data:
            if hasattr(self.inpatient_nursing_fulfillment_detail_data, 'to_alipay_dict'):
                params['inpatient_nursing_fulfillment_detail_data'] = self.inpatient_nursing_fulfillment_detail_data.to_alipay_dict()
            else:
                params['inpatient_nursing_fulfillment_detail_data'] = self.inpatient_nursing_fulfillment_detail_data
        if self.offline_escort_fulfillment_detail_data:
            if hasattr(self.offline_escort_fulfillment_detail_data, 'to_alipay_dict'):
                params['offline_escort_fulfillment_detail_data'] = self.offline_escort_fulfillment_detail_data.to_alipay_dict()
            else:
                params['offline_escort_fulfillment_detail_data'] = self.offline_escort_fulfillment_detail_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FulfillmentDataInfo()
        if 'consultation' in d:
            o.consultation = d['consultation']
        if 'examination' in d:
            o.examination = d['examination']
        if 'inpatient_nursing_fulfillment_detail_data' in d:
            o.inpatient_nursing_fulfillment_detail_data = d['inpatient_nursing_fulfillment_detail_data']
        if 'offline_escort_fulfillment_detail_data' in d:
            o.offline_escort_fulfillment_detail_data = d['offline_escort_fulfillment_detail_data']
        return o



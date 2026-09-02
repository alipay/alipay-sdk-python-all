#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdvisorParam import AdvisorParam
from alipay.aop.api.domain.ConsultationParam import ConsultationParam
from alipay.aop.api.domain.ExaminationParam import ExaminationParam
from alipay.aop.api.domain.ExaminationUrgentFulfillmentDetailData import ExaminationUrgentFulfillmentDetailData
from alipay.aop.api.domain.HighEndMedicalFulfillmentDetailData import HighEndMedicalFulfillmentDetailData
from alipay.aop.api.domain.InpatientAssistFulfillmentDetailData import InpatientAssistFulfillmentDetailData
from alipay.aop.api.domain.InpatientNursingFulfillmentDetailData import InpatientNursingFulfillmentDetailData
from alipay.aop.api.domain.OfflineEscortFulfillmentDetailData import OfflineEscortFulfillmentDetailData
from alipay.aop.api.domain.PhysicalExaminationFulfillmentDetailData import PhysicalExaminationFulfillmentDetailData
from alipay.aop.api.domain.PsychologicalFulfillmentDetailData import PsychologicalFulfillmentDetailData
from alipay.aop.api.domain.RegistrationGreenChannelFulfillmentDetailData import RegistrationGreenChannelFulfillmentDetailData


class FulfillmentDataInfo(object):

    def __init__(self):
        self._advisor = None
        self._consultation = None
        self._examination = None
        self._examination_urgent_fulfillment_detail_data = None
        self._highend_medical_fulfillment_detail_data = None
        self._inpatient_assist_fulfillment_detail_data = None
        self._inpatient_nursing_fulfillment_detail_data = None
        self._offline_escort_fulfillment_detail_data = None
        self._physical_examination_fulfillment_detail_data = None
        self._psychological_fulfillment_detail_data = None
        self._registration_green_channel_fulfillment_detail_data = None

    @property
    def advisor(self):
        return self._advisor

    @advisor.setter
    def advisor(self, value):
        if isinstance(value, AdvisorParam):
            self._advisor = value
        else:
            self._advisor = AdvisorParam.from_alipay_dict(value)
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
    def examination_urgent_fulfillment_detail_data(self):
        return self._examination_urgent_fulfillment_detail_data

    @examination_urgent_fulfillment_detail_data.setter
    def examination_urgent_fulfillment_detail_data(self, value):
        if isinstance(value, ExaminationUrgentFulfillmentDetailData):
            self._examination_urgent_fulfillment_detail_data = value
        else:
            self._examination_urgent_fulfillment_detail_data = ExaminationUrgentFulfillmentDetailData.from_alipay_dict(value)
    @property
    def highend_medical_fulfillment_detail_data(self):
        return self._highend_medical_fulfillment_detail_data

    @highend_medical_fulfillment_detail_data.setter
    def highend_medical_fulfillment_detail_data(self, value):
        if isinstance(value, HighEndMedicalFulfillmentDetailData):
            self._highend_medical_fulfillment_detail_data = value
        else:
            self._highend_medical_fulfillment_detail_data = HighEndMedicalFulfillmentDetailData.from_alipay_dict(value)
    @property
    def inpatient_assist_fulfillment_detail_data(self):
        return self._inpatient_assist_fulfillment_detail_data

    @inpatient_assist_fulfillment_detail_data.setter
    def inpatient_assist_fulfillment_detail_data(self, value):
        if isinstance(value, InpatientAssistFulfillmentDetailData):
            self._inpatient_assist_fulfillment_detail_data = value
        else:
            self._inpatient_assist_fulfillment_detail_data = InpatientAssistFulfillmentDetailData.from_alipay_dict(value)
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
    @property
    def physical_examination_fulfillment_detail_data(self):
        return self._physical_examination_fulfillment_detail_data

    @physical_examination_fulfillment_detail_data.setter
    def physical_examination_fulfillment_detail_data(self, value):
        if isinstance(value, PhysicalExaminationFulfillmentDetailData):
            self._physical_examination_fulfillment_detail_data = value
        else:
            self._physical_examination_fulfillment_detail_data = PhysicalExaminationFulfillmentDetailData.from_alipay_dict(value)
    @property
    def psychological_fulfillment_detail_data(self):
        return self._psychological_fulfillment_detail_data

    @psychological_fulfillment_detail_data.setter
    def psychological_fulfillment_detail_data(self, value):
        if isinstance(value, PsychologicalFulfillmentDetailData):
            self._psychological_fulfillment_detail_data = value
        else:
            self._psychological_fulfillment_detail_data = PsychologicalFulfillmentDetailData.from_alipay_dict(value)
    @property
    def registration_green_channel_fulfillment_detail_data(self):
        return self._registration_green_channel_fulfillment_detail_data

    @registration_green_channel_fulfillment_detail_data.setter
    def registration_green_channel_fulfillment_detail_data(self, value):
        if isinstance(value, RegistrationGreenChannelFulfillmentDetailData):
            self._registration_green_channel_fulfillment_detail_data = value
        else:
            self._registration_green_channel_fulfillment_detail_data = RegistrationGreenChannelFulfillmentDetailData.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.advisor:
            if hasattr(self.advisor, 'to_alipay_dict'):
                params['advisor'] = self.advisor.to_alipay_dict()
            else:
                params['advisor'] = self.advisor
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
        if self.examination_urgent_fulfillment_detail_data:
            if hasattr(self.examination_urgent_fulfillment_detail_data, 'to_alipay_dict'):
                params['examination_urgent_fulfillment_detail_data'] = self.examination_urgent_fulfillment_detail_data.to_alipay_dict()
            else:
                params['examination_urgent_fulfillment_detail_data'] = self.examination_urgent_fulfillment_detail_data
        if self.highend_medical_fulfillment_detail_data:
            if hasattr(self.highend_medical_fulfillment_detail_data, 'to_alipay_dict'):
                params['highend_medical_fulfillment_detail_data'] = self.highend_medical_fulfillment_detail_data.to_alipay_dict()
            else:
                params['highend_medical_fulfillment_detail_data'] = self.highend_medical_fulfillment_detail_data
        if self.inpatient_assist_fulfillment_detail_data:
            if hasattr(self.inpatient_assist_fulfillment_detail_data, 'to_alipay_dict'):
                params['inpatient_assist_fulfillment_detail_data'] = self.inpatient_assist_fulfillment_detail_data.to_alipay_dict()
            else:
                params['inpatient_assist_fulfillment_detail_data'] = self.inpatient_assist_fulfillment_detail_data
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
        if self.physical_examination_fulfillment_detail_data:
            if hasattr(self.physical_examination_fulfillment_detail_data, 'to_alipay_dict'):
                params['physical_examination_fulfillment_detail_data'] = self.physical_examination_fulfillment_detail_data.to_alipay_dict()
            else:
                params['physical_examination_fulfillment_detail_data'] = self.physical_examination_fulfillment_detail_data
        if self.psychological_fulfillment_detail_data:
            if hasattr(self.psychological_fulfillment_detail_data, 'to_alipay_dict'):
                params['psychological_fulfillment_detail_data'] = self.psychological_fulfillment_detail_data.to_alipay_dict()
            else:
                params['psychological_fulfillment_detail_data'] = self.psychological_fulfillment_detail_data
        if self.registration_green_channel_fulfillment_detail_data:
            if hasattr(self.registration_green_channel_fulfillment_detail_data, 'to_alipay_dict'):
                params['registration_green_channel_fulfillment_detail_data'] = self.registration_green_channel_fulfillment_detail_data.to_alipay_dict()
            else:
                params['registration_green_channel_fulfillment_detail_data'] = self.registration_green_channel_fulfillment_detail_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FulfillmentDataInfo()
        if 'advisor' in d:
            o.advisor = d['advisor']
        if 'consultation' in d:
            o.consultation = d['consultation']
        if 'examination' in d:
            o.examination = d['examination']
        if 'examination_urgent_fulfillment_detail_data' in d:
            o.examination_urgent_fulfillment_detail_data = d['examination_urgent_fulfillment_detail_data']
        if 'highend_medical_fulfillment_detail_data' in d:
            o.highend_medical_fulfillment_detail_data = d['highend_medical_fulfillment_detail_data']
        if 'inpatient_assist_fulfillment_detail_data' in d:
            o.inpatient_assist_fulfillment_detail_data = d['inpatient_assist_fulfillment_detail_data']
        if 'inpatient_nursing_fulfillment_detail_data' in d:
            o.inpatient_nursing_fulfillment_detail_data = d['inpatient_nursing_fulfillment_detail_data']
        if 'offline_escort_fulfillment_detail_data' in d:
            o.offline_escort_fulfillment_detail_data = d['offline_escort_fulfillment_detail_data']
        if 'physical_examination_fulfillment_detail_data' in d:
            o.physical_examination_fulfillment_detail_data = d['physical_examination_fulfillment_detail_data']
        if 'psychological_fulfillment_detail_data' in d:
            o.psychological_fulfillment_detail_data = d['psychological_fulfillment_detail_data']
        if 'registration_green_channel_fulfillment_detail_data' in d:
            o.registration_green_channel_fulfillment_detail_data = d['registration_green_channel_fulfillment_detail_data']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Advisory import Advisory
from alipay.aop.api.domain.Consultation import Consultation
from alipay.aop.api.domain.EscortVO import EscortVO
from alipay.aop.api.domain.Examination import Examination
from alipay.aop.api.domain.FulfillmentBizVO import FulfillmentBizVO
from alipay.aop.api.domain.HighEndMedicalFulfillmentDetailData import HighEndMedicalFulfillmentDetailData
from alipay.aop.api.domain.FulfillmentBizVO import FulfillmentBizVO
from alipay.aop.api.domain.NursingVO import NursingVO
from alipay.aop.api.domain.FulfillmentBizVO import FulfillmentBizVO
from alipay.aop.api.domain.PsychologicalVO import PsychologicalVO
from alipay.aop.api.domain.FulfillmentBizVO import FulfillmentBizVO


class FulfillmentBizInfo(object):

    def __init__(self):
        self._advisory = None
        self._consultation = None
        self._escort = None
        self._examination = None
        self._examination_urgent = None
        self._highend_medical = None
        self._inpatient_assist = None
        self._nursing = None
        self._physical_examination = None
        self._psychological = None
        self._registration_green_channel = None

    @property
    def advisory(self):
        return self._advisory

    @advisory.setter
    def advisory(self, value):
        if isinstance(value, Advisory):
            self._advisory = value
        else:
            self._advisory = Advisory.from_alipay_dict(value)
    @property
    def consultation(self):
        return self._consultation

    @consultation.setter
    def consultation(self, value):
        if isinstance(value, Consultation):
            self._consultation = value
        else:
            self._consultation = Consultation.from_alipay_dict(value)
    @property
    def escort(self):
        return self._escort

    @escort.setter
    def escort(self, value):
        if isinstance(value, EscortVO):
            self._escort = value
        else:
            self._escort = EscortVO.from_alipay_dict(value)
    @property
    def examination(self):
        return self._examination

    @examination.setter
    def examination(self, value):
        if isinstance(value, Examination):
            self._examination = value
        else:
            self._examination = Examination.from_alipay_dict(value)
    @property
    def examination_urgent(self):
        return self._examination_urgent

    @examination_urgent.setter
    def examination_urgent(self, value):
        if isinstance(value, FulfillmentBizVO):
            self._examination_urgent = value
        else:
            self._examination_urgent = FulfillmentBizVO.from_alipay_dict(value)
    @property
    def highend_medical(self):
        return self._highend_medical

    @highend_medical.setter
    def highend_medical(self, value):
        if isinstance(value, HighEndMedicalFulfillmentDetailData):
            self._highend_medical = value
        else:
            self._highend_medical = HighEndMedicalFulfillmentDetailData.from_alipay_dict(value)
    @property
    def inpatient_assist(self):
        return self._inpatient_assist

    @inpatient_assist.setter
    def inpatient_assist(self, value):
        if isinstance(value, FulfillmentBizVO):
            self._inpatient_assist = value
        else:
            self._inpatient_assist = FulfillmentBizVO.from_alipay_dict(value)
    @property
    def nursing(self):
        return self._nursing

    @nursing.setter
    def nursing(self, value):
        if isinstance(value, NursingVO):
            self._nursing = value
        else:
            self._nursing = NursingVO.from_alipay_dict(value)
    @property
    def physical_examination(self):
        return self._physical_examination

    @physical_examination.setter
    def physical_examination(self, value):
        if isinstance(value, FulfillmentBizVO):
            self._physical_examination = value
        else:
            self._physical_examination = FulfillmentBizVO.from_alipay_dict(value)
    @property
    def psychological(self):
        return self._psychological

    @psychological.setter
    def psychological(self, value):
        if isinstance(value, PsychologicalVO):
            self._psychological = value
        else:
            self._psychological = PsychologicalVO.from_alipay_dict(value)
    @property
    def registration_green_channel(self):
        return self._registration_green_channel

    @registration_green_channel.setter
    def registration_green_channel(self, value):
        if isinstance(value, FulfillmentBizVO):
            self._registration_green_channel = value
        else:
            self._registration_green_channel = FulfillmentBizVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.advisory:
            if hasattr(self.advisory, 'to_alipay_dict'):
                params['advisory'] = self.advisory.to_alipay_dict()
            else:
                params['advisory'] = self.advisory
        if self.consultation:
            if hasattr(self.consultation, 'to_alipay_dict'):
                params['consultation'] = self.consultation.to_alipay_dict()
            else:
                params['consultation'] = self.consultation
        if self.escort:
            if hasattr(self.escort, 'to_alipay_dict'):
                params['escort'] = self.escort.to_alipay_dict()
            else:
                params['escort'] = self.escort
        if self.examination:
            if hasattr(self.examination, 'to_alipay_dict'):
                params['examination'] = self.examination.to_alipay_dict()
            else:
                params['examination'] = self.examination
        if self.examination_urgent:
            if hasattr(self.examination_urgent, 'to_alipay_dict'):
                params['examination_urgent'] = self.examination_urgent.to_alipay_dict()
            else:
                params['examination_urgent'] = self.examination_urgent
        if self.highend_medical:
            if hasattr(self.highend_medical, 'to_alipay_dict'):
                params['highend_medical'] = self.highend_medical.to_alipay_dict()
            else:
                params['highend_medical'] = self.highend_medical
        if self.inpatient_assist:
            if hasattr(self.inpatient_assist, 'to_alipay_dict'):
                params['inpatient_assist'] = self.inpatient_assist.to_alipay_dict()
            else:
                params['inpatient_assist'] = self.inpatient_assist
        if self.nursing:
            if hasattr(self.nursing, 'to_alipay_dict'):
                params['nursing'] = self.nursing.to_alipay_dict()
            else:
                params['nursing'] = self.nursing
        if self.physical_examination:
            if hasattr(self.physical_examination, 'to_alipay_dict'):
                params['physical_examination'] = self.physical_examination.to_alipay_dict()
            else:
                params['physical_examination'] = self.physical_examination
        if self.psychological:
            if hasattr(self.psychological, 'to_alipay_dict'):
                params['psychological'] = self.psychological.to_alipay_dict()
            else:
                params['psychological'] = self.psychological
        if self.registration_green_channel:
            if hasattr(self.registration_green_channel, 'to_alipay_dict'):
                params['registration_green_channel'] = self.registration_green_channel.to_alipay_dict()
            else:
                params['registration_green_channel'] = self.registration_green_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FulfillmentBizInfo()
        if 'advisory' in d:
            o.advisory = d['advisory']
        if 'consultation' in d:
            o.consultation = d['consultation']
        if 'escort' in d:
            o.escort = d['escort']
        if 'examination' in d:
            o.examination = d['examination']
        if 'examination_urgent' in d:
            o.examination_urgent = d['examination_urgent']
        if 'highend_medical' in d:
            o.highend_medical = d['highend_medical']
        if 'inpatient_assist' in d:
            o.inpatient_assist = d['inpatient_assist']
        if 'nursing' in d:
            o.nursing = d['nursing']
        if 'physical_examination' in d:
            o.physical_examination = d['physical_examination']
        if 'psychological' in d:
            o.psychological = d['psychological']
        if 'registration_green_channel' in d:
            o.registration_green_channel = d['registration_green_channel']
        return o



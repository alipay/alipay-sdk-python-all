#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Informant import Informant
from alipay.aop.api.domain.Injured import Injured
from alipay.aop.api.domain.Insured import Insured
from alipay.aop.api.domain.ReportCar import ReportCar
from alipay.aop.api.domain.ReportCar import ReportCar


class AlipayInsDataAutoFraudQueryModel(object):

    def __init__(self):
        self._accident_city = None
        self._accident_date = None
        self._accident_location = None
        self._case_amount = None
        self._estimate_damage_amount = None
        self._informant = None
        self._injured_count = None
        self._injured_list = None
        self._insure_city = None
        self._insured = None
        self._policy_no = None
        self._report_date = None
        self._report_no = None
        self._request_no = None
        self._scene_type = None
        self._subject_car = None
        self._third_party_car_count = None
        self._third_party_car_list = None

    @property
    def accident_city(self):
        return self._accident_city

    @accident_city.setter
    def accident_city(self, value):
        self._accident_city = value
    @property
    def accident_date(self):
        return self._accident_date

    @accident_date.setter
    def accident_date(self, value):
        self._accident_date = value
    @property
    def accident_location(self):
        return self._accident_location

    @accident_location.setter
    def accident_location(self, value):
        self._accident_location = value
    @property
    def case_amount(self):
        return self._case_amount

    @case_amount.setter
    def case_amount(self, value):
        self._case_amount = value
    @property
    def estimate_damage_amount(self):
        return self._estimate_damage_amount

    @estimate_damage_amount.setter
    def estimate_damage_amount(self, value):
        self._estimate_damage_amount = value
    @property
    def informant(self):
        return self._informant

    @informant.setter
    def informant(self, value):
        if isinstance(value, Informant):
            self._informant = value
        else:
            self._informant = Informant.from_alipay_dict(value)
    @property
    def injured_count(self):
        return self._injured_count

    @injured_count.setter
    def injured_count(self, value):
        self._injured_count = value
    @property
    def injured_list(self):
        return self._injured_list

    @injured_list.setter
    def injured_list(self, value):
        if isinstance(value, list):
            self._injured_list = list()
            for i in value:
                if isinstance(i, Injured):
                    self._injured_list.append(i)
                else:
                    self._injured_list.append(Injured.from_alipay_dict(i))
    @property
    def insure_city(self):
        return self._insure_city

    @insure_city.setter
    def insure_city(self, value):
        self._insure_city = value
    @property
    def insured(self):
        return self._insured

    @insured.setter
    def insured(self, value):
        if isinstance(value, Insured):
            self._insured = value
        else:
            self._insured = Insured.from_alipay_dict(value)
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def report_no(self):
        return self._report_no

    @report_no.setter
    def report_no(self, value):
        self._report_no = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def subject_car(self):
        return self._subject_car

    @subject_car.setter
    def subject_car(self, value):
        if isinstance(value, ReportCar):
            self._subject_car = value
        else:
            self._subject_car = ReportCar.from_alipay_dict(value)
    @property
    def third_party_car_count(self):
        return self._third_party_car_count

    @third_party_car_count.setter
    def third_party_car_count(self, value):
        self._third_party_car_count = value
    @property
    def third_party_car_list(self):
        return self._third_party_car_list

    @third_party_car_list.setter
    def third_party_car_list(self, value):
        if isinstance(value, list):
            self._third_party_car_list = list()
            for i in value:
                if isinstance(i, ReportCar):
                    self._third_party_car_list.append(i)
                else:
                    self._third_party_car_list.append(ReportCar.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.accident_city:
            if hasattr(self.accident_city, 'to_alipay_dict'):
                params['accident_city'] = self.accident_city.to_alipay_dict()
            else:
                params['accident_city'] = self.accident_city
        if self.accident_date:
            if hasattr(self.accident_date, 'to_alipay_dict'):
                params['accident_date'] = self.accident_date.to_alipay_dict()
            else:
                params['accident_date'] = self.accident_date
        if self.accident_location:
            if hasattr(self.accident_location, 'to_alipay_dict'):
                params['accident_location'] = self.accident_location.to_alipay_dict()
            else:
                params['accident_location'] = self.accident_location
        if self.case_amount:
            if hasattr(self.case_amount, 'to_alipay_dict'):
                params['case_amount'] = self.case_amount.to_alipay_dict()
            else:
                params['case_amount'] = self.case_amount
        if self.estimate_damage_amount:
            if hasattr(self.estimate_damage_amount, 'to_alipay_dict'):
                params['estimate_damage_amount'] = self.estimate_damage_amount.to_alipay_dict()
            else:
                params['estimate_damage_amount'] = self.estimate_damage_amount
        if self.informant:
            if hasattr(self.informant, 'to_alipay_dict'):
                params['informant'] = self.informant.to_alipay_dict()
            else:
                params['informant'] = self.informant
        if self.injured_count:
            if hasattr(self.injured_count, 'to_alipay_dict'):
                params['injured_count'] = self.injured_count.to_alipay_dict()
            else:
                params['injured_count'] = self.injured_count
        if self.injured_list:
            if isinstance(self.injured_list, list):
                for i in range(0, len(self.injured_list)):
                    element = self.injured_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.injured_list[i] = element.to_alipay_dict()
            if hasattr(self.injured_list, 'to_alipay_dict'):
                params['injured_list'] = self.injured_list.to_alipay_dict()
            else:
                params['injured_list'] = self.injured_list
        if self.insure_city:
            if hasattr(self.insure_city, 'to_alipay_dict'):
                params['insure_city'] = self.insure_city.to_alipay_dict()
            else:
                params['insure_city'] = self.insure_city
        if self.insured:
            if hasattr(self.insured, 'to_alipay_dict'):
                params['insured'] = self.insured.to_alipay_dict()
            else:
                params['insured'] = self.insured
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        if self.report_no:
            if hasattr(self.report_no, 'to_alipay_dict'):
                params['report_no'] = self.report_no.to_alipay_dict()
            else:
                params['report_no'] = self.report_no
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.subject_car:
            if hasattr(self.subject_car, 'to_alipay_dict'):
                params['subject_car'] = self.subject_car.to_alipay_dict()
            else:
                params['subject_car'] = self.subject_car
        if self.third_party_car_count:
            if hasattr(self.third_party_car_count, 'to_alipay_dict'):
                params['third_party_car_count'] = self.third_party_car_count.to_alipay_dict()
            else:
                params['third_party_car_count'] = self.third_party_car_count
        if self.third_party_car_list:
            if isinstance(self.third_party_car_list, list):
                for i in range(0, len(self.third_party_car_list)):
                    element = self.third_party_car_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.third_party_car_list[i] = element.to_alipay_dict()
            if hasattr(self.third_party_car_list, 'to_alipay_dict'):
                params['third_party_car_list'] = self.third_party_car_list.to_alipay_dict()
            else:
                params['third_party_car_list'] = self.third_party_car_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsDataAutoFraudQueryModel()
        if 'accident_city' in d:
            o.accident_city = d['accident_city']
        if 'accident_date' in d:
            o.accident_date = d['accident_date']
        if 'accident_location' in d:
            o.accident_location = d['accident_location']
        if 'case_amount' in d:
            o.case_amount = d['case_amount']
        if 'estimate_damage_amount' in d:
            o.estimate_damage_amount = d['estimate_damage_amount']
        if 'informant' in d:
            o.informant = d['informant']
        if 'injured_count' in d:
            o.injured_count = d['injured_count']
        if 'injured_list' in d:
            o.injured_list = d['injured_list']
        if 'insure_city' in d:
            o.insure_city = d['insure_city']
        if 'insured' in d:
            o.insured = d['insured']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'report_date' in d:
            o.report_date = d['report_date']
        if 'report_no' in d:
            o.report_no = d['report_no']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'subject_car' in d:
            o.subject_car = d['subject_car']
        if 'third_party_car_count' in d:
            o.third_party_car_count = d['third_party_car_count']
        if 'third_party_car_list' in d:
            o.third_party_car_list = d['third_party_car_list']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DistributionRentInstallmentInfoDTO import DistributionRentInstallmentInfoDTO


class DistRentPlanInfoDTO(object):

    def __init__(self):
        self._installments = None
        self._rent_days = None
        self._rent_end_time = None
        self._rent_start_time = None
        self._term_type = None

    @property
    def installments(self):
        return self._installments

    @installments.setter
    def installments(self, value):
        if isinstance(value, list):
            self._installments = list()
            for i in value:
                if isinstance(i, DistributionRentInstallmentInfoDTO):
                    self._installments.append(i)
                else:
                    self._installments.append(DistributionRentInstallmentInfoDTO.from_alipay_dict(i))
    @property
    def rent_days(self):
        return self._rent_days

    @rent_days.setter
    def rent_days(self, value):
        self._rent_days = value
    @property
    def rent_end_time(self):
        return self._rent_end_time

    @rent_end_time.setter
    def rent_end_time(self, value):
        self._rent_end_time = value
    @property
    def rent_start_time(self):
        return self._rent_start_time

    @rent_start_time.setter
    def rent_start_time(self, value):
        self._rent_start_time = value
    @property
    def term_type(self):
        return self._term_type

    @term_type.setter
    def term_type(self, value):
        self._term_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.installments:
            if isinstance(self.installments, list):
                for i in range(0, len(self.installments)):
                    element = self.installments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.installments[i] = element.to_alipay_dict()
            if hasattr(self.installments, 'to_alipay_dict'):
                params['installments'] = self.installments.to_alipay_dict()
            else:
                params['installments'] = self.installments
        if self.rent_days:
            if hasattr(self.rent_days, 'to_alipay_dict'):
                params['rent_days'] = self.rent_days.to_alipay_dict()
            else:
                params['rent_days'] = self.rent_days
        if self.rent_end_time:
            if hasattr(self.rent_end_time, 'to_alipay_dict'):
                params['rent_end_time'] = self.rent_end_time.to_alipay_dict()
            else:
                params['rent_end_time'] = self.rent_end_time
        if self.rent_start_time:
            if hasattr(self.rent_start_time, 'to_alipay_dict'):
                params['rent_start_time'] = self.rent_start_time.to_alipay_dict()
            else:
                params['rent_start_time'] = self.rent_start_time
        if self.term_type:
            if hasattr(self.term_type, 'to_alipay_dict'):
                params['term_type'] = self.term_type.to_alipay_dict()
            else:
                params['term_type'] = self.term_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DistRentPlanInfoDTO()
        if 'installments' in d:
            o.installments = d['installments']
        if 'rent_days' in d:
            o.rent_days = d['rent_days']
        if 'rent_end_time' in d:
            o.rent_end_time = d['rent_end_time']
        if 'rent_start_time' in d:
            o.rent_start_time = d['rent_start_time']
        if 'term_type' in d:
            o.term_type = d['term_type']
        return o



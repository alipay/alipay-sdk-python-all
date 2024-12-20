#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GuaranteeDetail import GuaranteeDetail
from alipay.aop.api.domain.GuaranteeDetail import GuaranteeDetail
from alipay.aop.api.domain.RentCarGuaranteeDetailDescription import RentCarGuaranteeDetailDescription
from alipay.aop.api.domain.GuaranteeDetail import GuaranteeDetail
from alipay.aop.api.domain.GuaranteeDetail import GuaranteeDetail
from alipay.aop.api.domain.GuaranteeDetail import GuaranteeDetail
from alipay.aop.api.domain.GuaranteeDetail import GuaranteeDetail


class GuaranteeService(object):

    def __init__(self):
        self._advance_payment_guarantee = None
        self._amount = None
        self._depreciation_guarantee = None
        self._guarantee_detail_description = None
        self._name = None
        self._passenger_guarantee = None
        self._service_description = None
        self._service_exclude_detail = None
        self._service_include_detail = None
        self._stop_business_guarantee = None
        self._supplementary_img = None
        self._third_party_guarantee = None
        self._unique_code = None
        self._vehicle_damage_guarantee = None

    @property
    def advance_payment_guarantee(self):
        return self._advance_payment_guarantee

    @advance_payment_guarantee.setter
    def advance_payment_guarantee(self, value):
        if isinstance(value, GuaranteeDetail):
            self._advance_payment_guarantee = value
        else:
            self._advance_payment_guarantee = GuaranteeDetail.from_alipay_dict(value)
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def depreciation_guarantee(self):
        return self._depreciation_guarantee

    @depreciation_guarantee.setter
    def depreciation_guarantee(self, value):
        if isinstance(value, GuaranteeDetail):
            self._depreciation_guarantee = value
        else:
            self._depreciation_guarantee = GuaranteeDetail.from_alipay_dict(value)
    @property
    def guarantee_detail_description(self):
        return self._guarantee_detail_description

    @guarantee_detail_description.setter
    def guarantee_detail_description(self, value):
        if isinstance(value, list):
            self._guarantee_detail_description = list()
            for i in value:
                if isinstance(i, RentCarGuaranteeDetailDescription):
                    self._guarantee_detail_description.append(i)
                else:
                    self._guarantee_detail_description.append(RentCarGuaranteeDetailDescription.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def passenger_guarantee(self):
        return self._passenger_guarantee

    @passenger_guarantee.setter
    def passenger_guarantee(self, value):
        if isinstance(value, GuaranteeDetail):
            self._passenger_guarantee = value
        else:
            self._passenger_guarantee = GuaranteeDetail.from_alipay_dict(value)
    @property
    def service_description(self):
        return self._service_description

    @service_description.setter
    def service_description(self, value):
        self._service_description = value
    @property
    def service_exclude_detail(self):
        return self._service_exclude_detail

    @service_exclude_detail.setter
    def service_exclude_detail(self, value):
        if isinstance(value, list):
            self._service_exclude_detail = list()
            for i in value:
                self._service_exclude_detail.append(i)
    @property
    def service_include_detail(self):
        return self._service_include_detail

    @service_include_detail.setter
    def service_include_detail(self, value):
        if isinstance(value, list):
            self._service_include_detail = list()
            for i in value:
                self._service_include_detail.append(i)
    @property
    def stop_business_guarantee(self):
        return self._stop_business_guarantee

    @stop_business_guarantee.setter
    def stop_business_guarantee(self, value):
        if isinstance(value, GuaranteeDetail):
            self._stop_business_guarantee = value
        else:
            self._stop_business_guarantee = GuaranteeDetail.from_alipay_dict(value)
    @property
    def supplementary_img(self):
        return self._supplementary_img

    @supplementary_img.setter
    def supplementary_img(self, value):
        self._supplementary_img = value
    @property
    def third_party_guarantee(self):
        return self._third_party_guarantee

    @third_party_guarantee.setter
    def third_party_guarantee(self, value):
        if isinstance(value, GuaranteeDetail):
            self._third_party_guarantee = value
        else:
            self._third_party_guarantee = GuaranteeDetail.from_alipay_dict(value)
    @property
    def unique_code(self):
        return self._unique_code

    @unique_code.setter
    def unique_code(self, value):
        self._unique_code = value
    @property
    def vehicle_damage_guarantee(self):
        return self._vehicle_damage_guarantee

    @vehicle_damage_guarantee.setter
    def vehicle_damage_guarantee(self, value):
        if isinstance(value, GuaranteeDetail):
            self._vehicle_damage_guarantee = value
        else:
            self._vehicle_damage_guarantee = GuaranteeDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.advance_payment_guarantee:
            if hasattr(self.advance_payment_guarantee, 'to_alipay_dict'):
                params['advance_payment_guarantee'] = self.advance_payment_guarantee.to_alipay_dict()
            else:
                params['advance_payment_guarantee'] = self.advance_payment_guarantee
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.depreciation_guarantee:
            if hasattr(self.depreciation_guarantee, 'to_alipay_dict'):
                params['depreciation_guarantee'] = self.depreciation_guarantee.to_alipay_dict()
            else:
                params['depreciation_guarantee'] = self.depreciation_guarantee
        if self.guarantee_detail_description:
            if isinstance(self.guarantee_detail_description, list):
                for i in range(0, len(self.guarantee_detail_description)):
                    element = self.guarantee_detail_description[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.guarantee_detail_description[i] = element.to_alipay_dict()
            if hasattr(self.guarantee_detail_description, 'to_alipay_dict'):
                params['guarantee_detail_description'] = self.guarantee_detail_description.to_alipay_dict()
            else:
                params['guarantee_detail_description'] = self.guarantee_detail_description
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.passenger_guarantee:
            if hasattr(self.passenger_guarantee, 'to_alipay_dict'):
                params['passenger_guarantee'] = self.passenger_guarantee.to_alipay_dict()
            else:
                params['passenger_guarantee'] = self.passenger_guarantee
        if self.service_description:
            if hasattr(self.service_description, 'to_alipay_dict'):
                params['service_description'] = self.service_description.to_alipay_dict()
            else:
                params['service_description'] = self.service_description
        if self.service_exclude_detail:
            if isinstance(self.service_exclude_detail, list):
                for i in range(0, len(self.service_exclude_detail)):
                    element = self.service_exclude_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_exclude_detail[i] = element.to_alipay_dict()
            if hasattr(self.service_exclude_detail, 'to_alipay_dict'):
                params['service_exclude_detail'] = self.service_exclude_detail.to_alipay_dict()
            else:
                params['service_exclude_detail'] = self.service_exclude_detail
        if self.service_include_detail:
            if isinstance(self.service_include_detail, list):
                for i in range(0, len(self.service_include_detail)):
                    element = self.service_include_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_include_detail[i] = element.to_alipay_dict()
            if hasattr(self.service_include_detail, 'to_alipay_dict'):
                params['service_include_detail'] = self.service_include_detail.to_alipay_dict()
            else:
                params['service_include_detail'] = self.service_include_detail
        if self.stop_business_guarantee:
            if hasattr(self.stop_business_guarantee, 'to_alipay_dict'):
                params['stop_business_guarantee'] = self.stop_business_guarantee.to_alipay_dict()
            else:
                params['stop_business_guarantee'] = self.stop_business_guarantee
        if self.supplementary_img:
            if hasattr(self.supplementary_img, 'to_alipay_dict'):
                params['supplementary_img'] = self.supplementary_img.to_alipay_dict()
            else:
                params['supplementary_img'] = self.supplementary_img
        if self.third_party_guarantee:
            if hasattr(self.third_party_guarantee, 'to_alipay_dict'):
                params['third_party_guarantee'] = self.third_party_guarantee.to_alipay_dict()
            else:
                params['third_party_guarantee'] = self.third_party_guarantee
        if self.unique_code:
            if hasattr(self.unique_code, 'to_alipay_dict'):
                params['unique_code'] = self.unique_code.to_alipay_dict()
            else:
                params['unique_code'] = self.unique_code
        if self.vehicle_damage_guarantee:
            if hasattr(self.vehicle_damage_guarantee, 'to_alipay_dict'):
                params['vehicle_damage_guarantee'] = self.vehicle_damage_guarantee.to_alipay_dict()
            else:
                params['vehicle_damage_guarantee'] = self.vehicle_damage_guarantee
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GuaranteeService()
        if 'advance_payment_guarantee' in d:
            o.advance_payment_guarantee = d['advance_payment_guarantee']
        if 'amount' in d:
            o.amount = d['amount']
        if 'depreciation_guarantee' in d:
            o.depreciation_guarantee = d['depreciation_guarantee']
        if 'guarantee_detail_description' in d:
            o.guarantee_detail_description = d['guarantee_detail_description']
        if 'name' in d:
            o.name = d['name']
        if 'passenger_guarantee' in d:
            o.passenger_guarantee = d['passenger_guarantee']
        if 'service_description' in d:
            o.service_description = d['service_description']
        if 'service_exclude_detail' in d:
            o.service_exclude_detail = d['service_exclude_detail']
        if 'service_include_detail' in d:
            o.service_include_detail = d['service_include_detail']
        if 'stop_business_guarantee' in d:
            o.stop_business_guarantee = d['stop_business_guarantee']
        if 'supplementary_img' in d:
            o.supplementary_img = d['supplementary_img']
        if 'third_party_guarantee' in d:
            o.third_party_guarantee = d['third_party_guarantee']
        if 'unique_code' in d:
            o.unique_code = d['unique_code']
        if 'vehicle_damage_guarantee' in d:
            o.vehicle_damage_guarantee = d['vehicle_damage_guarantee']
        return o


